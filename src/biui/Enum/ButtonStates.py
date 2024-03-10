import biui

### ENUM class for button states.
##
##
class ButtonStates():
    
    def __init__(self):
        raise Exception( Messages.ERR_CLASS_NOT_INIT )
    
    NORMAL:int = 0      ## normal button. Mouse is not over it.
    OVER:int   = 1      ## Mouse is over the button
    DOWN:int   = 2      ## Mousebutton is pressed
    CHECKED:int = 3     ## Toggle button is checked
    