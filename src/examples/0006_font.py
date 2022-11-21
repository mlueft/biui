import sys
from _cffi_backend import typeof

sys.path.append('./../')

import biui

biui.init()

print("font folders:")
for f in biui.getFontFolders():
    print("    "+f)
    
print("fonts:")
for s in biui.getFonts():
    print( "    "+s[0] )

print("default font:")
print( biui.getDefaultFont() )

text = "hello world!"
color = biui.Color(255,255,255,0)
font = biui.Font(
    biui.getDefaultFont(),
    20
)

print ("font:")
print(font)

print( "familyName  : "+ font.familyName )
print( "styleName   : "+ font.styleName )
print( "ascent      : "+ str(font.ascent) )
print( "descent     : "+ str(font.descent) )
print( "size        : "+ str(font.size) )
print( "lineSpacing : "+ str(font.lineSpacing))
print( "hinting     : "+ str(font.hinting))
print( "kerning     : "+ str(font.kerning))
print( "style       : "+ str(font.style))
print( "outline     : "+ str(font.outline))
print( "alignment   : "+ str(font.alignment))
print( "direction   : "+ str(font.direction))
print( "renderSize  : ", text, font.getRenderSize(text) )
print( "measure     : ", font.measure(text,50) )

##texture = font.render(text,color)

##font.styleName = "foo"
##font.familyName = "Bold"
##font.ascent = 10
##font.descent = -20
font.size = 30
##font.lineSpacing = 35
font.hinting = 1
font.kerning = True
font.style = 2 # BOLD
font.outline = 2
font.alignment = 1
font.direction = 1


print( "familyName  : "+ font.familyName )
print( "styleName   : "+ font.styleName )
print( "ascent      : "+ str(font.ascent) )
print( "descent     : "+ str(font.descent) )
print( "size        : "+ str(font.size) )
print( "lineSpacing : "+ str(font.lineSpacing))
print( "hinting     : "+ str(font.hinting))
print( "kerning     : "+ str(font.kerning))
print( "style       : "+ str(font.style))
print( "outline     : "+ str(font.outline))
print( "alignment   : "+ str(font.alignment))
print( "direction   : "+ str(font.direction))
print( "renderSize  : ", text, font.getRenderSize(text) )
print( "measure     : ", font.measure(text,50) )

##texture = font.render(text,color)


print("fertig")
