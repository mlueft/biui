import os
import unittest
import biui
from biui.Widgets import Widget
from biui.Enum import Alignment

class WidgetTestCase(unittest.TestCase):
    
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
    
    def testPos(self):
        subject = Widget()
        valueX = 72
        valueY = 100
        subject.x = valueX
        subject.y = valueY
        """test Widget.pos"""
        assert subject.position == (valueX, valueY), "Widget.position not set correctly."
        
    def testSize(self):
        subject = Widget()
        valueW = 72
        valueH = 100
        subject.width = valueW
        subject.height = valueH
        """test Widget.pos"""
        assert subject.size == (valueW, valueH), "Widget.size not set correctly."
    
    def testX(self):
        subject = Widget()
        value = 72
        subject.x = value
        """test Widget.x"""
        assert subject.x == value, "Widget.x not set correctly."
                
    def testY(self):
        subject = Widget()
        value = 75
        subject.y = value
        """test Widget.y"""
        assert subject.y == value, "Widget.y not set correctly."

    def testLeft(self):
        subject = Widget()
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
        
        ##dMode = sdl2.SDL_DisplayMode()
        ##if sdl2.SDL_GetDesktopDisplayMode(0,dMode) != 0:
        ##    print( SDL_GetError() )
            
        ##print( dMode.w,dMode.h)
                
        subject = Widget()
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
        subject = Widget()
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
        subject = Widget()
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
        subject = Widget()
        value = 54
        subject.width = value
        """test Widget.width"""
        assert subject.width == value, "Widget.width not set correctly."
    
    def testMinWidth0(self):
        subject = Widget()
        subject.minWidth = 50
        """test Widget.minWidth"""
        assert subject.minWidth == 50, "Widget.minWidth not set correctly."

    def testMinWidth1(self):
        subject = Widget()
        subject.width = 50
        subject.minWidth = 100
        """test Widget.minWidth"""
        assert subject.width == 100, "Widget.width not corrected."
    
    def testmaxWidth0(self):
        subject = Widget()
        subject.maxWidth = 50
        """test Widget.maxWidth"""
        assert subject.maxWidth == 50, "Widget.maxWidth not set correctly."
        
    def testmaxWidth1(self):
        subject = Widget()
        subject.width = 150
        subject.maxWidth = 50
        """test Widget.maxWidth"""
        assert subject.width == 50, "Widget.width not corrected."
        
    def testHeight(self):
        subject = Widget()
        value = 34
        subject.height = value
        """test Widget.height"""
        assert subject.height == value, "Widget.height not set correctly."
    
    def testMinHeight0(self):
        subject = Widget()
        subject.minHeight = 50
        """test Widget.minHeight"""
        assert subject.minHeight == 50, "Widget.minHeight not set correctly."

    def testMinHeight1(self):
        subject = Widget()
        subject.height = 50
        subject.minHeight = 150
        """test Widget.minHeight"""
        assert subject.height == 150, "Widget.height not corrected."
            
    def testmaxHeight0(self):
        subject = Widget()
        subject.maxHeight = 50
        """test Widget.maxHeight"""
        assert subject.maxHeight == 50, "Widget.maxHeight not set correctly."

    def testmaxHeight1(self):
        subject = Widget()
        subject.height=150
        subject.maxHeight = 50
        """test Widget.maxHeight"""
        assert subject.height == 50, "Widget.height not corrected."
    
    def testHasChild(self):
        assert 1==1, ""
    
    def testAlignment(self):
        subject = Widget()
        subject.alignment = Alignment.FILL
        """test Widget.alignment"""
        assert subject.alignment == Alignment.FILL, "Widget.alignment not set correctly."
    
    def testDiretyRect(self):
        assert 1==1, ""
    
    def testIsInvalide(self):
        assert 1==1, ""
    
    def testInvalidate(self):
        assert 1==1, ""
    
    def testGetDirtyRect(self):
        assert 1==1, ""
    
    def testWindow(self):
        assert 1==1, ""
    
    def testParent(self):
        assert 1==1, ""
    
    def testCalculateLayout(self):
        assert 1==1, ""

    def testRenderRect(self):
        """test Widget.renderRect"""
        assert 1==1, ""
        
    def testToLocal0(self):
        subject = Widget()
        subject.x=150
        subject.y=50
        """test Widget.toLocal"""
        assert subject.toLocal((160,60)) == (10,10), "Widget.toLocal not calculated correctly."
    
    def testToGlobal0(self):
        subject = Widget()
        subject.x=150
        subject.y=50
        """test Widget.toGlobal"""
        assert subject.toGlobal((10,10)) == (160,60), "Widget.toGlobal not calculated correctly."
    
    def testFocus(self):
        """test Widget.focus"""
        assert 1==1, ""
            
    """
    backColor
    borderColor
    tooltip
    name
    onTextInput
    onKeyUp
    onKeyDown
    onMouseMove
    onMouseLeave
    onMouseEnter
    onMouseWheel
    onMouseUp
    onMouseDown
    onMouseClick
    onBeforeDraw
    onAfterDraw
    onFocus
    onFocusLost
    onShortcut
    onResized
    onGotAdded
    onGotRemoved
    """
    
if __name__ == "__main__":
    unittest.main() ## run all tests
    
    
    
    