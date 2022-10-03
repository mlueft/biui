import sys

sys.path.append('./../')

import biui

biui.init()

themePath = "./../../themes/default/"

lib = biui.ImageLibrary()

img0 = lib.getImage( themePath+"checkbox_checked_bg.png" )

img1 = lib.getI9(themePath+"button_normal_bg",100,100)

lib.debug()

lib.quit()