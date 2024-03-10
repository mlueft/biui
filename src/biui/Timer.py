import biui
from biui.Events import EventManager,Event
from time import time

class Timer():
    
    ###
    ##
    ##
    def __init__(self,interval,callback):
        self.__interval = interval
        self.__lastThickTime =  time()*1000
        self.__active = True
        
        self.tick:EventManager = EventManager()
        self.tick.add(callback)
        biui.addTimer(self)
        
    ###
    ##
    ##
    def main(self):
        
        if False == self.__active:
            return
        
        currentTime = time()*1000
        
        if currentTime-self.__lastThickTime < self.__interval:
            return
    
        self.tick.provoke(Event(self))
        
        self.__lastThickTime = currentTime
        
    ###
    ##
    ##
    @property
    def active(self):
        return self.__active
    
    ###
    ##
    ##
    @active.setter
    def active(self,value):
        self.__active = value
