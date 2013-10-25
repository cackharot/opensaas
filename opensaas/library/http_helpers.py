from webob import Response
import urllib2
import socket
import base64
from urlparse import urlparse, urlunparse
import urllib

def get_url(url, method='GET', data=None, client_id=None, user_id=None, api_key=None, timeout=5,
            get_body=True, extra_headers=None):
    """Performs a synchronous url call and returns the status and body.

This function is to be used to provide a gateway service.

If the url is not answering after `timeout` seconds, the function will
return a (504, {}, error).

If the url is not reachable at all, the function will
return (502, {}, error)

Other errors are managed by the urrlib2.urllopen call.

Args:
- url: url to visit
- method: method to use
- data: data to send
- user: user to use for Basic Auth, if needed
- password: password to use for Basic Auth
- timeout: timeout in seconds.
- extra headers: mapping of headers to add
- get_body: if set to False, the body is not retrieved

Returns:
- tuple : status code, headers, body
"""
    if isinstance(api_key, unicode):
        api_key = api_key.encode('utf-8')
        
    if data and isinstance(data,dict):
        data = urllib.urlencode(data)

    req = urllib2.Request(url, data=data)
    req.get_method = lambda: method

    if client_id and user_id and api_key:
        req.add_header("client_id", client_id)
        req.add_header("user_id", user_id)
        req.add_header("api_key", api_key)

    if extra_headers is not None:
        for name, value in extra_headers.items():
            req.add_header(name, value)

    try:
        res = urllib2.urlopen(req, timeout=timeout)
    except urllib2.HTTPError, e:
        if hasattr(e, 'headers'):
            headers = dict(e.headers)
        else:
            headers = {}

        if hasattr(e, 'read'):
            body = e.read()
        else:
            body = ''

        return e.code, headers, body

    except urllib2.URLError, e:
        if isinstance(e.reason, socket.timeout):
            return 504, {}, str(e)
        return 502, {}, str(e)

    if get_body:
        body = res.read()
    else:
        body = ''

    return res.getcode(), dict(res.headers), body
