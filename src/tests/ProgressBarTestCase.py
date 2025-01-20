import os
import unittest
import biui
from biui.Widgets import Widget,Progressbar, ContainerWidget, Button, ButtonGroup, Window, Pane
from biui.Enum import Alignment

from .ContainerWidgetTestCase import ContainerWidgetTestCase

class ProgressBarTestCase(ContainerWidgetTestCase):
    
    def createSubject(self,type="Progressbar"):
        if type == "Progressbar":
            return Progressbar()
        super().createSubject(type)
    
    def setUp(self):
        biui.init()
        biui.setThemeFolder(
            os.path.abspath(
                os.path.join(os.getcwd(),"./themes")
            )
        )
    
        biui.selectTheme("blocks")
 
    def tearDown(self):
        ## biui.quit()
        pass

    def testValue0(self):
        subject = self.createSubject()
        subject.value = 5
        """test Progressbar.value"""
        value = subject.value
        assert value == 5, "Progressbar.value({}) not set correctly.".format(value)
            
    def testMinValue0(self):
        subject = self.createSubject()
        subject.minValue = 10
        subject.value = 5
        """test Progressbar.minValue"""
        value = subject.value
        assert value == 10, "Progressbar.minValue({}) not set correctly.".format(value)

    def testMinValue1(self):
        subject = self.createSubject()
        subject.minValue = 10
        subject.value = 10
        """test Progressbar.minValue"""
        value = subject.value
        assert value == 10, "Progressbar.minValue({}) not set correctly.".format(value)

    def testMinValue2(self):
        subject = self.createSubject()
        subject.minValue = 10
        subject.value = 11
        """test Progressbar.minValue"""
        value = subject.value
        assert value == 11, "Progressbar.minValue({}) not set correctly.".format(value)

    def testMaxValue0(self):
        subject = self.createSubject()
        subject.maxValue = 10
        subject.value = 11
        """test Progressbar.maxValue"""
        value = subject.value
        assert value == 10, "Progressbar.maxValue({}) not set correctly.".format(value)

    def testMaxValue1(self):
        subject = self.createSubject()
        subject.maxValue = 10
        subject.value = 10
        """test Progressbar.maxValue"""
        value = subject.value
        assert value == 10, "Progressbar.maxValue({}) not set correctly.".format(value)

    def testMaxValue2(self):
        subject = self.createSubject()
        subject.maxValue = 10
        subject.value = 9
        """test Progressbar.maxValue"""
        value = subject.value
        assert value == 9, "Progressbar.maxValue({}) not set correctly.".format(value)
             
    def testGetChildAt0(self):
        wnd = Window()
        
        subject = self.createSubject()
        subject.x = 100
        subject.y = 100
        subject.width  = 100
        subject.height = 100
        wnd.addChild(subject)
         
        """test Progressbar.getChildAt"""
        value = subject.getChildAt((101,101))
        assert value == subject, "Progressbar.getChildAt({}) not set correctly.".format(value)
        
    def testGetChildAt1(self):
        wnd = Window(1024,768)
        
        subject = self.createSubject()
        subject.x = 100
        subject.y = 100
        subject.width = 150
        subject.height = 150
        wnd.addChild(subject)
        
        c0 = self.createSubject()
        c0.x = 10
        c0.y = 10
        c0.width = 100
        c0.height = 100
        subject.addChild(c0) 
        
        """test Widget.removeChildren"""
        value = subject.getChildAt((121,121))
        assert value == subject, "Widget.getChildAt({}) not set correctly.".format(value)
        
    def testChildren0(self):
        subject = self.createSubject()
        c0 = Widget()
        c1 = Widget()
        subject.addChild(c0) 
        subject.addChild(c1)
        """test Progress.children"""
        assert subject.children == [], "Progressbar.children not set correctly."

    def testRemoveChild0(self):
        subject = self.createSubject()
        c0 = Widget()
        c1 = Widget()
        subject.addChild(c0) 
        subject.addChild(c1)
        subject.removeChild(c0)
        """test Widget.removeChildren"""
        assert subject.children == [], "Widget.removechildren not set correctly."

    def testHasChild(self):
        subject = self.createSubject()
        c0 = Widget()
        subject.addChild(c0) 
        """test Progressbar.hasChildren"""
        assert subject.hasChild(c0) == False, "Progressbar.hasChildren not set correctly."

"""
showValue
label
getChildAt

"""

if __name__ == "__main__":
    unittest.main() ## run all tests