import biui

## Represents a mouse event for onMouseDown and so on.
#
#
class MouseEvent(biui.Event.Event):
    
    ##
    #
    #
    def __init__(self,eventSource,buttonStates,position,wheelX,wheelY):
        super().__init__(eventSource)
        self.__buttonStates = buttonStates
        self.__position = position
        self.__wheelX = wheelX
        self.__wheelY = wheelY
    
    ## Position as tuple with x and y.
    #  @return         A tuple with the position of the action.
    #
    def getPosition(self):
        return self.__position
    
    ## X position of the mouse action.
    #  @return         X position of the action
    #    
    def getX(self):
        return self.__position[0]
    
    ## Y position of the mouse action.
    #  @return         Y position of the action
    #
    def getY(self):
        return self.__position[1]
    
    ## Horicontal scroll action.
    #  @return         Horicontal scroll action.
    #                  Positive or negative integer value.
    #
    def getWheelX(self):
        return self.__wheelX
    
    ## Vertical scroll action.
    #  @return         Vertical scroll action.
    #                  Positive or negative integer value.
    #    
    def getWheelY(self):
        return self.__wheelY
        
    ## State of button 0 at action time.
    #  @return         A boolean value representing the button's state.
    #
    def pressed0(self):
        return self.__buttonStates[0]
    
    ## State of button 1 at action time.
    #  @return         A boolean value representing the button's state.
    #
    def pressed1(self):
        return self.__buttonStates[1]
    
    ## State of button 2 at action time.
    #  @return         A boolean value representing the button's state.
    #
    def pressed2(self):
        return self.__buttonStates[2]
    
    ## State of button 3 at action time.
    #  @return         A boolean value representing the button's state.
    #
    def pressed3(self):
        return self.__buttonStates[3]
    
    ## State of button 4 at action time.
    #  @return         A boolean value representing the button's state.
    #
    def pressed4(self):
        return self.__buttonStates[4]
    
    ## A string representation of the mouse event.
    #
    def __str__(self):
        result = "MouseEvent("+ str(self.__position[0]) +"/"+  str(self.__position[1]) +")"
        result += "(b0:"+str(self.__buttonStates[0])+" "
        result += "b1:"+str(self.__buttonStates[1])+" "
        result += "b2:"+str(self.__buttonStates[2])+" "
        result += "b3:"+str(self.__buttonStates[3])+" "
        result += "b4:"+str(self.__buttonStates[4])+")"
        result += "(h:"+str(self.__wheelX)+" "
        result += "v:"+str(self.__wheelY)+")"
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    