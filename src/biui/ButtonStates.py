import biui

## ENUM class for button states.
#
#
class ButtonStates():
    
    def __init__(self):
        raise Exception( Messages.ERR_CLASS_NOT_INIT )
    
    # normal button. Mouse is not over it.
    NORMAL = 0
    
    # Mouse is over the button
    OVER   = 1
    
    # Mousebutton is pressed
    DOWN   = 2
    
    # Toggle button is checked
    CHECKED = 3