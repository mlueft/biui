import time
import sys
import os
import biui
import biui.Enum as Keys
import biui.Enum as KeyModifiers
from biui.Widgets import Button,Window

KEYS = {}


def createKeyBoard(x,y,parent):
    createMainBlock(x,y,parent)
    createCursorBlock(x+750,y+70,parent)
    createNumBlock(x+950,y+70,parent)
    createSpecialBlock(x,y+340,parent)

def createSpecialBlock(x,y,parent):
    
    buttonWidth = 120
    buttonHeight = 30
    
    bx = x
    by = y
    
    keys = [
        ["K_UNKNOWN", "UNKNOWN"],
        ["K_EXCLAIM", "EXCLAIM"],
        ["K_QUOTEDBL", "QUOTEDBL"],
        ["K_DOLLAR", "DOLLAR"],
        ["K_PERCENT", "PERCENT"],
        ["K_AMPERSAND", "AMPERSAND",130],
        ["K_QUOTE", "QUOTE"],
        ["K_LEFTPAREN", "LEFTPAREN",140],
        ["K_RIGHTPAREN", "RIGHTPAREN",140],
        ["K_ASTERISK", "ASTERISK"],
        ["K_SLASH", "SLASH"],
        ["K_COLON", "COLON"],
        ["K_SEMICOLON", "SEMICOLON",130],
        ["K_EQUALS", "EQUALS"],
        ["K_GREATER", "GREATER"],
        ["K_QUESTION", "QUESTION"],
        ["K_AT", "AT"],
        ["K_LEFTBRACKET", "LEFTBRACKET",140],
        ["K_BACKSLASH", "BACKSLASH",130],
        ["K_RIGHTBRACKET", "RIGHTBRACKET",150],
        ["K_CARET", "CARET"],
        ["K_UNDERSCORE", "UNDERSCORE",140],
        ["K_BACKQUOTE", "BACKQUOTE",140],
        ["K_APPLICATION", "APPLICATION",140],
        ["K_POWER", "POWER"],
        ["K_KP_EQUALS", "KP_EQUALS",140],
        ["K_F16", "F16",60],
        ["K_F17", "F17",60],
        ["K_F18", "F18",60],
        ["K_F19", "F19",60],
        ["K_F20", "F20",60],
        ["K_F21", "F21",60],
        ["K_F22", "F22",60],
        ["K_F23", "F23",60],
        ["K_F24", "F24",60],
        ["K_EXECUTE", "EXECUTE"],
        ["K_HELP", "HELP"],
        ["K_SELECT", "SELECT"],
        ["K_STOP", "STOP"],
        ["K_AGAIN", "AGAIN"],
        ["K_UNDO", "UNDO"],
        ["K_CUT", "CUT"],
        ["K_COPY", "COPY"],
        ["K_PASTE", "PASTE"],
        ["K_FIND", "FIND"],
        ["K_MUTE", "MUTE"],
        ["K_VOLUMEUP", "VOLUMEUP"],
        ["K_VOLUMEDOWN", "VOLUMEDOWN",160],
        ["K_KP_COMMA", "KP_COMMA",140],
        ["K_KP_EQUALSAS400", "KP_EQUALSAS400",180],
        ["K_ALTERASE", "ALTERASE"],
        ["K_SYSREQ", "SYSREQ"],
        ["K_CANCEL", "CANCEL"],
        ["K_CLEAR", "CLEAR"],
        ["K_PRIOR", "PRIOR"],
        ["K_RETURN2", "RETURN2"],
        ["K_SEPARATOR", "K_SEPARATOR",160],
        ["K_OUT", "OUT"],
        ["K_OPER", "OPER"],
        ["K_CLEARAGAIN", "CLEARAGAIN",150],
        ["K_CRSEL", "CRSEL"],
        ["K_EXSEL", "EXSEL"],
        ["K_KP_00", "KP_00"],
        ["K_KP_000", "KP_000"],
        ["K_THOUSANDSSEPARATOR", "THOUSANDSSEPARATOR",250],
        ["K_DECIMALSEPARATOR", "DECIMALSEPARATOR",250],
        ["K_CURRENCYUNIT", "CURRENCYUNIT",200],
        ["K_CURRENCYSUBUNIT", "CURRENCYSUBUNIT",200],
        ["K_KP_LEFTPAREN", "KP_LEFTPAREN",200],
        ["K_KP_RIGHTPAREN", "KP_RIGHTPAREN",200],
        ["K_KP_LEFTBRACE", "KP_LEFTBRACE",200],
        ["K_KP_RIGHTBRACE", "KP_RIGHTBRACE",200],
        ["K_KP_TAB", "KP_TAB"],
        ["K_KP_BACKSPACE", "KP_BACKSPACE",200],
        ["K_KP_A", "KP_A",60],
        ["K_KP_B", "KP_B",60],
        ["K_KP_C", "KP_C",60],
        ["K_KP_D", "KP_D",60],
        ["K_KP_E", "KP_E",60],
        ["K_KP_F", "KP_F",60],
        ["K_KP_XOR", "KP_XOR"],
        ["K_KP_POWER", "KP_POWER"],
        ["K_KP_PERCENT", "KP_PERCENT",140],
        ["K_KP_LESS", "KP_LESS"],
        ["K_KP_GREATER", "KP_GREATER",150],
        ["K_KP_AMPERSAND", "KP_AMPERSAND",200],
        ["K_KP_DBLAMPERSAND", "KP_DBLAMPERSAND",230],
        ["K_KP_VERTICALBAR", "KP_VERTICALBAR",210],
        ["K_KP_DBLVERTICALBAR", "KP_DBLVERTICALBAR",250],
        ["K_KP_COLON", "KP_COLON"],
        ["K_KP_HASH", "KP_HASH"],
        ["K_KP_SPACE", "KP_SPACE"],
        ["K_KP_AT", "KP_AT"],
        ["K_KP_EXCLAM", "KP_EXCLAM",200],
        ["K_KP_MEMSTORE", "KP_MEMSTORE",200],
        ["K_KP_MEMRECALL", "KP_MEMRECALL",200],
        ["K_KP_MEMCLEAR", "KP_MEMCLEAR",200],
        ["K_KP_MEMADD", "KP_MEMADD",200],
        ["K_KP_MEMSUBTRACT", "KP_MEMSUBTRACT",200],
        ["K_KP_MEMMULTIPLY", "KP_MEMMULTIPLY",200],
        ["K_KP_MEMDIVIDE", "KP_MEMDIVIDE",200],
        ["K_KP_PLUSMINUS", "KP_PLUSMINUS",200],
        ["K_KP_CLEAR", "KP_CLEAR"],
        ["K_KP_CLEARENTRY", "KP_CLEARENTRY",200],
        ["K_KP_BINARY", "KP_BINARY"],
        ["K_KP_OCTAL", "KP_OCTAL"],
        ["K_KP_DECIMAL", "KP_DECIMAL",130],
        ["K_KP_HEXADECIMAL", "KP_HEXADECIMAL",200],
        ["K_MODE", "MODE"],
        ["K_AUDIONEXT", "AUDIONEXT",130],
        ["K_AUDIOPREV", "AUDIOPREV",130],
        ["K_AUDIOSTOP", "AUDIOSTOP",130],
        ["K_AUDIOPLAY", "AUDIOPLAY",130],
        ["K_AUDIOMUTE", "AUDIOMUTE",130],
        ["K_MEDIASELECT", "MEDIASELECT",150],
        ["K_WWW", "WWW",70],
        ["K_MAIL", "MAIL",70],
        ["K_CALCULATOR", "CALCULATOR",200],
        ["K_COMPUTER", "COMPUTER",140],
        ["K_AC_SEARCH", "AC_SEARCH",130],
        ["K_AC_HOME", "AC_HOME"],
        ["K_AC_BACK", "AC_BACK"],
        ["K_AC_FORWARD", "AC_FORWARD",180],
        ["K_AC_STOP", "AC_STOP"],
        ["K_AC_REFRESH", "AC_REFRESH",200],
        ["K_AC_BOOKMARKS", "AC_BOOKMARKS",200],
        ["K_BRIGHTNESSDOWN", "BRIGHTNESSDOWN",200],
        ["K_BRIGHTNESSUP", "BRIGHTNESSUP",200],
        ["K_DISPLAYSWITCH", "DISPLAYSWITCH",200],
        ["K_KBDILLUMTOGGLE", "KBDILLUMTOGGLE",200],
        ["K_KBDILLUMDOWN", "KBDILLUMDOWN",200],
        ["K_KBDILLUMUP", "KBDILLUMUP",200],
        ["K_EJECT", "EJECT"],
        ["K_SLEEP", "SLEEP"]
    ]
    
    for key in keys:
        
        b = Button()
        b.x = bx
        b.y = by
        if len(key)>2:
            b.width = key[2]
        else:
            b.width = buttonWidth
        b.height = buttonHeight
        b.value = key[1]
        parent.addChild(b)
        bx = b.right
        if bx > 1100:
            bx = x
            by = b.bottom
            
        if getattr(Keys,key[0]) in KEYS:
            print(key[0])
            
        KEYS[getattr(Keys,key[0])] = b
        
