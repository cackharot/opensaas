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
import uuid
import datetime

def datetime_adapter(obj, request):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)

def uuid_adapter(obj, request):
    if isinstance(obj, uuid.UUID):
        return str(obj)
    else:
        return None

def db_json_renderer(helper):
    json_renderer = _JsonRenderer()
    #json_renderer.add_adapter(datetime.datetime, datetime_adapter)
    #json_renderer.add_adapter(uuid.UUID, uuid_adapter)
    return json_renderer

class _JsonRenderer(object):
    def __call__(self, data, context):
        acceptable = ('application/json', 'text/json', 'text/plain')
        response = context['request'].response
        content_type = (context['request'].accept.best_match(acceptable)
                        or acceptable[0])
        response.content_type = content_type
        return json.dumps(data, default=json_util.default, use_decimal=True)
