# BIUI stands for blender inspired user interface.

## General
I love blender's UI so much, I have to do this.
I want to thank all people working on blender,
it's such a masterpeace!

This work is based on UX/UI of blender.
I am not into blender's source code.
So, i may do thing the "wrong" way in software design.

## Current status
This project is in early development and structure of the source files is changing
permanently.

## Development
This project uses gcc as a preprocessor for python files. See my ppp repository:

https://github.com/mlueft/ppp

This lib depends on pysdl2. I want to keep the lib in 
python, i hope it's not going to be laggy.

DONE:
* Button
* ToggleButton
* Buttongroup
* Label
* FlexGrid (Blender's window layout management)
* NumberSlider
* Progressbar
* TextField
* MenuBar/TopBar
* StatusBar
* Scrollbar

TODO:

* stopPropagation() for keyboardevents? Should it have it?
* Protect setter from unnecassary invalidate() calles.
* Label
  + format for pre/postfix
* Checkbox
* TextField Mouse interaction
* Combobox
* TreeView
* ListView
* IconBar(3D-View left side)
* LayoutManager

Bugs:
 * Menuitems are not resized to text length
 * Tool tips are not resized to text length
 * Sometimes the Layoutmanagemant doesn't redraw everything
   This comes from the DirtyRectangleManager and overlapped widgets
   doen't redraw
 * Resized flexgrids loses control over splitter and panels.
 * Icons
 * NumberSlider should have properties to enable/disable manual input
 * Icon/Menubar needs control buttons to control out of view content
 * Tabnavigator
 
```python

```
## License:

### Font:
The font 'ostrich sans' is delivered with biui. The font is an open source font provided by
'The League of Moveable Type'. For more information please take a look at: https://github.com/theleagueof/ostrich-sans/

