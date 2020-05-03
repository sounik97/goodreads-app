from db import db
from pprint import pprint
import sys

# def test(isbn):
    # result = db.execute (''' Select * from books limit 10 ''')
    # result_dict = []

    # for row in result:
    #     result_dict = dict(row)
        
    # pprint(result_dict)
    # print(sys.getsizeof(result_dict))

    # result_dict['id']=isbn

    # print(result_dict)


# test('0142501085')
rating=2
review_text='nice'
username='sounik97'
isbn='1632168146'

res = db.execute('''INSERT INTO reviews (rating,review_text,username,isbn) 
                    VALUES (:rating, :review_text, :username , :isbn );''',
                    {'rating' : rating,
                    'review_text': review_text,
                    'username':username, 'isbn':isbn})


print(list(db.execute('select * from reviews;')))

db.commit()
# if __name__ == "__main__":
#     app.run(debug=True)




