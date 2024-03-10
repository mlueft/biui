#include "biui.inc"

###
##
##
class Keys():
    
    def __init__(self):
        raise Exception( BIUI_ERR_CLASS_NOT_INIT )
    
    K_UNKNOWN = 0
    K_BACKSPACE = 8
    K_TAB = 9
    K_RETURN = 13
    K_ESCAPE = 27
    K_SPACE = 32
    K_EXCLAIM = 33
    K_QUOTEDBL = 34
    K_HASH = 35
    K_DOLLAR = 36
    K_PERCENT = 37
    K_AMPERSAND = 38
    K_QUOTE = 39
    K_LEFTPAREN = 40
    K_RIGHTPAREN = 41
    
    K_ASTERISK = 42
    K_PLUS = 43
    K_COMMA = 44
    K_MINUS = 45
    K_PERIOD = 46
    K_SLASH = 47
    K_0 = 48
    K_1 = 49
    K_2 = 50
    K_3 = 51
    K_4 = 52
    K_5 = 53
    K_6 = 54
    K_7 = 55
    K_8 = 56
    K_9 = 57
    K_COLON = 58
    K_SEMICOLON = 59
    K_LESS = 60
    K_EQUALS = 61
    K_GREATER = 62
    K_QUESTION = 63
    K_AT = 64
    K_LEFTBRACKET = 91
    K_BACKSLASH = 92
    K_RIGHTBRACKET = 93
    K_CARET = 94
    K_UNDERSCORE = 95
    K_BACKQUOTE = 96
    K_a = 97
    K_b = 98
    K_c = 99
    K_d = 100
    K_e = 101
    K_f = 102
    K_g = 103
    K_h = 104
    K_i = 105
    K_j = 106
    K_k = 107
    K_l = 108
    K_m = 109
    K_n = 110
    K_o = 111
    K_p = 112
    K_q = 113
    K_r = 114
    K_s = 115
    K_t = 116
    K_u = 117
    K_v = 118
    K_w = 119
    K_x = 120
    K_y = 121
    K_z = 122
    K_DELETE = 127
    ## my keys
    K_szlig = 223
    K_uuml = 252
    K_ouml = 246
    K_auml = 228
    ## end
    K_CAPSLOCK = 1073741881
    K_F1 = 1073741882
    K_F2 = 1073741883
    K_F3 = 1073741884
    K_F4 = 1073741885
    K_F5 = 1073741886
    K_F6 = 1073741887
    K_F7 = 1073741888
    K_F8 = 1073741889
    K_F9 = 1073741890
    K_F10 = 1073741891
    K_F11 = 1073741892
    K_F12 = 1073741893
    K_PRINTSCREEN = 1073741894
    K_SCROLLLOCK = 1073741895
    K_PAUSE = 1073741896
    K_INSERT = 1073741897
    K_HOME = 1073741898
    K_PAGEUP = 1073741899
    K_END = 1073741901
    K_PAGEDOWN = 1073741902
    K_RIGHT = 1073741903
    K_LEFT = 1073741904
    K_DOWN = 1073741905
    K_UP = 1073741906
    K_NUMLOCKCLEAR = 1073741907
    K_KP_DIVIDE = 1073741908
    K_KP_MULTIPLY = 1073741909
    K_KP_MINUS = 1073741910
    K_KP_PLUS = 1073741911
    K_KP_ENTER = 1073741912
    K_KP_1 = 1073741913
    K_KP_2 = 1073741914
    K_KP_3 = 1073741915
    K_KP_4 = 1073741916
    K_KP_5 = 1073741917
    K_KP_6 = 1073741918
    K_KP_7 = 1073741919
    K_KP_8 = 1073741920
    K_KP_9 = 1073741921
    K_KP_0 = 1073741922
    K_KP_PERIOD = 1073741923
    K_APPLICATION = 1073741925
    K_POWER = 1073741926
    K_KP_EQUALS = 1073741927
    K_F13 = 1073741928
    K_F14 = 1073741929
    K_F15 = 1073741930
    K_F16 = 1073741931
    K_F17 = 1073741932
    K_F18 = 1073741933
    K_F19 = 1073741934
    K_F20 = 1073741935
    K_F21 = 1073741936
    K_F22 = 1073741937
    K_F23 = 1073741938
    K_F24 = 1073741939
    K_EXECUTE = 1073741940
    K_HELP = 1073741941
    K_MENU = 1073741942
    K_SELECT = 1073741943
    K_STOP = 1073741944
    K_AGAIN = 1073741945
    K_UNDO = 1073741946
    K_CUT = 1073741947
    K_COPY = 1073741948
    K_PASTE = 1073741949
    K_FIND = 1073741950
    K_MUTE = 1073741951
    K_VOLUMEUP = 1073741952
    K_VOLUMEDOWN = 1073741953
    K_KP_COMMA = 1073741957
    K_KP_EQUALSAS400 = 1073741958
    K_ALTERASE = 1073741977
    K_SYSREQ = 1073741978
    K_CANCEL = 1073741979
    K_CLEAR = 1073741980
    K_PRIOR = 1073741981
    K_RETURN2 = 1073741982
    K_SEPARATOR = 1073741983
    K_OUT = 1073741984
    K_OPER = 1073741985
    K_CLEARAGAIN = 1073741986
    K_CRSEL = 1073741987
    K_EXSEL = 1073741988
    K_KP_00 = 1073742000
    K_KP_000 = 1073742001
    K_THOUSANDSSEPARATOR = 1073742002
    K_DECIMALSEPARATOR = 1073742003
    K_CURRENCYUNIT = 1073742004
    K_CURRENCYSUBUNIT = 1073742005
    K_KP_LEFTPAREN = 1073742006
    K_KP_RIGHTPAREN = 1073742007
    K_KP_LEFTBRACE = 1073742008
    K_KP_RIGHTBRACE = 1073742009
    K_KP_TAB = 1073742010
    K_KP_BACKSPACE = 1073742011
    K_KP_A = 1073742012
    K_KP_B = 1073742013
    K_KP_C = 1073742014
    K_KP_D = 1073742015
    K_KP_E = 1073742016
    K_KP_F = 1073742017
    K_KP_XOR = 1073742018
    K_KP_POWER = 1073742019
    K_KP_PERCENT = 1073742020
    K_KP_LESS = 1073742021
    K_KP_GREATER = 1073742022
    K_KP_AMPERSAND = 1073742023
    K_KP_DBLAMPERSAND = 1073742024
    K_KP_VERTICALBAR = 1073742025
    K_KP_DBLVERTICALBAR = 1073742026
    K_KP_COLON = 1073742027
    K_KP_HASH = 1073742028
    K_KP_SPACE = 1073742029
    K_KP_AT = 1073742030
    K_KP_EXCLAM = 1073742031
    K_KP_MEMSTORE = 1073742032
    K_KP_MEMRECALL = 1073742033
    K_KP_MEMCLEAR = 1073742034
    K_KP_MEMADD = 1073742035
    K_KP_MEMSUBTRACT = 1073742036
    K_KP_MEMMULTIPLY = 1073742037
    K_KP_MEMDIVIDE = 1073742038
    K_KP_PLUSMINUS = 1073742039
    K_KP_CLEAR = 1073742040
    K_KP_CLEARENTRY = 1073742041
    K_KP_BINARY = 1073742042
    K_KP_OCTAL = 1073742043
    K_KP_DECIMAL = 1073742044
    K_KP_HEXADECIMAL = 1073742045
    K_LCTRL = 1073742048
    K_LSHIFT = 1073742049
    K_LALT = 1073742050
    K_LGUI = 1073742051
    K_RCTRL = 1073742052
    K_RSHIFT = 1073742053
    K_RALT = 1073742054
    K_RGUI = 1073742055
    K_MODE = 1073742081
    K_AUDIONEXT = 1073742082
    K_AUDIOPREV = 1073742083
    K_AUDIOSTOP = 1073742084
    K_AUDIOPLAY = 1073742085
    K_AUDIOMUTE = 1073742086
    K_MEDIASELECT = 1073742087
    K_WWW = 1073742088
    K_MAIL = 1073742089
    K_CALCULATOR = 1073742090
    K_COMPUTER = 1073742091
    K_AC_SEARCH = 1073742092
    K_AC_HOME = 1073742093
    K_AC_BACK = 1073742094
    K_AC_FORWARD = 1073742095
    K_AC_STOP = 1073742096
    K_AC_REFRESH = 1073742097
    K_AC_BOOKMARKS = 1073742098
    K_BRIGHTNESSDOWN = 1073742099
    K_BRIGHTNESSUP = 1073742100
    K_DISPLAYSWITCH = 1073742101
    K_KBDILLUMTOGGLE = 1073742102
    K_KBDILLUMDOWN = 1073742103
    K_KBDILLUMUP = 1073742104
    K_EJECT = 1073742105
    K_SLEEP = 1073742106