def createNumBlock(x,y,parent):
    
    buttonWidth = 50
    buttonHeight = buttonWidth
    
    bx = x
    by = y
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Num"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_NUMLOCKCLEAR] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "/"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_DIVIDE] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "*"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_MULTIPLY] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "-"
    parent.addChild(b)
    bx = x
    by = b.bottom
    KEYS[Keys.K_KP_MINUS] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "7"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_7] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "8"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_8] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "9"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_9] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "+"
    parent.addChild(b)
    bx = x
    by = b.bottom
    b.height = buttonHeight*2
    KEYS[Keys.K_KP_PLUS] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "4"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_4] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "5"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_5] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "6"
    parent.addChild(b)
    bx = x
    by = b.bottom
    KEYS[Keys.K_KP_6] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "1"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_1] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "2"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_2] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "3"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_3] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Ent"
    parent.addChild(b)
    bx = x
    by = b.bottom
    b.height = buttonHeight*2
    KEYS[Keys.K_KP_ENTER] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth*2
    b.height = buttonHeight
    b.value = "0"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_0] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = ","
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_KP_PERIOD] = b
    
def createCursorBlock(x,y,parent):
    
    buttonWidth = 50
    buttonHeight = buttonWidth
    
    bx = x
    by = y
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Ins"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_INSERT] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "P1"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_HOME] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Pup"
    parent.addChild(b)
    bx = x
    by = b.bottom
    KEYS[Keys.K_PAGEUP] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Del"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_DELETE] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "End"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_END] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "PDn"
    parent.addChild(b)
    bx = b.right-2*buttonWidth
    by = b.bottom+50
    KEYS[Keys.K_PAGEDOWN] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Up"
    parent.addChild(b)
    bx = b.right-2*buttonWidth
    by = b.bottom
    KEYS[Keys.K_UP] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Lft"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_LEFT] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Dwn"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_DOWN] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Rght"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_RIGHT] = b
    
