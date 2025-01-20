import os
import unittest
import biui
from biui.Widgets import Widget, ContainerWidget, Button, ButtonGroup, Window, Pane
from biui.Enum import Alignment

class WidgetTestCase(unittest.TestCase):
    
    def createSubject(self,type="Widget"):
        if type == "Widget":
            return Widget()
        if type == "Button":
            return Button()
        if type == "Window":
            return Button()
    
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
        subject = self.createSubject()
        valueX = 72
        valueY = 100
        subject.x = valueX
        subject.y = valueY
        """test Widget.pos"""
        value = subject.position
        assert value == (valueX, valueY), "Widget.position({}) not set correctly.".format(value)
        
    def testSize(self):
        subject = self.createSubject()
        valueW = 72
        valueH = 100
        subject.width = valueW
        subject.height = valueH
        """test Widget.pos"""
        assert subject.size == (valueW, valueH), "Widget.size not set correctly."
    
    def testX(self):
        subject = self.createSubject()
        value = 72
        subject.x = value
        """test Widget.x"""
        assert subject.x == value, "Widget.x not set correctly."
                
    def testY(self):
        subject = self.createSubject()
        value = 75
        subject.y = value
        """test Widget.y"""
        assert subject.y == value, "Widget.y not set correctly."

    def testLeft(self):
        subject = self.createSubject()
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
                
        subject = self.createSubject()
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
        subject = self.createSubject()
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
        subject = self.createSubject()
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
        subject = self.createSubject()
        value = 54
        subject.width = value
        """test Widget.width"""
        assert subject.width == value, "Widget.width not set correctly."
    
    def testMinWidth0(self):
        subject = self.createSubject()
        subject.minWidth = 50
        """test Widget.minWidth"""
        assert subject.minWidth == 50, "Widget.minWidth not set correctly."

    def testMinWidth1(self):
        subject = self.createSubject()
        subject.width = 50
        subject.minWidth = 100
        """test Widget.minWidth"""
        assert subject.width == 100, "Widget.width not corrected."
    
    def testmaxWidth0(self):
        subject = self.createSubject()
        subject.maxWidth = 50
        """test Widget.maxWidth"""
        assert subject.maxWidth == 50, "Widget.maxWidth not set correctly."
        
    def testmaxWidth1(self):
        subject = self.createSubject()
        subject.width = 150
        subject.maxWidth = 50
        """test Widget.maxWidth"""
        assert subject.width == 50, "Widget.width not corrected."
        
    def testHeight(self):
        subject = self.createSubject()
        value = 34
        subject.height = value
        """test Widget.height"""
        assert subject.height == value, "Widget.height not set correctly."
    
    def testMinHeight0(self):
        subject = self.createSubject()
        subject.minHeight = 50
        """test Widget.minHeight"""
        assert subject.minHeight == 50, "Widget.minHeight not set correctly."

    def testMinHeight1(self):
        subject = self.createSubject()
        subject.height = 50
        subject.minHeight = 150
        """test Widget.minHeight"""
        assert subject.height == 150, "Widget.height not corrected."
            
    def testmaxHeight0(self):
        subject = self.createSubject()
        subject.maxHeight = 50
        """test Widget.maxHeight"""
        assert subject.maxHeight == 50, "Widget.maxHeight not set correctly."

    def testmaxHeight1(self):
        subject = self.createSubject()
        subject.height=150
        subject.maxHeight = 50
        """test Widget.maxHeight"""
        assert subject.height == 50, "Widget.height not corrected."
    
    def testHasChild0(self):
        subject = self.createSubject()
        """test Widget.hasChild"""
        assert subject.hasChild(subject) == True, "Widget.hasChild() not corrected."
    
    def testHasChild1(self):
        subject = self.createSubject()
        """test Widget.hasChild"""
        assert subject.hasChild(self.createSubject()) == False, "Widget.hasChild() not corrected."
        
    def testAlignment(self):
        subject = self.createSubject()
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
    
    def testWindow0(self):
        subject = self.createSubject()
        """test Widget.window"""
        assert subject.window == None, "Widget.window not set correctly."
    
    def testWindow1(self):
        
        wnd = Window(1025,768)
        subject = self.createSubject()
        wnd.addChild(subject)
        """test Widget.window"""
        assert subject.window == wnd, "Widget.window not set correctly."

    def testWindow2(self):
        wnd0 = Window(1025,768)
        wnd1 = Window(1025,768)
        subject = self.createSubject()
        wnd0.addChild(subject)
        wnd1.addChild(subject)
        """test Widget.window"""
        assert subject.window == wnd1, "Widget.window not set correctly."
                
    def testParent0(self):
        subject = self.createSubject()
        """test Widget.parent"""
        assert subject.parent == None, "Widget.parent not set correctly."
    
    def testParent1(self):
        wnd = Window(1025,768)
        subject = self.createSubject()
        wnd.addChild(subject)
        """test Widget.parent"""
        assert subject.parent == wnd, "Widget.parent not set correctly."

    def testParent2(self):
        wnd0 = Window(1025,768)
        wnd1 = Window(1025,768)
        subject = self.createSubject()
        wnd0.addChild(subject)
        wnd1.addChild(subject)
        """test Widget.parent"""
        assert subject.parent == wnd1, "Widget.parent not set correctly."
                
    def testCalculateLayout(self):
        assert 1==1, ""

    def testRenderRect(self):
        """test Widget.renderRect"""
        assert 1==1, ""
        
    def testToLocal0(self):
        subject = self.createSubject()
        subject.x=150
        subject.y=50
        """test Widget.toLocal"""
        assert subject.toLocal((160,60)) == (10,10), "Widget.toLocal not calculated correctly."
    
    def testToGlobal0(self):
        subject = self.createSubject()
        subject.x=150
        subject.y=50
        """test Widget.toGlobal"""
        assert subject.toGlobal((10,10)) == (160,60), "Widget.toGlobal not calculated correctly."
    
    def testFocus(self):
        """test Widget.focus"""
        assert 1==1, ""
            
    """ "
    getChildAt
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
    onBeforeRender
    onAfterRender
    onFocus
    onFocusLost
    onShortcut
    onResized
    onGotAdded
    onGotRemoved
    """ #"
    
if __name__ == "__main__":
    unittest.main() ## run all tests
    
