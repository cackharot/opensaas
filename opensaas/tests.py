import unittest

from pyramid import testing
from service_proxies.user_proxy import UserProxy

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from opensaas.views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'opensaas')
        
    def test_get_users(self):
        proxy = UserProxy()
        users = proxy.get_users(client_id=1111)
        print users
        self.assertEqual(True,True)
        
    def test_create_user(self):
        proxy = UserProxy()
        user = {
            "user" : {
                    "client_id"  : "1111",
                    "first_name" : "john",
                    "last_name"  : "smith",
                    "email"      : "john.smith@gmail.com",
                    "contact"    : {
                        "address" : "new address",
                        "state"   : "Lior",
                        "country" : "amestries",
                        "zip"     : "256321",
                        "phone"   : "14587965230"
                    }
                },
            "membership" : {
                "username" : "john",
                "password" : "pass#231"
            }
        }
        resp = proxy.create_user(user,client_id=1111)
        print resp
        self.assertEqual(True,True)

