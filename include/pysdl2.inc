#ifndef _PYSDL2Definitions_
#define _PYSDL2Definitions_

#define PYSDL2_INIT \
	sdl2.ext.init(); \
	sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO);\
	sdl2.sdlttf.TTF_Init();

#define PYSDL2_GET_WINDOW_ID(window) \
	sdl2.SDL_GetWindowID(window)

#define PYSDL2_RENDER_COPY(renderer,texture,srect,trect) \
    src = sdl2.SDL_Rect(int(srect[0]),int(srect[1]),int(srect[2]),int(srect[3])); \
    tgt = sdl2.SDL_Rect(int(trect[0]),int(trect[1]),int(trect[2]),int(trect[3])); \
    sdl2.render.SDL_RenderCopy(renderer,texture,src,tgt);

#define PYSDL2_FILL(renderer,texture,color)  \
	tmpT = sdl2.SDL_GetRenderTarget(renderer); \
	sdl2.SDL_SetRenderTarget(renderer,texture); \
	sdl2.render.SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], color[3]); \
	sdl2.render.SDL_RenderClear(renderer); \
	sdl2.SDL_SetRenderTarget(renderer,tmpT);

#define PYSDL2_SETWINDOWPOS(window,x,y) \
	sdl2.SDL_SetWindowPosition(window,x,y)

#define PYSDL2_PRESENT(renderer) \
	sdl2.SDL_RenderPresent(renderer)

#define PYSDL2_SETWINDOWPOS(window,x,y) \
	sdl2.SDL_SetWindowPosition(window,x,y)

#define PYSDL2_SETWINDOWSIZE(window,width,height) \
	sdl2.SDL_SetWindowSize(window,width,height)

#define PYSDL2_SETWINDOWTITLE(window,title) \
	bTitle = title.encode('utf-8'); \
	sdl2.SDL_SetWindowTitle(window,bTitle)

#define PYSDL2_GETWINDOWSIZE(window,width,height) \
	_width = ctypes.c_int(); \
	_height = ctypes.c_int(); \
	sdl2.SDL_GetWindowSize(window,ctypes.byref(_width),ctypes.byref(_height)); \
	width = _width.value; \
	height = _height.value;










#endif
