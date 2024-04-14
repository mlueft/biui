from biui.Enum import Keys, KeyModifiers,ShortCuts
from biui.Events import EventManager,KeyEvent,ShortcutEvent

###
##
##
class ShortcutControl(object):
    
    ###
    ##
    ##
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ShortcutControl, cls).__new__(cls)
        return cls.instance
    
    ###
    ##
    ##
    def __init__(self):
        self.__shortcuts = {}
        
        self.addShortCut( ShortCuts.SELECT_ALL           , [ [KeyModifiers.CTRL,Keys.K_a] ])
        self.addShortCut( ShortCuts.COPY                 , [ [KeyModifiers.CTRL,Keys.K_c] ])
        self.addShortCut( ShortCuts.PASTE                , [ [KeyModifiers.CTRL,Keys.K_v] ])
        self.addShortCut( ShortCuts.CUT                  , [ [KeyModifiers.CTRL,Keys.K_x] ])
        self.addShortCut( ShortCuts.MOVE_SELECTION_UP    , [ [KeyModifiers.ALT,Keys.K_UP] ])
        self.addShortCut( ShortCuts.MOVE_SELECTION_DOWN  , [ [KeyModifiers.ALT,Keys.K_DOWN] ])
        self.addShortCut( ShortCuts.MOVE_SELECTION_LEFT  , [ [KeyModifiers.ALT,Keys.K_LEFT] ])
        self.addShortCut( ShortCuts.MOVE_SELECTION_RIGHT , [ [KeyModifiers.ALT,Keys.K_RIGHT] ])
        
        ##
        self.onShortcut:EventManager = EventManager()
    
    ### 
    ##
    ##
    def sdlOnKeyDown(self,event)->None:
        pass
        
    ### 
    ##
    ##
    def sdlOnKeyUp(self,event)->None:
        ##print("ShortCutControl::sdlOnKeyUp")
        ke = KeyEvent(
            self,
            event.key.keysym.sym,
            event.key.keysym.scancode,
            event.key.keysym.mod,
            event.key.repeat,
            event.key.timestamp
        )
        for k,v in self.__shortcuts.items():
            if self.isShortcut(ke, k):
                ev = ShortcutEvent(self,k,ke)
                self.onShortcut.provoke(ev)
        
        ##öäself._onKeyUp(ev)
        
    ###
    ##
    ##
    def getText(self,event):
        result = None
        
        if not event.modifiers & KeyModifiers.CTRL:
            if  not event.modifiers & KeyModifiers.ALT:
                if  not event.modifiers & KeyModifiers.META:
                    if  not event.modifiers & KeyModifiers.MODE:
                        if event.keyCode == Keys.K_a: result = "a"
                        elif event.keyCode == Keys.K_b: result = "b"
                        elif event.keyCode == Keys.K_c: result = "c"
                        elif event.keyCode == Keys.K_d: result = "d"
                        elif event.keyCode == Keys.K_e: result = "e"
                        elif event.keyCode == Keys.K_f: result = "f"
                        elif event.keyCode == Keys.K_g: result = "g"
                        elif event.keyCode == Keys.K_h: result = "h"
                        elif event.keyCode == Keys.K_i: result = "i"
                        elif event.keyCode == Keys.K_j: result = "j"
                        elif event.keyCode == Keys.K_k: result = "k"
                        elif event.keyCode == Keys.K_l: result = "l"
                        elif event.keyCode == Keys.K_m: result = "m"
                        elif event.keyCode == Keys.K_n: result = "n"
                        elif event.keyCode == Keys.K_o: result = "o"
                        elif event.keyCode == Keys.K_p: result = "p"
                        elif event.keyCode == Keys.K_q: result = "q"
                        elif event.keyCode == Keys.K_r: result = "r"
                        elif event.keyCode == Keys.K_s: result = "s"
                        elif event.keyCode == Keys.K_t: result = "t"
                        elif event.keyCode == Keys.K_u: result = "u"
                        elif event.keyCode == Keys.K_v: result = "v"
                        elif event.keyCode == Keys.K_w: result = "w"
                        elif event.keyCode == Keys.K_x: result = "x"
                        elif event.keyCode == Keys.K_y: result = "y"
                        elif event.keyCode == Keys.K_z: result = "z"
                        elif event.keyCode == Keys.K_KP_SPACE: result = " "        
                        elif event.keyCode == Keys.K_szlig: result = "ß"
                        elif event.keyCode == Keys.K_uuml: result = "ü"
                        elif event.keyCode == Keys.K_ouml: result = "ö"
                        elif event.keyCode == Keys.K_auml: result = "ä"
                        elif event.keyCode == Keys.K_0: result = "0"
                        elif event.keyCode == Keys.K_1: result = "1"
                        elif event.keyCode == Keys.K_2: result = "2"
                        elif event.keyCode == Keys.K_3: result = "3"
                        elif event.keyCode == Keys.K_4: result = "4"
                        elif event.keyCode == Keys.K_5: result = "5"
                        elif event.keyCode == Keys.K_6: result = "6"
                        elif event.keyCode == Keys.K_7: result = "7"
                        elif event.keyCode == Keys.K_8: result = "8"
                        elif event.keyCode == Keys.K_9: result = "9"
                        elif event.keyCode == Keys.K_ASTERISK: result = "*"
                        elif event.keyCode == Keys.K_PLUS: result = "+"
                        elif event.keyCode == Keys.K_COMMA: result = ","
                        elif event.keyCode == Keys.K_MINUS: result = "-"
                        elif event.keyCode == Keys.K_PERIOD: result = "."
                        elif event.keyCode == Keys.K_SLASH: result = "/"
                        elif event.keyCode == Keys.K_COLON: result = ":"
                        elif event.keyCode == Keys.K_SEMICOLON: result = ";"
                        elif event.keyCode == Keys.K_LESS: result = "<"
                        elif event.keyCode == Keys.K_GREATER: result = ">"
                        elif event.keyCode == Keys.K_KP_MULTIPLY: result = "*"
                        elif event.keyCode == Keys.K_KP_MINUS: result = "-"
                        elif event.keyCode == Keys.K_KP_PLUS: result = "+"
                        elif event.keyCode == Keys.K_KP_PERIOD: result = ","
                        elif event.keyCode == Keys.K_KP_COMMA: result = ","
                        elif event.keyCode == Keys.K_KP_LESS: result = "<"
                        elif event.keyCode == Keys.K_KP_GREATER: result = ">"
                        elif event.keyCode == Keys.K_SPACE: result = " "
                        elif event.keyCode == Keys.K_HASH: result = "#"
                        elif event.keyCode == Keys.K_DOLLAR: result = "$"
                        elif event.keyCode == Keys.K_PERCENT: result = "%"
                        elif event.keyCode == Keys.K_QUOTE: result = '"'
                        elif event.keyCode == Keys.K_LEFTPAREN: result = "("
                        elif event.keyCode == Keys.K_RIGHTPAREN: result = ")"
                        elif event.keyCode == Keys.K_EQUALS: result = "="
                        elif event.keyCode == Keys.K_QUESTION: result = "?"
                        elif event.keyCode == Keys.K_AT: result = "@"
                        elif event.keyCode == Keys.K_LEFTBRACKET: result = "["
                        elif event.keyCode == Keys.K_BACKSLASH: result = "\\"
                        elif event.keyCode == Keys.K_RIGHTBRACKET: result = "]"
                        elif event.keyCode == Keys.K_CARET: result = "^"
                        elif event.keyCode == Keys.K_UNDERSCORE: result = "_"
                        elif event.keyCode == Keys.K_KP_DIVIDE: result = "/"
                        elif event.keyCode == Keys.K_THOUSANDSSEPARATOR: result = "."
                        elif event.keyCode == Keys.K_DECIMALSEPARATOR: result = ","
                        elif event.keyCode == Keys.K_CURRENCYUNIT: result = "€"
                        elif event.keyCode == Keys.K_KP_LEFTPAREN: result = "("
                        elif event.keyCode == Keys.K_KP_RIGHTPAREN: result = ")"
                        elif event.keyCode == Keys.K_KP_LEFTBRACE: result = "{"
                        elif event.keyCode == Keys.K_KP_RIGHTBRACE: result = "}"
                        elif event.keyCode == Keys.K_KP_PERCENT: result = "%"
                        elif event.keyCode == Keys.K_KP_AMPERSAND: result = "&"
                        elif event.keyCode == Keys.K_KP_DBLAMPERSAND: result = "&&"
                        elif event.keyCode == Keys.K_KP_COLON: result = ":"
                        elif event.keyCode == Keys.K_KP_HASH: result = "#"
                        elif event.keyCode == Keys.K_KP_AT: result = "@"

        if event.modifiers & KeyModifiers.NUM:
            if event.keyCode == Keys.K_KP_1: result = "1"
            elif event.keyCode == Keys.K_KP_2: result = "2"
            elif event.keyCode == Keys.K_KP_3: result = "3"
            elif event.keyCode == Keys.K_KP_4: result = "4"
            elif event.keyCode == Keys.K_KP_5: result = "5"
            elif event.keyCode == Keys.K_KP_6: result = "6"
            elif event.keyCode == Keys.K_KP_7: result = "7"
            elif event.keyCode == Keys.K_KP_8: result = "8"
            elif event.keyCode == Keys.K_KP_9: result = "9"
            elif event.keyCode == Keys.K_KP_0: result = "0"
            
        if event.modifiers & KeyModifiers.SHIFT:
            if event.keyCode == Keys.K_1: result = "!"
            elif event.keyCode == Keys.K_2: result = "\""
            elif event.keyCode == Keys.K_3: result = "§"
            elif event.keyCode == Keys.K_4: result = "$"
            elif event.keyCode == Keys.K_5: result = "%"
            elif event.keyCode == Keys.K_6: result = "&"
            elif event.keyCode == Keys.K_7: result = "/"
            elif event.keyCode == Keys.K_8: result = "("
            elif event.keyCode == Keys.K_9: result = ")"
            elif event.keyCode == Keys.K_0: result = "="
            elif event.keyCode == Keys.K_szlig: result = "?"
            elif event.keyCode == Keys.K_PLUS: result = "*"
            elif event.keyCode == Keys.K_LESS: result = ">"
            elif event.keyCode == Keys.K_HASH: result = "'"
            elif result != None: result = result.upper()
            
        if event.modifiers & KeyModifiers.RALT:
            if event.keyCode == Keys.K_e: result = "€"
            elif event.keyCode == Keys.K_2: result = "²"
            elif event.keyCode == Keys.K_3: result = "³"
            elif event.keyCode == Keys.K_7: result = "{"
            elif event.keyCode == Keys.K_8: result = "["
            elif event.keyCode == Keys.K_9: result = "]"
            elif event.keyCode == Keys.K_0: result = "}"
            elif event.keyCode == Keys.K_szlig: result = "\\"
            elif event.keyCode == Keys.K_LESS: result = "|"
            elif event.keyCode == Keys.K_m: result = "µ"
            elif event.keyCode == Keys.K_q: result = "@"
            elif event.keyCode == Keys.K_PLUS: result = "~"
                
        return result


    ###
    ##  @param signature           (string) A unique id of the shortcut
    ##  @param definition            (list) A List with the shortcut definition
    ##                                      ex: [ [KeyModifiers.ALT,Keys.K_RIGHT] ]
    ##
    def addShortCut(self,signature,definition):
        if signature in self.__shortcuts:
            return False
        
        self.__shortcuts[signature] = definition
        
        return True
        
    ###
    ##
    ##
    def removeShortCut(self,signature):
        if signature not in self.__shortcuts:
            return False
        
        del self.__shortcuts[signature]
        
    ###
    ##
    ##
    def isShortcut(self,event,signature):
        
        if signature not in self.__shortcuts:
            return False
        
        sc = self.__shortcuts[signature]
        if event.modifiers & sc[0][0] and event.keyCode == sc[0][1]:
            return True
        
        return False

    ###
    ##
    ##
    def isShortcutAny(self,ev):
        
        for k,v in self.__shortcuts.items():
            if self.isShortcut(ev,k):
                return True
        
        return False
    ###
    ##
    ##
    