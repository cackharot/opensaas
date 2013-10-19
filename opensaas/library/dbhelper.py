import pymongo

def init_db_conn(config,settings):
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.Connection
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.Connection):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn

# MongoDB
def add_db_to_request(event):
    settings = event.request.registry.settings
    url = settings['mongodb.url']
    db_name = settings['mongodb.db_name']
    db = settings['mongodb_conn'][db_name]
    event.request.db = db
    event.request.add_finished_callback(cleanup_callback)

def cleanup_callback(request):
    pass

from bson import json_util
import simplejson as json

def db_json_renderer(helper):
    return _JsonRenderer()

class _JsonRenderer(object):
    def __call__(self, data, context):
        acceptable = ('application/json', 'text/json', 'text/plain')
        response = context['request'].response
        content_type = (context['request'].accept.best_match(acceptable)
                        or acceptable[0])
        response.content_type = content_type
        return json.dumps(data, default=json_util.default, use_decimal=True)
