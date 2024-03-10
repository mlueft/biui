#include "biui.inc"

###
##
##
class Direction():

    def __init__(self):
        raise Exception( BIUI_ERR_CLASS_NOT_INIT )

    LTR = 0      ## Left to right.
    RTL = 1      ## Right to left.
    TTB = 2      ## Top to bottom.
    BTT = 3      ## Bottom to top. 