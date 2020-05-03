from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session

from helpers  import get_reviews_count,login_required

from db import db

book_blueprint = Blueprint('book_blueprint',__name__)

@book_blueprint.route("/search",methods=['GET','POST'])
@login_required
def search():
    # print(request.method)
    if request.method=='POST':

        print('hi')

        q = request.form.get('search')

        q = '%' + q + "%"
        print(q)

        result = db.execute(''' Select * from books where isbn LIKE :q
                                OR title LIKE :q or author LIKE :q ''',{"q" : q})
        
       
        
        results = tuple(result)

        # for isbn,title,author, year in result:
        #     result_list.append(f''' {isbn} , {title}, {author}, {year} ''')



        result.close()

        return render_template('search_result.html', results=results)
    else:
        return render_template('search.html')


@book_blueprint.route("/book/<isbn>",methods=['GET','POST'])
@login_required
def book(isbn):

    result = db.execute(''' SELECT * from reviews where username=:username and isbn=:isbn''',{'username': session['username'],'isbn':isbn})

    # print(result)

    user_review=result.first()

    if request.method == 'POST':
        print('hihihij')
        if not user_review:
            rating=request.form.get('rating')
            review_text= request.form.get('review_text')
            print(review_text)
            print(rating)

            db.execute('''INSERT INTO reviews 
                        (rating,review_text,username,isbn) 
                        VALUES 
                        (:rating, :review_text, :username , :isbn ) ''',
                        {'rating' : rating,'review_text': review_text,'username':session['username'], 'isbn':isbn})
            
            db.commit()
            

            return redirect('/book/'+isbn)
    elif request.method == 'GET':
        review_exists = user_review is not None

        result=db.execute(''' SELECT * from books where isbn= :isbn''',{'isbn' : isbn })

        books_dict=[]

        for row in result:
            books_dict= dict(row)

        api_result= get_reviews_count(books_dict['isbn'])

        print(api_result)

        if api_result is None:
            books_dict['average_rating'] = None
            books_dict['work_rating'] = None

        else:   
            books_dict['average_rating'] =api_result['books'][0]['average_rating']
            books_dict['work_rating'] = api_result['books'][0]['work_ratings_count']

        

        get_review= db.execute(''' SELECT rating,review_text, username from reviews where isbn= :isbn ''',{'isbn' : isbn})

        review_result=[]

        for row in get_review:
            review_result.append(dict(row))
        
        print(review_result)
        
        return render_template('book.html' , 
                                book_dict=books_dict, 
                                review_result= review_result, 
                                review_exists=review_exists)
              
    

