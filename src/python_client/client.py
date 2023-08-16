import requests
import json

"""This module corresponds to a client for my API in `src/server/api/views.py`.
I made this so I can test my API.

Usage:
     $ python manage.py runserver
     $ python
     >>> from src.python_client.client import *
     >>> register(<password>, <username>, <first_name>, <email>)
     >>> {'account': 'created'}
"""

URL = 'http://127.0.0.1:8000/api/'

def login(username, password):
    link = URL + 'login/'
    data = {'username': username, 'password': password}
    re = requests.post(link, data=data)
    return re.json()

def register(password, username, first_name, email):
    link = URL + 'register/'
    data = {'password': password, 'password2': password, 'username':username, 'first_name': first_name, 'email': email}
    re = requests.post(link, data=data)
    return re.json()

def request_friend(to_username, from_user, from_user_password):
    link = URL + 'request/'
    data = {'username': to_username}
    auth = (from_user, from_user_password)
    re = requests.post(link, data=data, auth=auth)
    return re.json()

def accept(username_whos_accepted, user_whos_accepting, user_whos_accepting_password):
    """
    accept: accepts a friend request

    Example:
        >>> accept('jobpink3', 'jobpink', 'hello123')
        >>> {'accept': 'request'}

    Note: here 'jobpink` is accepting `jobpink3`.
    """
    link = URL + 'accept/'
    data = {'username': username_whos_accepted}
    auth = (user_whos_accepting, user_whos_accepting_password)
    re = requests.post(link, data=data, auth=auth)
    return re.json()

def compute(exp, user_name, user_password):

    link = URL + 'compute/'
    data = {'exp': exp}
    auth = (user_name, user_password)
    re = requests.post(link, data=data, auth=auth)
    return re.json()


def dashboard(username, password):
    """this endpoint returns the activity feed of the account associated with
    the parameters `username`, and `password`."""
    link = URL + 'dashboard/'
    auth=(username, password)
    re = requests.post(link, auth=auth)
    return re.json()

def create_study(username, password, study_name):
    link = URL + 'create_study/'
    auth=(username,password)
    data = {'name': study_name}
    re = requests.post(link, data=data, auth=auth)
    return re.json()

def join_study(username, password, to_user, study_name):
    link = URL + 'join_study/'
    auth = (username, password)
    data = {'to_user': to_user, 'study_name': study_name}
    re = requests.post(link, data=data, auth=auth)
    return re.json()
