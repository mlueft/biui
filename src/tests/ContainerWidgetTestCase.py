import unittest
import os

import biui

class ContainerWidgetTestCase(unittest.TestCase):
    
    def setUp(self):
        biui.init()
        biui.setThemeFolder(
            os.path.abspath(
                os.path.join(os.getcwd(),"./themes")
            )
        )
        
        biui.selectTheme("blocks")
 
    def tearDown(self):
        ##biui.quit()
        pass
    
    def testChildren(self):
        assert 1==1, ""

    def testHasChild(self):
        assert 1==1, ""
    
    def testRemoveChild(self):
        assert 1==1, ""
    
    def testAddChild(self):
        assert 1==1, ""
    
    def testGetChildAt(self):
        assert 1==1, ""
    
    def testIsInvalide(self):
        assert 1==1, ""
    
    def testLayoutManager(self):
        assert 1==1, ""

    def testGetDirtyRectAngle(self):
        assert 1==1, ""
    
    def testCalculateLayout(self):
        assert 1==1, ""
    
    def testInvalidate(self):
        assert 1==1, ""
    
    """ "
    connectScrollNavigator
    disconnectScrollNavigator
    scrollPosition
    maxScrollPosition
    maxScrollX
    maxScrollY
    scrollX
    scrollY
    renderRect
    toLocal
    toGlobal
    onChildAdded
    onChildRemoved
    onScrollPositionChanged
    """ #"
if __name__ == "__main__":
    unittest.main() ## run all tests