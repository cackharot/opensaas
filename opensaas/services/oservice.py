from cornice import Service
#from cornice.service import get_services

class OService(Service):
	def __init__(self,name,path,description,**kw):
		Service.__init__(self, name='users', path='/users', description="User registration", depth=2,**kw)
		pass
	pass

