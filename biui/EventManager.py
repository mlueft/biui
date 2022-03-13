import biui

##
#
#
class EventManager (object):

	##
	#
	#
	def __init__(self):
		self.__handlers= []

	##
	#
	#
	def add(self, handler):
		self.__handlers.append(handler)

	##
	#
	#
	def remove(self, handler):
		if handler not in self.__handlers:
			return
		 
		self.__handlers.remove(handler)

	##
	#
	#
	def has(self,handler):
		return handler in self.__handlers
	
	##
	#
	#
	def provoke(self, event):
		for handler in self.__handlers:
			handler(event)
			