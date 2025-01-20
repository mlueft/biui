import unittest
import os

import biui
from biui.Widgets import Window, Widget, ButtonGroup
from .ContainerWidgetTestCase import ContainerWidgetTestCase

class ButtonGroupTestCase(ContainerWidgetTestCase):
    
    def createSubject(self,type="ButtonGroup"):
        if type == "ButtonGroup":
            return ButtonGroup()
        return super().createSubject(type)
    
    def setUp(self):
        super().setUp()
 
    def tearDown(self):
        super().tearDown()

if __name__ == "__main__":
    unittest.main() ## run all tests