from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
from .library.dbhelper import add_db_to_request, init_db_conn, db_json_renderer
from .library.authhelper import add_user_context_to_request, get_user
from .library.authhelper import SaaSAuthTktAuthenticationPolicy
from .library.authhelper import UserAuthorizationPolicy

from opensaas.resources import Root

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    # Configure our authorisation policy
    authn_policy = SaaSAuthTktAuthenticationPolicy(settings)
    authz_policy = UserAuthorizationPolicy()
    
    config = Configurator(settings=settings, 
                            root_factory=Root,
                            authentication_policy=authn_policy,
                            authorization_policy=authz_policy)
    
    config.include("cornice")
    #config.add_static_view('static', 'opensaas:static')
    
    init_db_conn(config,settings)
    config.set_request_property(get_user, 'user_identity', reify=True)
    
    config.add_subscriber(add_db_to_request, NewRequest)
    config.add_subscriber(add_user_context_to_request, NewRequest)
    config.add_renderer('json', db_json_renderer)
    config.add_renderer('simplejson', db_json_renderer)
    
    config.scan('opensaas')
    return config.make_wsgi_app()
