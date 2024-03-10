#include "biui.inc"

import biui
from biui.Widgets import Widget
from biui.Enum.Keys import Keys

class TextField(Widget):
    
    def __init__(self):
        super().__init__()
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawTextFieldBeforeChildren
        
        self.onKeyDown.add(self.__hndKeyDown)
        self.onKeyDown.add(self.__hndKeyUp)
        self.onFocus.add(self.__hndFocus)
        self.onFocusLost.add(self.__hndFocusLost)
        
        self.color = biui.Color(200,200,200,255)
        self._font = None
        self.font = biui.Font()
        self.font.size = 18
        ##
        self.name = "textfield"
        ##
        self.__data = biui.TextDataEditComponent()
        self.__data.onDataChanged.add(self.__hndDataChanged)
        self.__data.onCursorpositionChanged.add(self.__hndCursorpositionChanged)
        self.__data.onSelectionChanged.add(self.__hndSelectionChanged)
        self.__cursorVisible = False
        self.__cursorTimer = biui.Timer(1000,self.__cursorCallBack)
        self.__cursorTimer.active = False
        
    def __hndFocus(self,ev):
        self.__cursorTimer.active = True
    
    def __hndFocusLost(self,ev):
        self.__cursorTimer.active = False
        self.__cursorVisible = False
        self._invalidate()
        
    def __cursorCallBack(self,ev):
        self.__cursorVisible = not self.__cursorVisible
        self._invalidate()
       
    ###
    ##
    ##
    def getCursorPosition(self):
        text = self.__data.data[0:self.__data.cursorPosition]
        size = self.font.getRenderSize(text)
        return size[0]
    ###
    ##
    ##
    @property
    def cursorVisible(self):
        return self.__cursorVisible 
    
    def __hndKeyDown(self,ev):
        ##print("TextField::__hndKeyDown")
        pass
    
    def __hndKeyUp(self,ev):
        ##print("TextField::__hndKeyUp")
        
        sc = biui.ShortcutControl
        text = sc.getText(ev)
        
        if text != None:
            self.__data.insert(text)
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_BACKSPACE:
            self.__data.delete()
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_DELETE:
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_HOME:
            self.__data.cursorPosition = 0;
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_END:
            self.__data.cursorPosition = len(self.__data.data);
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_PAGEUP:
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_PAGEDOWN:
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_UP:
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_DOWN:
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_LEFT:
            self.__data.cursorPosition = self.__data.cursorPosition - 1 
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_RIGHT:
            self.__data.cursorPosition = self.__data.cursorPosition + 1
            ev.stopPropagation()
        
        elif sc.isCopy(ev):
            ev.stopPropagation()
        
        elif sc.isPaste(ev):
            ev.stopPropagation()
        
        elif sc.isMoveSelectionLeft(ev):
            ev.stopPropagation()
        
        elif sc.isMoveSelectionRight(ev):
            ev.stopPropagation()
        
        elif sc.isMoveSelectionUp(ev):
            ev.stopPropagation()
        
        elif sc.isMoveSelectionDown(ev):
            ev.stopPropagation()
        
        else:
            print("Keyboard input not processed")
        
    def __hndDataChanged(self,ev):
        ##print("TextField::__hndDataChanged")
        self._invalidate()
    
    def __hndCursorpositionChanged(self,ev):
        print("TextField::__hndCursorpositionChanged")
        self._invalidate()
        
    def __hndSelectionChanged(self,ev):
        print("TextField::__hndSelectionChanged")
        self._invalidate()    
        
    ### Handles the font change of the font element.
    ##
    ##        
    def __hndFontOnSizeChanged(self,ev):
        self._invalidate()
                
    ### Set/Get the value of the label.
    ##  The value is the shown text.
    ##
    ##
    @property   
    def value(self):
        return self.__data.data
    
    ###  Sets the shown text.
    ##
    ##   @param value   The text that should be shown.
    ##   
    @value.setter
    def value(self,value):
        self.__data.data = value
        
    ### Set/Get the text color.
    ##
    ##  @return  The color orject.
    ##
    @property
    def color(self):
        return self._color
    
    ### Sets the color of the text.
    ##
    ##  @param value
    ##
    @color.setter
    def color(self,value):
        self._color = value
        self._invalidate()
    
    ### Set/Get the font object.
    ##
    ##  @return
    ##
    @property   
    def font(self):
        return self._font
        
    ### Sets the font object.
    ##
    ##  @param value 
    ##
    @font.setter
    def font(self,value):
        
        if not value.onSizeChanged.has(self.__hndFontOnSizeChanged):
            value.onSizeChanged.add(self.__hndFontOnSizeChanged)
            
        self._font = value
        self._invalidate()
        
                
        