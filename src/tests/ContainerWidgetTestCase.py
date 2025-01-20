import unittest
import os

import biui
from biui.Widgets import Window, Widget, ContainerWidget
from .WidgetTestCase import WidgetTestCase

class ContainerWidgetTestCase(WidgetTestCase):
    
    def createSubject(self,type="ContainerWidget"):
        if type == "ContainerWidget":
            return ContainerWidget()        
        return super().createSubject(type)
    
    def setUp(self):
        super().setUp()
 
    def tearDown(self):
        super().tearDown()
    
    def testChildren0(self):
        subject = self.createSubject()
        c0 = Widget()
        c1 = Widget()
        subject.addChild(c0) 
        subject.addChild(c1)
        """test Widget.children"""
        assert subject.children == [c0,c1], "Widget.children not set correctly."

    def testHasChild(self):
        subject = self.createSubject()
        c0 = Widget()
        subject.addChild(c0) 
        """test Widget.hasChildren"""
        assert subject.hasChild(c0) == True, "Widget.hasChildren not set correctly."
    
    def testRemoveChild0(self):
        subject = self.createSubject()
        c0 = Widget()
        c1 = Widget()
        subject.addChild(c0) 
        subject.addChild(c1)
        subject.removeChild(c0)
        """test Widget.removeChildren"""
        assert subject.children == [c1], "Widget.removechildren not set correctly."
    
    def testRemoveChild1(self):
        subject = self.createSubject()
        c0 = Widget()
        c1 = Widget()
        subject.addChild(c0) 
        subject.addChild(c1)
        subject.removeChild(c0)
        subject.removeChild(c1)
        """test Widget.removeChildren"""
        assert subject.children == [], "Widget.removechildren not set correctly."
        
    def testAddChild(self):
        assert 1==1, ""
    
    def testGetChildAt0(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.x = 100
        subject.y = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.x = 10
        c0.y = 10
        c0.width = 50
        c0.height = 50
        subject.addChild(c0)
        
        print(subject.getChildAt((11,11)))
        
        """test Widget.getChildAt"""
        assert subject.getChildAt((110,110)) == c0, "Widget.getChildAt not set correctly."
    
    def testGetChildAt1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.x = 100
        subject.y = 100
        wnd.addChild(subject)
        
        c0 = self.createSubject()
        c0.x = 10
        c0.y = 10
        c0.width = 100
        c0.height = 100
        subject.addChild(c0) 
        
        c1 = self.createSubject("Button")
        c1.x = 10
        c1.y = 10
        c0.addChild(c1)
        
        """test Widget.removeChildren"""
        value = subject.getChildAt((121,121))
        assert value == c1, "Widget.getChildAt({}) not set correctly.".format(value)
        
    def _testIsInvalide0(self):
        assert 1==1, ""
    
    def _testLayoutManager(self):
        assert 1==1, ""

    def _testGetDirtyRectAngle(self):
        assert 1==1, ""
    
    def _testCalculateLayout(self):
        assert 1==1, ""
    
    def _testInvalidate(self):
        assert 1==1, ""
    

                                         
    """ "
    connectScrollNavigator
    disconnectScrollNavigator

    children
    hasChild
    removeChild
    renderRect
    toLocal
    toGlobal
    onChildAdded
    onChildRemoved
    onScrollPositionChanged
    """ #"
if __name__ == "__main__":
    unittest.main() ## run all tests