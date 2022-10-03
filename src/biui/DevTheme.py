import biui

class DevTheme(biui.Theme.Theme):
    

 
    def drawWindowBeforeChildren(self, renderer, widget, texture):
        biui.DL.fill( renderer,texture, biui.Color(66,128,66,255).rgba )

    def drawFlexGridBeforeChildren(self, renderer, widget, texture):
        biui.DL.drawRect(
            renderer,
            texture,
            biui.Color(128,0,0,255).rgba,
            (
                0,
                0,
                widget.width,
                widget.height
            ),
            1
        )
        
    def drawFlexPaneBeforeChildren(self, renderer, widget, texture):
        biui.DL.drawRect(
            renderer,
            texture,
            biui.Color(55,55,55,255).rgba,
            (
                0,
                0,
                widget.width,
                widget.height
            )  
        )