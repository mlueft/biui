import os
import unittest
import biui
from biui.Widgets import Widget,NumberSlider, ScrollableContainerWidget, Button, ButtonGroup, Window, Pane
from biui.Enum import Alignment

from .ContainerWidgetTestCase import ContainerWidgetTestCase

class ScrollableContainerWidgetTestCase(ContainerWidgetTestCase):
    
    def createSubject(self,type="ScrollableContainerWidget"):
        
        if type == "ScrollableContainerWidget":
            return ScrollableContainerWidget()
        
        return super().createSubject(type)
    
    def setUp(self):
        super().setUp()
 
    def tearDown(self):
        super().tearDown()
    
    def testScrollPosition0(self):
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 10
        subject.addChild(c0) 
       
        """test Widget.scrollPosition0"""
        assert subject.scrollPosition == (0,0), "Widget.scrollPosition not set correctly."

    def testScrollPosition1(self):
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 100
        c0.y = 100
        subject.addChild(c0) 
       
        """test Widget.scrollPosition0"""
        assert subject.scrollPosition == (0,0), "Widget.scrollPosition not set correctly."

    def testScrollWidth0(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.scrollSize0"""
        value = subject.scrollWidth
        assert value == 100, "Widget.scrollWidth({}) not set correctly.".format(value)

    def testScrollWidth1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 110
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
        value = subject.scrollWidth
        """test Widget.scrollWidth"""
        assert value == 120, "Widget.scrollWidth({}) not set correctly.".format(value)

    def testScrollHeight0(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.scrollSize0"""
        value = subject.scrollHeight
        assert value == 100, "Widget.scrollHeight({}) not set correctly.".format(value)

    def testScrollHeight1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 110
        subject.addChild(c0) 
       
        biui.main()
        value = subject.scrollHeight
        """test Widget.scrollHeight"""
        assert value == 120, "Widget.scrollHeight({}) not set correctly.".format(value)
        
    def testScrollSize0(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.scrollSize0"""
        assert subject.scrollSize == (100,100), "Widget.scrollSize({}) not set correctly.".format(subject.scrollSize)

    def testScrollSize1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 110
        c0.y = 120
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.scrollSize0"""
        assert subject.scrollSize == (120,130), "Widget.scrollSize({}) not set correctly.".format(subject.scrollSize)

    def testMaxScrollX0(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.maxScrollPosition"""
        value = subject.maxScrollX
        assert value == 0, "Widget.maxScrollX({}) not set correctly.".format(value)
        
    def testMaxScrollX1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 110
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.maxScrollPosition"""
        value = subject.maxScrollX
        assert value == 20, "Widget.maxScrollX({}) not set correctly.".format(value)
       
    def testMaxScrollY0(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 10
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.maxScrollY"""
        value = subject.maxScrollY
        assert value == 0, "Widget.maxScrollY({}) not set correctly.".format(value)
        
    def testMaxScrollY1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 10
        c0.y = 110
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.maxScrollY"""
        value = subject.maxScrollY
        assert value == 20, "Widget.maxScrollY({}) not set correctly.".format(value)
        
    def testMaxScrollPosition(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.width = 100
        subject.height = 100
        wnd.addChild(subject)
        
        c0 = Widget()
        c0.width = 10
        c0.height = 10
        c0.x = 110
        c0.y = 120
        subject.addChild(c0) 
       
        biui.main()
       
        """test Widget.maxScrollPosition"""
        value = subject.maxScrollPosition
        assert value == (20,30), "Widget.scrollSize({}) not set correctly.".format(value)


"""
tooltip
label
minValue
maxValue
value
step
microStep
showNavigation
allowManualInput
"""

if __name__ == "__main__":
    unittest.main() ## run all tests