from biui.Messages import Messages

##
#
#
class KeyMofifiers():
    
    def __init__(self):
        raise Exception( Messages.ERR_CLASS_NOT_INIT )
    
    #           65432109876543210
    #
    NONE     = 0b0000000000000000 #     0
    LSHIFT   = 0b0000000000000001 #     1
    RSHIFT   = 0b0000000000000010 #     2
    SHIFT    = 0b0000000000000011 #     3
    LCTRL    = 0b0000000001000000 #    64
    RCTRL    = 0b0000000010000000 #   128
    CTRL     = 0b0000000011000000 #   192
    LALT     = 0b0000000100000000 #   256
    RALT     = 0b0000001000000000 #   512
    ALT      = 0b0000001100000000 #   768
    LMETA    = 0b0000010000000000 #  1024
    RMETA    = 0b0000100000000000 #  2048
    META     = 0b0000110000000000 #  3072
    CAPS     = 0b0010000000000000 #  8192
    NUM      = 0b0001000000000000 #  4096
    MODE     = 0b0100000000000000 # 16384