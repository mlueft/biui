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
		self.__handlers.remove(handler)

	##
	#
	#
	def provoke(self, event):
		for handler in self.__handlers:
			handler(event)
			