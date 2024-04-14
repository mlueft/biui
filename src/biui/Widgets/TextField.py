#include "biui.inc"
from biui.Enum import ShortCuts

import biui
from biui.Widgets import Widget
from biui.Enum.Keys import Keys
from biui.Enum.KeyModifiers import KeyModifiers
from biui.Enum.EditingMode import EditingMode

class TextField(Widget):
    
    def __init__(self):
        super().__init__()
        
        theme = biui.getTheme()
        self._themeBackgroundfunction = theme.drawTextFieldBeforeChildren
        
        self.onKeyDown.add(self.__hndKeyDown)
        self.onKeyDown.add(self.__hndKeyUp)
        self.onFocus.add(self.__hndFocus)
        self.onFocusLost.add(self.__hndFocusLost)
        
        self.color = biui.Color(50,50,50,255)
        self._font = None
        self.font = biui.Font()
        self.font.size = 18
        ##
        self.name = "textfield"
        ##
        self.__dataComponent = biui.TextDataEditComponent()
        self.__dataComponent.onDataChanged.add(self.__hndDataChanged)
        self.__dataComponent.onCursorpositionChanged.add(self.__hndCursorpositionChanged)
        self.__dataComponent.onSelectionChanged.add(self.__hndSelectionChanged)
        self.__cursorVisible = False
        self.__cursorTimer = biui.Timer(1000,self.__cursorCallBack)
        self.__cursorTimer.active = False
        self.__selectionBox = None
        self.onShortcut.add(self.__hndShortcut)
        
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
    
    ###
    ##
    ##
    @property
    def editingMode(self):
        return self.__dataComponent.editingMode
    
    ###
    ##
    ##
    @editingMode.setter
    def editingMode(self,value):
        self.__dataComponent.editingMode = value
            
    @property
    def dataComponent(self):
        return self.__dataComponent
    
    ###
    ##
    ##
    @dataComponent.setter
    def dataComponent(self,value):
        
        if value == None:
            return
        
        if value == self.__dataComponent:
            return
        
        if self.__dataComponent != None:
            self.__dataComponent.onDataChanged.remove(self.__hndDataChanged)
            self.__dataComponent.onCursorpositionChanged.remove(self.__hndCursorpositionChanged)
            self.__dataComponent.onSelectionChanged.remove(self.__hndSelectionChanged)
        
        self.__dataComponent = value
        self.__dataComponent.onDataChanged.add(self.__hndDataChanged)
        self.__dataComponent.onCursorpositionChanged.add(self.__hndCursorpositionChanged)
        self.__dataComponent.onSelectionChanged.add(self.__hndSelectionChanged)
        
        self._invalidate()
    
    ### returns the graphical dimension of the cursor.
    ##
    ##
    @property
    def cursor(self):
        
        if not self.cursorVisible:
            return None

        ## calculate graphical cursorposition
        text = self.__dataComponent.data[0:self.__dataComponent.cursorPosition]
        size = self.font.getRenderSize(text)
        cp = size[0]
    
        ## Cursor for insert mode
        if self.dataComponent.editingMode == EditingMode.INSERT:
            return (cp,3,2,self.height-6)

        ## Cursor for replace mode
        
        ## Calculate cursor width
        ## "a" is representative for a single
        ## character
        size = self.font.getRenderSize("a")
        cp1 = size[0]
        
        return (cp,self.height-4,cp1,2)
    
    ### Return the graphical dimensions of the selection box.
    ##
    ##
    @property
    def selectionBox(self):
        if self.__selectionBox == None:
            sb = self.__dataComponent.selectionBox
            
            if sb == None:
                self.__selectionBox = None
                self._invalidate()
                return
            
            text = self.__dataComponent.data[0:sb[0][0]]
            x0 = self.font.getRenderSize(text)
            
            text = self.__dataComponent.data[0:sb[1][0]]
            x1 = self.font.getRenderSize(text)
            
            self.__selectionBox = (
                x0[0],2,x1[0]-x0[0],self.height-4
            )
        
        return self.__selectionBox
    
    ### Returns the graphical cursor position
    ##
    ##
    
    ###
    ##
    ##
    @property
    def cursorVisible(self):
        return self.__cursorVisible 
    
    def __hndKeyDown(self,ev):
        ##print("TextField::__hndKeyDown")
        self.__cursorVisible = True
        self._invalidate()
        pass
    
    def __hndKeyUp(self,ev):
        ##print("TextField::__hndKeyUp: {}".format(ev.keyCode) )
        
        sc = biui.ShortcutControl
        text = sc.getText(ev)

        if text != None:
            self.__dataComponent.insert(text)
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_BACKSPACE:
            self.__dataComponent.delete()
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_DELETE:
            self.__dataComponent.remove()
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_HOME:
            if ev.modifiers & KeyModifiers.SHIFT:
                self.__dataComponent.extendSelection(-999999999)
            else:
                self.__dataComponent.cursorPosition = 0;
            ev.stopPropagation()
            
        elif ev.keyCode == Keys.K_END:
            if ev.modifiers & KeyModifiers.SHIFT:
                self.__dataComponent.extendSelection(999999999)
            else:            
                self.__dataComponent.cursorPosition = len(self.__dataComponent.data);
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
            if ev.modifiers & KeyModifiers.SHIFT:
                self.__dataComponent.extendSelection(-1)
            elif False == biui.ShortcutControl.isShortcutAny(ev):
                self.__dataComponent.moveCursor(-1,0) 
            ev.stopPropagation()
        
        elif ev.keyCode == Keys.K_RIGHT:
            
            if ev.modifiers & KeyModifiers.SHIFT:
                self.__dataComponent.extendSelection(1)
            elif False == biui.ShortcutControl.isShortcutAny(ev):
                self.__dataComponent.moveCursor(1,0)
            ev.stopPropagation()

        elif ev.keyCode == Keys.K_INSERT:
            print("a")
            if self.editingMode == EditingMode.INSERT:
                self.editingMode = EditingMode.REPLACE
            else:
                self.editingMode = EditingMode.INSERT
        
        ##else:
        ##    print("Keyboard input not processed")

            
    def __hndDataChanged(self,ev):
        self._invalidate()
    
    def __hndCursorpositionChanged(self,ev):
        ##print("TextField::__hndCursorpositionChanged")
        self._invalidate()
        
    def __hndSelectionChanged(self,ev):
        self.__selectionBox = None
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
        return self.__dataComponent.data
    
    ###  Sets the shown text.
    ##
    ##   @param value   The text that should be shown.
    ##   
    @value.setter
    def value(self,value):
        self.__dataComponent.data = value
        
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
        
    def _invalidate(self):
        super()._invalidate()
        ##self.__selectionBox = None
        
    ###
    ##
    ##
    def __hndShortcut(self,ev):
        
        if ev.type == ShortCuts.SELECT_ALL:
            self.__dataComponent.selectAll()
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.COPY:
            
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.PASTE:
            data = biui.Clipboard.get()
            self.__dataComponent.insert(data)
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.CUT:
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.MOVE_SELECTION_UP:
            self.__dataComponent.moveSelection(0,-1)
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.MOVE_SELECTION_DOWN:
            self.__dataComponent.moveSelection(0,1)
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.MOVE_SELECTION_LEFT:
            self.__dataComponent.moveSelection(-1,0)
            ev.stopPropagation()
        
        elif ev.type == ShortCuts.MOVE_SELECTION_RIGHT:
            self.__dataComponent.moveSelection(1,0)
            ev.stopPropagation()
            
        else:
            
            print("shortcut not processed")
        
                
        