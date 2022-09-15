from biui.Messages import Messages

##
#
#
class Alignment():

    def __init__(self):
        raise Exception( Messages.ERR_CLASS_NOT_INIT )

    ABSOLUTE      = 0   # position is x and y
    FILL          = 1   # All available space is used
    TOP_LEFT      = 2
    TOP_CENTER    = 3
    TOP_RIGHT     = 4
    CENTER_LEFT   = 5
    CENTER_CENTER = 6
    CENTER_RIGHT  = 7
    BOTTOM_LEFT   = 8
    BOTTOM_CENTER = 9
    BOTTOM_RIGHT  = 10
