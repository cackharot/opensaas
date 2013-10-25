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
    user_mem = request.json_body
    user = user_mem.get('user',None)
    membership = user_mem.get('membership',None)
    print user
    print membership
    if user:
        try:
            if membership:
                request.db['user_memberships'].insert(membership)
                user['membership_id'] = membership['_id']
            request.db['users'].insert(user)
        except Exception as e:
            print e
        
    return { 'status': 'created', 'user' : user }
    
@users.post()
def update_user(request):
    """Update user details."""
    user_mem = request.json_body
    user = user_mem.get('user',None)
    membership = user_mem.get('membership',None)
    print user
    print membership
    if user:
        try:
            if membership:
                request.db['user_memberships'].save(membership)
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
        user = request.db['users'].find_one(data.id)
        if user:
            request.db['user_memberships'].remove(user.membership_id)
            request.db['users'].remove(data.id)
            return { 'status': 'deleted' }
    return { 'status': 'error', 'message' : 'user not found!' }
