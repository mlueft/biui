#ifndef _BIUICONFIG_
#define _BIUICONFIG_

// Shows the update regions in all windows
// Remove leading underscore to activate
#define _SHOW_UPDATE_BOX

//
//
#define _SHOW_FUNCTIONNAMES

// Time in seconds
#define BIUI_CLICKDURATION 0.25

// Has to be even
// Size of the spacer between flexpanes
#define BIUI_FLEXGRID_SPACER_WIDTH 3
// Size of the Dragraster in Flecgrid
#define BIUI_FLEXGRID_RASTERSTEP 5

#define BIUI_FLEXGRID_CORNER_SIZE 10

#define BIUI_THEMEFOLDER "themes"

// Control of the image chache
#define BIUI_CACHE_IMAGES_SCALED True
#define BIUI_CACHE_IMAGES_ORIGINAL True
#define BIUI_CACHE_IMAGES_I9 True

// Error messages
#define BIUI_ERR_CLASS_NOT_INIT "This class is not meant to be instantiated!"
#define BIUI_ERR_COL_INDEX_OUT_OF_RANGE "Column index out of range!"
#define BIUI_ERR_ROW_INDEX_OUT_OF_RANGE "Row index out of range!"
#define BIUI_ERR_FLEXGRID_ADDCHILD "FlexGrid.addChild: Use addFlexPane() instead!"
#define BIUI_ERR_FLEXGRID_REMOVECHILD "FlexGrid.removeChild: Use removeFlexPane() instead!"
#define BIUI_ERR_MENUBAR_ADDCHILD "Menubar.addChild: Use addItem() instead!"
#define BIUI_ERR_MENUBAR_REMOVECHILD "Menubar.removeChild: Use removeItem() instead!"
#define BIUI_ERR_MENUPANE_ADDCHILD "MenuPane.addChild: Use addItem() instead!"
#define BIUI_ERR_MENUPANE_REMOVECHILD "MenuPane.removeChild: Use removeItem() instead!"
#define BIUI_ERR_PROPERTY_NOT_EXISIS "This Property doesn't exist!"
#define BIUI_ERR_DEL_ATTR_NOT_ALLOWED "It is not allowed to delete attributes."

#define FUNCTIONEND #pass

#endif