def createMainBlock(x,y,parent):

    buttonWidth = 50
    buttonHeight = buttonWidth
    
    bx = x
    by = y
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Esc"
    parent.addChild(b)
    bx = b.right+10
    KEYS[Keys.K_ESCAPE] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F1"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F1] = b

    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F2"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F2] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F3"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F3] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F4"
    parent.addChild(b)
    bx = b.right+10
    KEYS[Keys.K_F4] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F5"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F5] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F6"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F6] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F7"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F7] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F8"
    parent.addChild(b)
    bx = b.right+10
    KEYS[Keys.K_F8] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F9"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F9] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F10"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F10] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F11"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F11] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F12"
    parent.addChild(b)
    bx = b.right+20
    KEYS[Keys.K_F12] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F13"
    parent.addChild(b)
    bx = b.right 
    KEYS[Keys.K_F13] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F14"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_F14] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "F15"
    parent.addChild(b)
    bx = b.right + 50
    KEYS[Keys.K_F15] = b
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Prt"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_PRINTSCREEN] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Scr"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_SCROLLLOCK] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+20
    b.height = buttonHeight
    b.value = "Pause"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_PAUSE] = b
    
    bx = x
    by = b.bottom+20
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "^"
    parent.addChild(b)
    bx = b.right
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "1"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_1] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "2"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_2] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "3"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_3] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "4"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_4] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "5"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_5] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "6"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_6] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "7"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_7] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "8"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_8] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "9"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_9] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "0"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_0] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "ß"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_szlig] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "`"
    parent.addChild(b)
    bx = b.right
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+20
    b.height = buttonHeight
    b.value = "bsp"
    parent.addChild(b)
    bx = x
    by = b.bottom
    KEYS[Keys.K_BACKSPACE] = b
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+20
    b.height = buttonHeight
    b.value = "Tab"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_TAB] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "q"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_q] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "w"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_w] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "e"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_e] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "r"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_r] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "t"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_t] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "z"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_z] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "u"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_u] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "i"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_i] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "o"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_o] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "p"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_p] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "ü"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_uuml] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "+"
    parent.addChild(b)
    bx = x
    by =b.bottom
    KEYS[Keys.K_PLUS] = b
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+30
    b.height = buttonHeight
    b.value = "Cap"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_CAPSLOCK] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "a"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_a] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "s"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_s] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "d"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_d] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "f"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_f] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "g"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_g] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "h"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_h] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "j"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_j] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "k"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_k] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "l"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_l] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "ö"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_ouml] = b
        
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "ä"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_auml] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "#"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_HASH] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "ret"
    parent.addChild(b)
    bx = x
    by = b.bottom
    KEYS[Keys.K_RETURN] = b
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+20
    b.height = buttonHeight
    b.value = "Shft"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_LSHIFT] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "<"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_LESS] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "y"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_y] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "x"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_x] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "c"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_c] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "v"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_v] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "b"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_b] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "n"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_n] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "m"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_m] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = ","
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_COMMA] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "."
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_PERIOD] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "-"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_MINUS] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+50
    b.height = buttonHeight
    b.value = "Shft"
    parent.addChild(b)
    bx = x
    by = b.bottom
    KEYS[Keys.K_RSHIFT] = b
    
    
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth+20
    b.height = buttonHeight
    b.value = "Strg"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_LCTRL] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Wnd"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_LGUI] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Alt"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_LALT] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth*6
    b.height = buttonHeight
    b.value = "Space"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_SPACE] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth*2
    b.height = buttonHeight
    b.value = "AltGr"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_RALT] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Wnd"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_RGUI] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Mnu"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_MENU] = b
    
    b = Button()
    b.x = bx
    b.y = by
    b.width = buttonWidth
    b.height = buttonHeight
    b.value = "Strg"
    parent.addChild(b)
    bx = b.right
    KEYS[Keys.K_RCTRL] = b
    
