import unittest
import os

import biui
from biui.Widgets import Window, Widget, ButtonGroup, Pane
from .ContainerWidgetTestCase import ContainerWidgetTestCase

class PaneTestCase(ContainerWidgetTestCase):
    
    def createSubject(self,type="Pane"):
        if type == "Pane":
            return Pane()
        return super().createSubject(type)
    
    def setUp(self):
        super().setUp()
 
    def tearDown(self):
        super().tearDown()

"""
    onScrollSizeChanged
    connectScrollNavigator
    disconnectScrollNavigator
    verticalScrollbar
    horizontalScrollbar
"""

if __name__ == "__main__":
    unittest.main() ## run all tests