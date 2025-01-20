import os
import unittest
import biui
from biui.Widgets import Widget,NumberSlider, ContainerWidget, Button, ButtonGroup, Window, Pane
from biui.Enum import Alignment

from .ProgressBarTestCase import ProgressBarTestCase

class NumberSliderTestCase(ProgressBarTestCase):
    
    def createSubject(self,type="NumberSlider"):
        if type == "NumberSlider":
            return NumberSlider()
        super().createSubject(type)
    
    def testChildren0(self):
        pass

    def testGetChildAt0(self):
        pass
        
    def testGetChildAt1(self):
        pass
        
    def testRemoveChild0(self):
        pass

    def testRemoveChild1(self):
        pass
    
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