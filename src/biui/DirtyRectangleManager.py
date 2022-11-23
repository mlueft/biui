import biui

### 
##  
##  
##  
class DirtyRectangleManager():
    
    def __init__(self):
        self._xmin1 = []
        self._ymin1 = []
        self._xmax1 = []
        self._ymax1 = []
        self._xmin = 10000
        self._ymin = 10000
        self._xmax = 0
        self._ymax = 0
        self._recs = []

        v = 2
        if v == 0:
            self.add = self.add0
            self.getRectangles = self.getRectangles0
        elif v == 1:
            self.add = self.add1
            self.getRectangles = self.getRectangles1
        elif v == 2:
            self.add = self.add2
            self.getRectangles = self.getRectangles2
        elif v == 3:
            self.add = self.add3
            self.getRectangles = self.getRectangles2  

    def add0(self,rect):
        self._xmin1.append(rect[0])
        self._ymin1.append(rect[1])
        self._xmax1.append(rect[0]+rect[2])
        self._ymax1.append(rect[1]+rect[3])

            
    def add1(self,rect):
        self._xmin = min(self._xmin,rect[0])
        self._ymin = min(self._ymin,rect[1])
        self._xmax = max(self._xmax,rect[0]+rect[2])
        self._ymax = max(self._ymax,rect[1]+rect[3])

    def add11(self,rect):
        if rect[0] < self._xmin:
            self._xmin = rect[0]
        
        if rect[1] < self._ymin:
            self._ymin = rect[1]
            
        if rect[0]+rect[2] > self._xmax:
            self._xmax = rect[0]+rect[2]
            
        if rect[1]+rect[3] > self._ymax:
            self._ymax = rect[1]+rect[3]
        
    def add2(self,rect):
        self._recs.append(rect)

    def add(self,rect):
        
        extended = False
        for e in self._recs:
            pass
            
            
        self._recs.append(rect)
                
    def getRectangles0(self):
        result = [(
            min(self._xmin1),
            min(self._ymin1),
            max(self._xmax1),
            max(self._ymax1)
        )]
        self._xmin = []
        self._ymin = []
        self._xmax = []
        self._ymax = []
        return result

    def getRectangles1(self):
        result = [(self._xmin,self._ymin,self._xmax,self._ymax)]
        self._xmin = 10000
        self._ymin = 10000
        self._xmax = 0
        self._ymax = 0
        return result

    def getRectangles2(self):
        result = self._recs.copy()
        self._recs.clear()
        return result