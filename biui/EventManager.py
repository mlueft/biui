import biui

##
#
#
class EventManager (object):

	##
	#
	#
	def __init__(self):
		self.__qeue_misc = []

	##
	#
	#
	def register(self, type, callback ):
		if type == biui.EventTypes.MISC:
			# Prevent callbacks from regictered twice.
			if callback not in self.__qeue_misc:
				self.__qeue_misc.append(callback)
		else:
			raise ValueError("EventType: '"+str(type)+"' not recognized!")

	##
	#
	#
	def unregister(self, type, callback):
		if type == biui.EventTypes.MISC:
			self.__qeue_misc.remove(callback)
		else:
			raise ValueError("EventType: '"+str(type)+"' not recognized!")

	##
	#
	#
	def pour(self, type, event = None):
		if type == biui.EventTypes.MISC:
			for callback in self.__qeue_misc:
				callback(event)
			return
		else:
			raise ValueError("EventType: '"+str(type)+"' not recognized!")
			