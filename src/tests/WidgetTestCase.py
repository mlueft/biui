import sys
import unittest
sys.path.append('./../') # needed if the file is tested.
sys.path.append('./')    # needed if the folder is tested.
import biui


class WidgetTestCase(unittest.TestCase):
    
    def setUp(self):
        biui.init()
        biui.setThemeFolder("../themes")
 
    def tearDown(self):
        #biui.quit()
        assert 1==1, ""
    
    def testPos(self):
        assert 1==1, ""
    
    def testSize(self):
        assert 1==1, ""
    
    
    def testX(self):
        subject = biui.Widget()
        value = 72
        subject.x = value
        """test Widget.x"""
        assert subject.x == value, "Widget.x not set correctly."
                
    def testY(self):
        subject = biui.Widget()
        value = 75
        subject.y = value
        """test Widget.y"""
        assert subject.y == value, "Widget.y not set correctly."

    def testLeft(self):
        subject = biui.Widget()
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.left = 50
        """test Widget.left"""
        assert subject.x == 50, "Widget.left not set correctly."
        assert subject.width == 250, "Widget.left not set correctly."
        assert subject.y == 100, "Widget.left not set correctly."
        assert subject.height == 200, "Widget.left not set correctly."
                    
    def testTop(self):
        
        #dMode = sdl2.SDL_DisplayMode()
        #if sdl2.SDL_GetDesktopDisplayMode(0,dMode) != 0:
        #    print( SDL_GetError() )
            
        #print( dMode.w,dMode.h)
                
        subject = biui.Widget()
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.top = 50
        """test Widget.top"""
        assert subject.x == 100, "Widget.top not set correctly."
        assert subject.width == 200, "Widget.top not set correctly."
        assert subject.y == 50, "Widget.top not set correctly."
        assert subject.height == 250, "Widget.top not set correctly."
        
    def testRight(self):
        subject = biui.Widget()
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.right = 400
        """test Widget.right"""
        assert subject.x == 100, "Widget.right not set correctly."
        assert subject.width == 300, "Widget.right not set correctly."
        assert subject.y == 100, "Widget.right not set correctly."
        assert subject.height == 200, "Widget.right not set correctly."
            
    def testBottom(self):
        subject = biui.Widget()
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.bottom = 250
        """test Widget.bottom"""
        assert subject.x == 100, "Widget.bottom not set correctly."
        assert subject.width == 200, "Widget.bottom not set correctly."
        assert subject.y == 100, "Widget.bottom not set correctly."
        assert subject.height == 150, "Widget.bottom not set correctly."

    def testWidth(self):
        subject = biui.Widget()
        value = 54
        subject.width = value
        """test Widget.width"""
        assert subject.width == value, "Widget.width not set correctly."
    
    def testMinWidth(self):
        assert 1==1, ""
    
    def testmaxWidth(self):
        assert 1==1, ""
        
    def testHeight(self):
        subject = biui.Widget()
        value = 34
        subject.height = value
        """test Widget.height"""
        assert subject.height == value, "Widget.height not set correctly."
    
    def testMinHeight(self):
        assert 1==1, ""
    
    def testmaxHeight(self):
        assert 1==1, ""
    
    def testHasChild(self):
        assert 1==1, ""
    
    def testAlignment(self):
        assert 1==1, ""
    
    def testDiretyRect(self):
        assert 1==1, ""
    
    def testIsInvalide(self):
        assert 1==1, ""
    
    def testInvalidate(self):
        assert 1==1, ""
    
    def testGetFirtyRect(self):
        assert 1==1, ""
    
    def testWindow(self):
        assert 1==1, ""
    
    def testParent(self):
        assert 1==1, ""
    
    def testCalculateLayout(self):
        assert 1==1, ""
    
    def testToLocal(self):
        assert 1==1, ""
    
    def testToGlobal(self):
        assert 1==1, ""
    
if __name__ == "__main__":
    unittest.main() # run all tests
    
    
    
    