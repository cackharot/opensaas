import os
import binascii
import json

from webob import Response, exc
from .oservice import OService
from cornice import Service

users = OService(name='users', path='/users', description="User registration")

@users.get()
def get_users(request):
    """Returns a list of all users."""
    query = request.db['users'].find()
    users = [x for x in query]
    print users
    return { 'status': 'success', 'users': users }

@users.put()
def create_user(request):
    """Adds a new user."""
    user = request.json_body
    print user
    if user:
        request.db['users'].insert(user)
    return { 'status': 'created', 'user' : user }
    
@users.post()
def update_user(request):
    """Update user details."""
    user = request.json_body
    #print user
    if user:
        try:
            request.db['users'].save(user)
            user = request.db['users'].find_one(user['_id'])
        except Exception as e:
            print e
    return { 'status': 'updated', 'user' : user }

@users.delete()
def del_user(request):
    """Removes the user."""
    data = request.json_body
    print data
    if data.id:
        request.db['users'].remove(data.id)
    return { 'status': 'deleted' }
