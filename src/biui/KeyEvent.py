import biui
from biui.DOMEvent import DOMEvent
from biui.KeyModifiers import KeyModifiers
from biui.Keys import Keys

### Represents a KeyEvent. 
##
##
class KeyEvent(DOMEvent):
    
    def __init__(self,eventSource,keyCode,scanCode,modifiers,repeat,timestamp):
        super().__init__(eventSource)
        self.__keyCode = keyCode
        self.__scanCode = scanCode
        self.__modifiers = modifiers
        self.__repeat = repeat != 0
        self.__timestamp = timestamp
            
    def __str__(self):
        return "KeyEvent: key: {} scancode: {} mod: ({}) rep: {} time: {}".format(
            self.__decodeKeyCode(),
            self.__decodeScanCode(),
            self.__decodeModifiers(),    
            biui.default(self.__repeat,""),
            biui.default(self.__timestamp,"")            
        )
    
    ###
    ##
    ##
    @property
    def keyCode(self):
        return self.__keyCode
    
    ###
    ##
    ##
    @property
    def scanCode(self):
        return self.__scanCode
     
    ###
    ##
    ##
    @property
    def modifiers(self):
        return self.__modifiers
    
    ###
    ##
    ##
    @property
    def repeat(self):
        return self.__repeat
    
    ###
    ##
    ##
    @property
    def timestamp(self):
        return self.__timestamp
    
    def __decodeModifiers(self):
        result = str(self.__modifiers)+" "
        
        if self.__modifiers == KeyModifiers.NONE:
            result += "none "
        
        if self.__modifiers & KeyModifiers.LSHIFT:
            result += "lshift "
        
        if self.__modifiers & KeyModifiers.RSHIFT:
            result += "rshift "
                
        if self.__modifiers & KeyModifiers.SHIFT:
            result += "shift "
            
        if self.__modifiers & KeyModifiers.LCTRL:
            result += "lctrl "
            
        if self.__modifiers & KeyModifiers.RCTRL:
            result += "rctrl "
        
        if self.__modifiers & KeyModifiers.CTRL:
            result += "ctrl "
            
        if self.__modifiers & KeyModifiers.LALT:
            result += "lalt "
            
        if self.__modifiers & KeyModifiers.RALT:
            result += "ralt "
            
        if self.__modifiers & KeyModifiers.ALT:
            result += "alt "
            
        if self.__modifiers & KeyModifiers.LMETA:
            result += "lmeta "
            
        if self.__modifiers & KeyModifiers.RMETA:
            result += "rmeta "
            
        if self.__modifiers & KeyModifiers.META:
            result += "meta "
            
        if self.__modifiers & KeyModifiers.CAPS:
            result += "caps "
            
        if self.__modifiers & KeyModifiers.NUM:
            result += "num "
            
        if self.__modifiers & KeyModifiers.MODE:
            result += "mode "
            
        if self.__modifiers & KeyModifiers.SCROLL:
            result += "scroll "
            
        return result
    
    def __decodeKeyCode(self):
        result = ""
        
        if self.__keyCode == Keys.K_BACKSPACE: result += "K_BACKSPACE";
        elif self.__keyCode == Keys.K_TAB: result += "K_TAB";
        elif self.__keyCode == Keys.K_CLEAR: result += "K_CLEAR";
        elif self.__keyCode == Keys.K_RETURN: result += "K_RETURN";
        elif self.__keyCode == Keys.K_PAUSE: result += "K_PAUSE";
        elif self.__keyCode == Keys.K_ESCAPE: result += "K_ESCAPE";
        elif self.__keyCode == Keys.K_SPACE: result += "K_SPACE";
        elif self.__keyCode == Keys.K_EXCLAIM: result += "K_EXCLAIM";
        elif self.__keyCode == Keys.K_QUOTEDBL: result += "K_QUOTEDBL";
        elif self.__keyCode == Keys.K_HASH: result += "K_HASH";
        elif self.__keyCode == Keys.K_DOLLAR: result += "K_DOLLAR";
        elif self.__keyCode == Keys.K_AMPERSAND: result += "K_AMPERSAND";
        elif self.__keyCode == Keys.K_QUOTE: result += "K_QUOTE";
        elif self.__keyCode == Keys.K_LEFTPAREN: result += "K_LEFTPAREN";
        elif self.__keyCode == Keys.K_RIGHTPAREN: result += "K_RIGHTPAREN";
        elif self.__keyCode == Keys.K_ASTERISK: result += "K_ASTERISK";
        elif self.__keyCode == Keys.K_PLUS: result += "K_PLUS";
        elif self.__keyCode == Keys.K_COMMA: result += "K_COMMA";
        elif self.__keyCode == Keys.K_MINUS: result += "K_MINUS";
        elif self.__keyCode == Keys.K_PERIOD: result += "K_PERIOD";
        elif self.__keyCode == Keys.K_SLASH: result += "K_SLASH";
        elif self.__keyCode == Keys.K_0: result += "K_0";
        elif self.__keyCode == Keys.K_1: result += "K_1";
        elif self.__keyCode == Keys.K_2: result += "K_2";
        elif self.__keyCode == Keys.K_3: result += "K_3";
        elif self.__keyCode == Keys.K_4: result += "K_4";
        elif self.__keyCode == Keys.K_5: result += "K_5";
        elif self.__keyCode == Keys.K_6: result += "K_6";
        elif self.__keyCode == Keys.K_7: result += "K_7";
        elif self.__keyCode == Keys.K_8: result += "K_8";
        elif self.__keyCode == Keys.K_9: result += "K_9";
        elif self.__keyCode == Keys.K_COLON: result += "K_COLON";
        elif self.__keyCode == Keys.K_SEMICOLON: result += "K_SEMICOLON";
        elif self.__keyCode == Keys.K_LESS: result += "K_LESS";
        elif self.__keyCode == Keys.K_EQUALS: result += "K_EQUALS";
        elif self.__keyCode == Keys.K_GREATER: result += "K_GREATER";
        elif self.__keyCode == Keys.K_QUESTION: result += "K_QUESTION";
        elif self.__keyCode == Keys.K_AT: result += "K_AT";
        elif self.__keyCode == Keys.K_LEFTBRACKET: result += "K_LEFTBRACKET";
        elif self.__keyCode == Keys.K_BACKSLASH: result += "K_BACKSLASH";
        elif self.__keyCode == Keys.K_RIGHTBRACKET: result += "K_RIGHTBRACKET";
        elif self.__keyCode == Keys.K_CARET: result += "K_CARET";
        elif self.__keyCode == Keys.K_UNDERSCORE: result += "K_UNDERSCORE";
        elif self.__keyCode == Keys.K_BACKQUOTE: result += "K_BACKQUOTE";
        elif self.__keyCode == Keys.K_a: result += "K_a";
        elif self.__keyCode == Keys.K_b: result += "K_b";
        elif self.__keyCode == Keys.K_c: result += "K_c";
        elif self.__keyCode == Keys.K_d: result += "K_d";
        elif self.__keyCode == Keys.K_e: result += "K_e";
        elif self.__keyCode == Keys.K_f: result += "K_f";
        elif self.__keyCode == Keys.K_g: result += "K_g";
        elif self.__keyCode == Keys.K_h: result += "K_h";
        elif self.__keyCode == Keys.K_i: result += "K_i";
        elif self.__keyCode == Keys.K_j: result += "K_j";
        elif self.__keyCode == Keys.K_k: result += "K_k";
        elif self.__keyCode == Keys.K_l: result += "K_l";
        elif self.__keyCode == Keys.K_m: result += "K_m";
        elif self.__keyCode == Keys.K_n: result += "K_n";
        elif self.__keyCode == Keys.K_o: result += "K_o";
        elif self.__keyCode == Keys.K_p: result += "K_p";
        elif self.__keyCode == Keys.K_q: result += "K_q";
        elif self.__keyCode == Keys.K_r: result += "K_r";
        elif self.__keyCode == Keys.K_s: result += "K_s";
        elif self.__keyCode == Keys.K_t: result += "K_t";
        elif self.__keyCode == Keys.K_u: result += "K_u";
        elif self.__keyCode == Keys.K_v: result += "K_v";
        elif self.__keyCode == Keys.K_w: result += "K_w";
        elif self.__keyCode == Keys.K_x: result += "K_x";
        elif self.__keyCode == Keys.K_y: result += "K_y";
        elif self.__keyCode == Keys.K_z: result += "K_z";
        elif self.__keyCode == Keys.K_DELETE: result += "K_DELETE";
        elif self.__keyCode == Keys.K_KP0: result += "K_KP0";
        elif self.__keyCode == Keys.K_KP1: result += "K_KP1";
        elif self.__keyCode == Keys.K_KP2: result += "K_KP2";
        elif self.__keyCode == Keys.K_KP3: result += "K_KP3";
        elif self.__keyCode == Keys.K_KP4: result += "K_KP4";
        elif self.__keyCode == Keys.K_KP5: result += "K_KP5";
        elif self.__keyCode == Keys.K_KP6: result += "K_KP6";
        elif self.__keyCode == Keys.K_KP7: result += "K_KP7";
        elif self.__keyCode == Keys.K_KP8: result += "K_KP8";
        elif self.__keyCode == Keys.K_KP9: result += "K_KP9";
        elif self.__keyCode == Keys.K_KP_PERIOD: result += "K_KP_PERIOD";
        elif self.__keyCode == Keys.K_KP_DIVIDE: result += "K_KP_DIVIDE";
        elif self.__keyCode == Keys.K_KP_MULTIPLY: result += "K_KP_MULTIPLY";
        elif self.__keyCode == Keys.K_KP_MINUS: result += "K_KP_MINUS";
        elif self.__keyCode == Keys.K_KP_PLUS: result += "K_KP_PLUS";
        elif self.__keyCode == Keys.K_KP_ENTER: result += "K_KP_ENTER";
        elif self.__keyCode == Keys.K_KP_EQUALS: result += "K_KP_EQUALS";
        elif self.__keyCode == Keys.K_UP: result += "K_UP";
        elif self.__keyCode == Keys.K_DOWN: result += "K_DOWN";
        elif self.__keyCode == Keys.K_RIGHT: result += "K_RIGHT";
        elif self.__keyCode == Keys.K_LEFT: result += "K_LEFT";
        elif self.__keyCode == Keys.K_INSERT: result += "K_INSERT";
        elif self.__keyCode == Keys.K_HOME: result += "K_HOME";
        elif self.__keyCode == Keys.K_END: result += "K_END";
        elif self.__keyCode == Keys.K_PAGEUP: result += "K_PAGEUP";
        elif self.__keyCode == Keys.K_PAGEDOWN: result += "K_PAGEDOWN";
        elif self.__keyCode == Keys.K_F1: result += "K_F1";
        elif self.__keyCode == Keys.K_F2: result += "K_F2";
        elif self.__keyCode == Keys.K_F3: result += "K_F3";
        elif self.__keyCode == Keys.K_F4: result += "K_F4";
        elif self.__keyCode == Keys.K_F5: result += "K_F5";
        elif self.__keyCode == Keys.K_F6: result += "K_F6";
        elif self.__keyCode == Keys.K_F7: result += "K_F7";
        elif self.__keyCode == Keys.K_F8: result += "K_F8";
        elif self.__keyCode == Keys.K_F9: result += "K_F9";
        elif self.__keyCode == Keys.K_F10: result += "K_F10";
        elif self.__keyCode == Keys.K_F11: result += "K_F11";
        elif self.__keyCode == Keys.K_F12: result += "K_F12";
        elif self.__keyCode == Keys.K_F13: result += "K_F13";
        elif self.__keyCode == Keys.K_F14: result += "K_F14";
        elif self.__keyCode == Keys.K_F15: result += "K_F15";
        elif self.__keyCode == Keys.K_NUMLOCK: result += "K_NUMLOCK";
        elif self.__keyCode == Keys.K_CAPSLOCK: result += "K_CAPSLOCK";
        elif self.__keyCode == Keys.K_SCROLLOCK: result += "K_SCROLLOCK";
        elif self.__keyCode == Keys.K_RSHIFT: result += "K_RSHIFT";
        elif self.__keyCode == Keys.K_LSHIFT: result += "K_LSHIFT";
        elif self.__keyCode == Keys.K_RCTRL: result += "K_RCTRL";
        elif self.__keyCode == Keys.K_LCTRL: result += "K_LCTRL";
        elif self.__keyCode == Keys.K_RALT: result += "K_RALT";
        elif self.__keyCode == Keys.K_LALT: result += "K_LALT";
        elif self.__keyCode == Keys.K_RMETA: result += "K_RMETA";
        elif self.__keyCode == Keys.K_LMETA: result += "K_LMETA";
        elif self.__keyCode == Keys.K_LSUPER: result += "K_LSUPER";
        elif self.__keyCode == Keys.K_RSUPER: result += "K_RSUPER";
        elif self.__keyCode == Keys.K_MODE: result += "K_MODE";
        elif self.__keyCode == Keys.K_HELP: result += "K_HELP";
        elif self.__keyCode == Keys.K_PRINT: result += "K_PRINT";
        elif self.__keyCode == Keys.K_SYSREQ: result += "K_SYSREQ";
        elif self.__keyCode == Keys.K_BREAK: result += "K_BREAK";
        elif self.__keyCode == Keys.K_MENU: result += "K_MENU";
        elif self.__keyCode == Keys.K_POWER: result += "K_POWER";
        elif self.__keyCode == Keys.K_EURO: result += "K_EURO";
        elif self.__keyCode == Keys.K_AC_BACK: result += "K_AC_BACK";
        return result
     
    def __decodeScanCode(self):
        result = str(self.__scanCode)+" "
        
        return result