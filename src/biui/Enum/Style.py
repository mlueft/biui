#include "biui.inc"

###
##
##
class Style():

    def __init__(self):
        raise Exception( BIUI_ERR_CLASS_NOT_INIT )

    NORMAL        = 0x00
    BOLD          = 0x01
    ITALIC        = 0x02
    UNDERLINE     = 0x04
    STRIKETHROUGH = 0x08