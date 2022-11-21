import sys
import unittest
sys.path.append('./../') ## needed if the file is tested.
sys.path.append('./')    ## needed if the folder is tested.
import biui


class FontTestCase(unittest.TestCase):
    
    def setUp(self):
        biui.init()
        
 
    def tearDown(self):
        ## biui.quit()
        pass
    
    def testFamilyName(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )

        """test Font.familyName"""
        assert subject.familyName == "Ostrich Sans", "font.familyName can't be read."
        
        subject.close()
    

    def testStyleName(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.StyleName"""
        assert subject.styleName == "Medium", "font.styleName can't be read."
        
        subject.close()

    def testAscent(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        """test Font.ascent"""
        assert subject.ascent == 15, "font.ascent can't be read."
        
    def testDescent(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        """test Font.descent"""
        assert subject.descent == -5, "font.descentascent can't be read."
        subject.close()

    def testSize0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.size"""
        assert subject.size == 20, "font.size can't be read."
        subject.close()

    def testSize1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        subject.size = 31
        
        """test Font.size"""
        assert subject.size == 31, "font.size can't be set."
        subject.close()

    def testLineSpacing(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.lineSpacing"""
        assert subject.lineSpacing == 20, "font.lineSpacing can't be read."
        subject.close()

    def testHinting0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        
        """test Font.hinting"""
        assert subject.hinting == biui.Hinting.NORMAL, "font.hinting can't be read."
        subject.close()

    def testHinting1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        subject.hinting = biui.Hinting.LIGHT
        """test Font.hinting"""
        assert subject.hinting == biui.Hinting.LIGHT, "font.hinting can't be set."
        subject.close()
        
    def testKerning0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.kerning"""
        assert subject.kerning == True, "font.kerning can't be read."
        subject.close()
        
    def testKerning1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        subject.kerning = False
        
        """test Font.kerning"""
        assert subject.kerning == False, "font.kerning can't be set."
        subject.close()

    def testKerning2(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        subject.kerning = True
        
        """test Font.kerning"""
        assert subject.kerning == True, "font.kerning can't be set."
        subject.close()
        
    def testStyle0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.style"""
        assert subject.style == biui.Style.NORMAL, "font.style can't be set."
        subject.close()
                
    def testStyle1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        value = biui.Style.BOLD | biui.Style.ITALIC
        
        subject.style = value
        
        """test Font.style"""
        assert subject.style == value, "font.style can't be read."
        subject.close()
        
    def testOutline0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.outline"""
        assert subject.outline == 0, "font.outline can't be read."
        subject.close()
        
    def testOutline1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        subject.outline = 11
        
        """test Font.outline"""
        assert subject.outline == 11, "font.outline can't be set."
        subject.close()
        
    def testAlignment0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        ##TODO: Use ENUM-Class
        """test Font.alignment"""
        assert subject.alignment == 0, "font.alignment can't be read."
        subject.close()
        
    def testAlignment1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        subject.alignment = 2
        ##TODO: Use ENUM-Class
        """test Font.alignment"""
        assert subject.alignment == 2, "font.alignment can't be set."
        subject.close()        
        
    def testdirection0(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        """test Font.direction"""
        assert subject.direction == biui.Direction.LTR, "font.direction can't be read."
        subject.close()
        
    def testdirection1(self):
        
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        subject.direction = biui.Direction.TTB
        """test Font.direction"""
        assert subject.direction == biui.Direction.TTB, "font.direction can't be set."
        subject.close()
        
    def testGetRenderSize0(self):
        
        text = "hello world!"
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        result = subject.getRenderSize( text )
        
        """test Font.getRenderSize"""
        assert result == (78,20), "font.getRenderSize can't be read."
        subject.close()
        
    def testMeasure0(self):
        
        text = "hello world!"
        width = 50
        subject = biui.Font(
            "../../fonts/ostrich-sans-regular.ttf",
            20
        )
        
        result = subject.measure( text, width )
        
        """test Font.measure"""
        assert result == (7,49), "font.measure can't be read."
        subject.close()        
        
    ## TODO: Test render function()
    ## TODO: Test close()
    
if __name__ == "__main__":
    unittest.main() ## run all tests