def decodeModifiers(ev):
    if ev.modifiers & KeyModifiers.LSHIFT:
        KEYS[Keys.K_LSHIFT].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_LSHIFT].borderColor = None
        
    if ev.modifiers & KeyModifiers.RSHIFT:
        KEYS[Keys.K_RSHIFT].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_RSHIFT].borderColor = None
        
    if ev.modifiers & KeyModifiers.LCTRL:
        KEYS[Keys.K_LCTRL].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_LCTRL].borderColor = None

    if ev.modifiers & KeyModifiers.RCTRL:
        KEYS[Keys.K_RCTRL].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_RCTRL].borderColor = None
                
    if ev.modifiers & KeyModifiers.LALT:
        KEYS[Keys.K_LALT].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_LALT].borderColor = None
        
    if ev.modifiers & KeyModifiers.RALT:
        KEYS[Keys.K_RALT].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_RALT].borderColor = None
        
    ##if ev.modifiers & KeyModifiers.LMETA:
    ##    KEYS[Keys.K_LMETA].borderColor = biui.Color(255,255,0)
    ##else:
    ##    KEYS[Keys.K_LMETA].borderColor = None
        
    ##if ev.modifiers & KeyModifiers.RMETA:
    ##    KEYS[Keys.K_RMETA].borderColor = biui.Color(255,255,0)
    ##else:
    ##    KEYS[Keys.K_RMETA].borderColor = None
        
    if ev.modifiers & KeyModifiers.CAPS:
        KEYS[Keys.K_CAPSLOCK].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_CAPSLOCK].borderColor = None
        
    if ev.modifiers & KeyModifiers.NUM:
        KEYS[Keys.K_NUMLOCKCLEAR].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_NUMLOCKCLEAR].borderColor = None

    ##if ev.modifiers & KeyModifiers.MODE:
    ##    KEYS[Keys.K_MODE].borderColor = biui.Color(255,255,0)
    ##else:
    ##    KEYS[Keys.K_MODE].borderColor = None

    if ev.modifiers & KeyModifiers.SCROLL:
        KEYS[Keys.K_SCROLLLOCK].borderColor = biui.Color(255,255,0)
    else:
        KEYS[Keys.K_SCROLLLOCK].borderColor = None
            
def hndKeyDown(ev):
    
    if ev.keyCode not in KEYS:
        print("KeyDown key code ({}) not found".format(ev.keyCode))
        return
    key = KEYS[ev.keyCode]
    key.backColor = biui.Color(0,255,0)
    decodeModifiers(ev)


def hndKeyUp(ev):
    if ev.keyCode not in KEYS:
        print("KeyUp key code({}) not found".format(ev.keyCode))
        return
    key = KEYS[ev.keyCode]
    key.backColor = None
    decodeModifiers(ev)

def init():

    biui.init()
    biui.setThemeFolder(
        os.path.abspath(
            os.path.join(os.getcwd(),"./themes")
        )
    )
    
    biui.selectTheme("blocks")

            
def main():
    init()
    
    wnd = Window(1300,900)
    wnd.title = "title"
    wnd.x = 200
    wnd.y = 10
    wnd.onKeyDown.add(hndKeyDown)
    wnd.onKeyUp.add(hndKeyUp)
    createKeyBoard(50,50,wnd)
    
    while biui.main():
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()
    
biui.quit()

print("fertig")
