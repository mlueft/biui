import unittest
import biui
from biui.Widgets import Window
import os

class WindowTestCase(unittest.TestCase):
    
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
        assert 1==1, ""
    

    def _testX(self):
        subject = Window(1024,768)
        value = 72
        subject.x = value
        """test Window.x"""
        assert subject.x == value, "Window.x not set correctly."
                
    def _testY(self):
        subject = Window(1024,768)
        value = 75
        subject.y = value
        """test Window.y"""
        assert subject.y == value, "Window.y not set correctly."
        
    def testWidth(self):
        subject = Window(1024,768)
        value = 54
        subject.width = value
        """test Window.width"""
        assert subject.width == value, "Window.width not set correctly."
        
    def testHeight(self):
        subject = Window(1024,768)
        value = 34
        subject.height = value
        """test Window.height"""
        assert subject.height == value, "Window.height not set correctly."
    
    def testTitle(self):
        subject = Window(1024,768)
        value = "Window title!"
        subject.title = value
        """test Window.title"""
        assert subject.title == value, "Window.title not set correctly."
        
    def testRight(self):
        subject = Window(1024,768)
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.right = 400
        """test Window.right"""
        assert subject.x == 100, "Window.right not set correctly."
        assert subject.width == 300, "Window.right not set correctly."
        assert subject.y == 100, "Window.right not set correctly."
        assert subject.height == 200, "Window.right not set correctly."
            
    def _testLeft(self):
        subject = Window(1024,768)
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.left = 50
        """test Window.left"""
        assert subject.x == 50, "Window.left not set correctly."
        assert subject.width == 250, "Window.left not set correctly."
        assert subject.y == 100, "Window.left not set correctly."
        assert subject.height == 200, "Window.left not set correctly."
                    
    def _testTop(self):
        
        ##dMode = sdl2.SDL_DisplayMode()
        ##if sdl2.SDL_GetDesktopDisplayMode(0,dMode) != 0:
        ##    print( SDL_GetError() )
            
        ##print( dMode.w,dMode.h)
                
        subject = Window(1024,768)
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.top = 50
        """test Window.top"""
        assert subject.x == 100, "Window.top not set correctly."
        assert subject.width == 200, "Window.top not set correctly."
        assert subject.y == 50, "Window.top not set correctly."
        assert subject.height == 250, "Window.top not set correctly."
        
    def testBottom(self):
        subject = Window(1024,768)
        subject.x = 100
        subject.y = 100
        subject.width = 200
        subject.height = 200
        subject.bottom = 250
        """test Window.bottom"""
        assert subject.x == 100, "Window.bottom not set correctly."
        assert subject.width == 200, "Window.bottom not set correctly."
        assert subject.y == 100, "Window.bottom not set correctly."
        assert subject.height == 150, "Window.bottom not set correctly."

        
    def testGetChildAt(self):
        assert 1==1, ""
    
if __name__ == "__main__":
    unittest.main() ## run all tests
    
    
    
    