import biui

###
##
##
class Color():
    
    ###
    ##
    ##
    def __init__(self,r=0,g=0,b=0,a=255):
        self._r = r
        self._g = g
        self._b = b
        self._a = a
        
    ### Returns the red value of the color.
    ##
    ##  @return     An integer between 0 and 255.
    ##
    @property
    def r(self):
        return self._r
    
    ### Sets the red value of the color.
    ##
    ##  @param value   An integer value between 0 and 255.
    ##
    @r.setter
    def r(self,value):
        self._r = value
        
    ### Returns the green value of the color.
    ##
    ##  @return     An integer between 0 and 255.
    ##
    @property
    def g(self):
        return self._g
    
    ### Sets the green value of the color.
    ##
    ##  @param value   An integer value between 0 and 255.
    ##
    @g.setter
    def g(self,value):
        self._g = value
        
    ### Returns the blue value of the color.
    ##
    ##  @return     An integer between 0 and 255.
    ##
    @property
    def b(self):
        return self._b
    
    ### Sets the blue value of the color.
    ##
    ##  @param value   An integer value between 0 and 255.
    ##
    @b.setter
    def b(self,value):
        self._b = value
        
    ### Returns the alpha value of the color.
    ##
    ##  @return     An integer between 0 and 255.
    ##
    @property
    def a(self):
        return self._a
    
    ### Sets the alpha value of the color.
    ##
    ##  @param value   An integer value between 0 and 255.
    ##
    @a.setter
    def a(self,value):
        self._a = value
        
    ### Liefert ein Tuple mit rot, grün, blau unf alpha.
    ##
    ## @return     (r,g,b,a)  Tupel mit den Farbwerten.
    ##
    @property
    def rgba(self):
        return(self.r,self.g,self.b,self.a)
    
    ### Liefert ein Tuple mit alpha, rot, grün und blau.
    ##
    ## @return     (a,r,g,b)  Tupel mit den Farbwerten.
    ##
    @property
    def argb(self):
        return(self.a,self.r,self.g,self.b)
    
        