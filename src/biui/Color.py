import biui

###
##
##
class Color():
    
    def __init__(self,r=0,g=0,b=0,a=255):
        self._r = r
        self._g = g
        self._b = b
        self._a = a
        
    ###
    ##
    ##
    @property
    def r(self):
        return self._r
    
    ###
    ##
    ##
    @r.setter
    def r(self,value):
        self._r = value
        
    ###
    ##
    ##
    @property
    def g(self):
        return self._g
    
    ###
    ##
    ##
    @g.setter
    def g(self,value):
        self._g = value
        
    ###
    ##
    ##
    @property
    def b(self):
        return self._b
    
    ###
    ##
    ##
    @b.setter
    def b(self,value):
        self._b = value
        
    ###
    ##
    ##
    @property
    def a(self):
        return self._a
    
    ###
    ##
    ##
    @a.setter
    def a(self,value):
        self._a = value
        
    @property
    def rgba(self):
        return(self.r,self.g,self.b,self.a)