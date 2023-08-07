import requests
import json


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

    Note: here 'jobpink` is accepting `jobpink3` who is the accepted
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
    """this endpoints returns that activity stream of the account associated with
    the parameters `username`, and `password`."""
    link = URL + 'dashboard/'
    auth=(username, password)
    re = requests.post(link, auth=auth)
    return re.json()
