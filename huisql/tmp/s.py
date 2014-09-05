class Singleton(object):
    def __init__(self):
	pass
    def __new__(self,name):
	self.a=name
        return self



