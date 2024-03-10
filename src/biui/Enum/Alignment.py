#include "biui.inc"

###
##
##
class Alignment():

    def __init__(self):
        raise Exception( BIUI_ERR_CLASS_NOT_INIT )

    ABSOLUTE      :int = 0   ## position is x and y
    FILL          :int = 1   ## All available space is used
    TOP_LEFT      :int = 2
    TOP_CENTER    :int = 3
    TOP_RIGHT     :int = 4
    CENTER_LEFT   :int = 5
    CENTER_CENTER :int = 6
    CENTER_RIGHT  :int = 7
    BOTTOM_LEFT   :int = 8
    BOTTOM_CENTER :int = 9
    BOTTOM_RIGHT  :int = 10
    DOCK_TOP      :int = 11
    DOCK_LEFT     :int = 12
    DOCK_BOTTOM   :int = 13
    DOCK_RIGHT    :int = 14
