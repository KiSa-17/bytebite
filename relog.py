import json
from database import newuser, getuser
from jwtreq import create_token

def register(data):
    username = data.get('username')
    password = data.get('password')
    newuser(username, password)
    return {"message": "User created"}, 201

def login(data):
    username = data.get('username')
    password = data.get('password')
    user = getuser(username)
    if not user or user['password'] != password:
        return {"message": "Invalid credentials"}, 401
    token = create_token(user['id'])
    return {"access_token": token}, 200
