import uuid
import hashlib
import urllib.parse
import requests

from functools  import wraps
from flask import session
from flask import redirect
from flask import url_for
from flask import request
# import urllib.parse


def hash_password(password):
    salt=uuid.uuid4().hex
    hash_password= hashlib.sha256(salt.encode()+password.encode()).hexdigest()+':'+salt
    return hash_password


def check_password(hash_password, user_password):
    password,salt = hash_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('user_blueprint.login'))

        return func(*args, **kwargs)
    
    return inner

def get_reviews_count(isbn):
    print('hahahah')

    dev_key = 'pGtcbDoTAXhZeqljBPExg'

    base_url = "https://www.goodreads.com/book/review_counts.json"

    response = requests.get( base_url, params={'isbns':isbn, 'key':dev_key })
    # params={'isbn':isbn, 'key':dev_key }
    # full_url= base_url+ urllib.parse.urlencode(params)
    print(dir(response))
    try:
        # response=requests.get(full_url)
        print(response.url)
        json_data=response.json()
        # print(json_data)
    except:
        return None
    return json_data

    


    print(json_data)

    # get_date=json_data.firstone()

    work_rating= json_data['books'][0]['work_ratings_count']
    average_rating =  json_data['book'][0]['average_rating']

    if not work_rating:
        work_rating = 'Not Found'
    if not average_rating:
        average_rating = 'Not Found'


    reviews_count = {'work_rating' : work_rating, 'average_rating' : average_rating}

    return reviews_count



