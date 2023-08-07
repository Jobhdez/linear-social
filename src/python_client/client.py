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

def request_friend(to_user_id, from_user, from_user_password):
    link = URL + 'request/'
    data = {'id': to_user_id}
    auth = (from_user, from_user_password)
    re = requests.post(link, data=data, auth=auth)
    return re.json()

def accept(to_user_id, user_name_accepting, user_password_accepting):
    link = URL + 'accept/'
    data = {'id': to_user_id}
    auth = (user_name_accepting, user_password_accepting)
    re = requests.post(link, data=data, auth=auth)
    return re.json()

def compute(exp, user_name, user_password):

    link = URL + 'compute/'
    data = {'exp': exp}
    auth = (user_name, user_password)
    re = requests.post(link, data=data, auth=auth)
    return re.json()

