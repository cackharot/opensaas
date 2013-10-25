from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.url import route_url
from pyramid.config.settings import asbool
from pyramid.interfaces import IAuthenticationPolicy
from pyramid.interfaces import IAuthorizationPolicy
from pyramid.security import unauthenticated_userid
from pyramid.authentication import AuthTktCookieHelper
from pyramid.security import Allow, Everyone, Authenticated
from pyramid.security import authenticated_userid
from zope.interface import implements

import logging
log = logging.getLogger(__name__)

from pyramid.events import subscriber
from pyramid.events import BeforeRender

test_identity = { 
            'user_id' : 123, 
            'user' : {}, 
            'client_id' : 1111, 
            'client': {},
            'roles' : [],
            'privileges' : [],
            'api_key' : 'oh so secret api key'
            }

def add_user_context_to_request(event):
    settings = event.request.registry.settings
    req = event.request
    headers = req.headers
    client_id = headers.get('client_id',None)
    user_id = headers.get('user_id',None)
    api_key = headers.get('api_key',None)

    identity = {}
    
    if client_id and user_id and api_key:
        if validate(client_id,user_id,api_key):
            identity['client_id'] = client_id
            identity['user_id'] = user_id
            identity['api_key'] = api_key
    elif not settings.get('test_user_identity',None):
        identity = test_identity
    event.request['user_identity'] = identity
    print identity
    pass
    
def validate(client_id,user_id,api_key):
    return True

def get_user(request):
    user_id = unauthenticated_userid(request)
    if user_id:
        return { 'user_id' : user_id }
    return None

class SaaSAuthTktAuthenticationPolicy(object):
    implements(IAuthenticationPolicy)
    """
        Custom AUthentication Ticket policy
    """
    def __init__(self, settings):
        self.client_id = None
        self.user_id   = None
        self.api_key   = None

    def remember(self, request, principal, **kw):
        return None

    def forget(self, request):
        return None

    def unauthenticated_userid(self, request):
        headers = request.headers
        user_id = headers.get('user_id',None)
        return user_id

    def authenticated_userid(self, request):
        headers = request.headers
        client_id = headers.get('client_id',None)
        user_id = headers.get('user_id',None)
        api_key = headers.get('api_key',None)
        print client_id, user_id, api_key
        if client_id and user_id and api_key:
            if validate(client,user_id,api_key):
                return user_id
        return None

    def effective_principals(self, request):
        principals = [Everyone]
        user = request.user
        if user:
            principals += [Authenticated, 'u:%s' % user.Id]
            principals.extend(('g:%s' % g for g in ['admin', 'user']))
            log.info(principals)
        return principals


class UserAuthorizationPolicy(object):
    implements(IAuthorizationPolicy)
    """
        Custom User authorization policy
    """
    def permits(self, context, principals, permission):
        return True

    def principals_allowed_by_permission(self, context, permission):
        raise NotImplementedError('Method Not Implemented.')

    pass
