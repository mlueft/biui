import biui

### TODO: Does a file based cache make sense?
##        So we do not have to recompose all
##        images at each program start.
##
class DirtyRectangleManager():
    
    def __init__(self):
        self._xmin = 10000
        self._ymin = 10000
        self._xmax = 0
        self._ymax = 0
        
        ##self._recs = []
    
    def add(self,rect):
        self._xmin = min(self._xmin,rect[0])
        self._ymin = min(self._ymin,rect[1])
        self._xmax = max(self._xmax,rect[0]+rect[2])
        self._ymax = max(self._ymax,rect[1]+rect[3])
        ##self._recs.append(rect)
        
    def getRectangles(self):
        
        
        result = [(self._xmin,self._ymin,self._xmax,self._ymax)]
        
        self._xmin = 10000
        self._ymin = 10000
        self._xmax = 0
        self._ymax = 0
        
        ##print(result) 
        return result
    
        result = self._recs.copy()
        self._recs.clear()
        return result
        