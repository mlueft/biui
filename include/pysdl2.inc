#ifndef _PYSDL2Definitions_
#define _PYSDL2Definitions_

#define PYSDL2_INIT \
	"""MACROSTART:PYSDL2_INIT"""; \
	sdl2.ext.init( sdl2.SDL_INIT_TIMER ); \
	sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO);\
	sdl2.sdlttf.TTF_Init(); \
	"""MACROEND:PYSDL2_INIT""";

#define PYSDL2_QUIT() \
	"""MACROSTART:PYSDL2_QUIT"""; \
    sdl2.ext.quit(); \
    sdl2.SDL_Quit(); \
	"""MACROEND:PYSDL2_QUIT""";

#define PYSDL2_GET_WINDOWBORDERSIZE(window,size) \
	"""MACROSTART:PYSDL2_GET_WINDOWBORDERSIZE"""; \
	top = ctypes.c_int(); \
	left = ctypes.c_int(); \
	bottom = ctypes.c_int(); \
	right = ctypes.c_int(); \
	sdl2.SDL_GetWindowBordersSize(window,ctypes.byref(top),ctypes.byref(left),ctypes.byref(bottom),ctypes.byref(right)); \
	size = (top.value,left.value,bottom.value,right.value); \
	"""MACROEND:PYSDL2_GET_WINDOWBORDERSIZE""";

#define PYSDL2_CREATEWINDOW(size,window) \
	"""MACROSTART:PYSDL2_CREATEWINDOW"""; \
    window = sdl2.SDL_CreateWindow( None, 100, 100, size[0], size[1], sdl2.SDL_WINDOW_RESIZABLE ); \
	"""MACROEND:PYSDL2_CREATEWINDOW""";

#define PYSDL2_GET_WINDOW_ID(window,var) \
	"""MACROSTART:PYSDL2_GET_WINDOW_ID"""; \
	var = sdl2.SDL_GetWindowID(window); \
	"""MACROEND:PYSDL2_GET_WINDOW_ID""";

#define PYSDL2_SETWINDOWPOS(window,x,y) \
	"""MACROSTART:PYSDL2_SETWINDOWPOS"""; \
	sdl2.SDL_SetWindowPosition(window,x,y); \
	"""MACROEND:PYSDL2_SETWINDOWPOS""";

#define PYSDL2_SETWINDOWPOS(window,x,y) \
	"""MACROSTART:PYSDL2_SETWINDOWPOS"""; \
	sdl2.SDL_SetWindowPosition(window,x,y); \
	"""MACROEND:PYSDL2_SETWINDOWPOS""";

#define PYSDL2_GETWINDOWPOS(window,x,y) \
	"""MACROSTART:PYSDL2_GETWINDOWPOS"""; \
	_x = ctypes.c_int(); \
	_y = ctypes.c_int(); \
	sdl2.SDL_GetWindowPosition(window,ctypes.byref(_x),ctypes.byref(_y)); \
	x = _x.value; \
	y = _y.value; \
	"""MACROEND:PYSDL2_GETWINDOWPOS""";

#define PYSDL2_SETWINDOWSIZE(window,width,height) \
	"""MACROSTART:PYSDL2_SETWINDOWSIZE"""; \
	sdl2.SDL_SetWindowSize(window,width,height); \
	"""MACROEND:PYSDL2_SETWINDOWSIZE""";

#define PYSDL2_SETWINDOWTITLE(window,title) \
	"""MACROSTART:PYSDL2_SETWINDOWTITLE"""; \
	bTitle = title.encode('utf-8'); \
	sdl2.SDL_SetWindowTitle(window,bTitle); \
	"""MACROEND:PYSDL2_SETWINDOWTITLE""";

#define PYSDL2_GETWINDOWSIZE(window,width,height) \
	"""MACROSTART:PYSDL2_GETWINDOWSIZE"""; \
	_width = ctypes.c_int(); \
	_height = ctypes.c_int(); \
	sdl2.SDL_GetWindowSize(window,ctypes.byref(_width),ctypes.byref(_height)); \
	width = _width.value; \
	height = _height.value; \
	"""MACROEND:PYSDL2_GETWINDOWSIZE""";

#define PYSDL2_CREATERENDERER(window,index,flags,renderer) \
	"""MACROSTART:PYSDL2_CREATERENDERER"""; \
	renderer = sdl2.SDL_CreateRenderer(window,index,flags); \
    sdl2.SDL_SetRenderDrawBlendMode(renderer, sdl2.SDL_BLENDMODE_BLEND); \
	"""MACROEND:PYSDL2_CREATERENDERER""";

#define PYSDL2_CREATESURFACE(w,h,surface) \
	"""MACROSTART:PYSDL2_CREATESURFACE"""; \
	surface = sdl2.SDL_CreateRGBSurface( \
		sdl2.SDL_SWSURFACE, \
		w, \
		h, \
		32, \
		0xFF000000, \
		0x00FF0000, \
		0x0000FF00, \
		0x000000FF \
	); \
	sdl2.SDL_SetSurfaceBlendMode(surface, sdl2.SDL_BLENDMODE_BLEND); \
	rect = sdl2.SDL_Rect(0,0,int(w),int(h)); \
	sdl2.SDL_FillRect(surface,rect,0x00000000); \
	"""MACROEND:PYSDL2_CREATESURFACE""";

#define PYSDL2_CREATETEXTURE(renderer,w,h,texture) \
	"""MACROSTART:PYSDL2_CREATETEXTURE"""; \
	texture = sdl2.SDL_CreateTexture( \
		renderer, \
		sdl2.SDL_PIXELFORMAT_RGBA32, \
		sdl2.SDL_TEXTUREACCESS_TARGET, \
		int(w), \
		int(h) \
	); \
	sdl2.SDL_SetTextureBlendMode(texture,sdl2.SDL_BLENDMODE_BLEND); \
	PYSDL2_FILL(renderer,texture,(0,0,0,0)); \
	"""MACROEND:PYSDL2_CREATETEXTURE""";

#define PYSDL2_RENDER_COPY(renderer,texture,srect,trect) \
	"""MACROSTART:PYSDL2_RENDER_COPY"""; \
	src = sdl2.SDL_Rect(int(srect[0]),int(srect[1]),int(srect[2]),int(srect[3])); \
    tgt = sdl2.SDL_Rect(int(trect[0]),int(trect[1]),int(trect[2]),int(trect[3])); \
    sdl2.render.SDL_RenderCopy(renderer,texture,src,tgt); \
	"""MACROEND:PYSDL2_RENDER_COPY""";

#define PYSDL2_RENDER_COPY1(renderer,tTgt,tSrc,tgtRect,srcRect) \
	"""MACROSTART:PYSDL2_RENDER_COPY1"""; \
    _src = sdl2.SDL_Rect(int(srcRect[0]),int(srcRect[1]),int(srcRect[2]),int(srcRect[3])); \
	_tgt = sdl2.SDL_Rect(int(tgtRect[0]),int(tgtRect[1]),int(tgtRect[2]),int(tgtRect[3])); \
	sdl2.SDL_SetRenderTarget(renderer,tTgt); \
	sdl2.SDL_RenderCopy(renderer,tSrc,_src,_tgt); \
	sdl2.SDL_SetRenderTarget(renderer,None); \
	"""MACROEND:PYSDL2_RENDER_COPY1""";

#define PYSDL2_BLIT(tTgt,tSrc,tgtRect,srcRect) \
	"""MACROSTART:PYSDL2_BLIT"""; \
	_src = sdl2.SDL_Rect(int(srcRect[0]),int(srcRect[1]),int(srcRect[2]),int(srcRect[3])); \
	_tgt = sdl2.SDL_Rect(int(tgtRect[0]),int(tgtRect[1]),int(tgtRect[2]),int(tgtRect[3])); \
	sdl2.SDL_BlitScaled(tSrc,_src,tTgt,_tgt); \
	"""MACROEND:PYSDL2_BLIT""";

#define PYSDL2_GETTEXTURESIZE(texture,size) \
	"""MACROSTART:PYSDL2_GETTEXTURESIZE"""; \
	_Width = ctypes.c_int(); \
    _Height = ctypes.c_int(); \
    sdl2.SDL_QueryTexture(texture,None,None,_Width,_Height); \
    size = (0,0,_Width.value,_Height.value); \
	"""MACROEND:PYSDL2_GETTEXTURESIZE""";

#define PYSDL2_GETSURFACESIZE(surface,size) \
	"""MACROSTART:PYSDL2_GETSURFACESIZE"""; \
    size = (0,0,surface.w,surface.h); \
	"""MACROEND:PYSDL2_GETSURFACESIZE""";

#define PYSDL2_FILL(renderer,texture,color)  \
	"""MACROSTART:PYSDL2_FILL"""; \
    tmpT = sdl2.SDL_GetRenderTarget(renderer); \
	sdl2.SDL_SetRenderTarget(renderer,texture); \
	sdl2.render.SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], color[3]); \
	sdl2.render.SDL_RenderClear(renderer); \
	sdl2.SDL_SetRenderTarget(renderer,tmpT); \
	"""MACROEND:PYSDL2_FILL"""

#define PYSDL2_PRESENT(renderer) \
	"""MACROSTART:PYSDL2_PRESENT"""; \
	sdl2.SDL_RenderPresent(renderer); \
	"""MACROEND:PYSDL2_PRESENT""";

#define PYSDL2_SETRENDERCONTEXT(renderer, tTgt) \
	"""MACROSTART:PYSDL2_SETRENDERCONTEXT"""; \
	sdl2.SDL_SetRenderTarget(renderer,tTgt); \
	"""MACROEND:PYSDL2_SETRENDERCONTEXT""";

#define PYSDL2_DRAWRECT(renderer,texture,color,rect) \
	"""MACROSTART:PYSDL2_DRAWRECT"""; \
	tmpT = sdl2.SDL_GetRenderTarget(renderer); \
	sdl2.SDL_SetRenderTarget(renderer,texture); \
	sdl2.render.SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], color[3]); \
	_rect = sdl2.SDL_Rect(int(rect[0]),int(rect[1]),int(rect[2]),int(rect[3])); \
	sdl2.SDL_RenderDrawRect(renderer,_rect); \
	sdl2.SDL_SetRenderTarget(renderer,tmpT); \
	"""MACROEND:PYSDL2_DRAWRECT""";

#define PYSDL2_DRAWRECTFILLED(renderer,texture,color,rect) \
	"""MACROSTART:PYSDL2_DRAWRECTFILLED"""; \
	tmpT = sdl2.SDL_GetRenderTarget(renderer); \
	sdl2.SDL_SetRenderTarget(renderer,texture); \
	sdl2.render.SDL_SetRenderDrawColor(renderer, color[0], color[1], color[2], color[3]); \
	_rect = sdl2.SDL_Rect(int(rect[0]),int(rect[1]),int(rect[2]),int(rect[3])); \
	sdl2.SDL_RenderFillRect(renderer,_rect); \
	sdl2.SDL_SetRenderTarget(renderer,tmpT); \
	"""MACROEND:PYSDL2_DRAWRECTFILLED""";

#define PYSDL2_LOAD_IMG(fileName,renderer, img) \
	"""MACROSTART:PYSDL2_LOAD_IMG"""; \
	img = sdl2.ext.load_img(fileName); \
	"""MACROEND:PYSDL2_LOAD_IMG""";

#define PYSDL2_DESTROYWINDOW(subject) \
	"""MACROSTART:PYSDL2_DESTROYWINDOW"""; \
	sdl2.SDL_DestroyWindow(subject); \
	"""MACROEND:PYSDL2_DESTROYWINDOW""";

#define PYSDL2_DESTROYRENDERER(subject) \
	"""MACROSTART:PYSDL2_DESTROYRENDERER"""; \
	sdl2.SDL_DestroyWindow(subject); \
	"""MACROEND:PYSDL2_DESTROYRENDERER""";

#define PYSDL2_DESTROYTEXTURE(subject) \
	"""MACROSTART:PYSDL2_DESTROYTEXTURE"""; \
	sdl2.SDL_DestroyTexture(subject); \
	"""MACROEND:PYSDL2_DESTROYTEXTURE""";

#define PYSDL2_DESTROYIMAGE(subject) \
	"""MACROSTART:PYSDL2_DESTROYIMAGE"""; \
	sdl2.SDL_DestroyImage(subject); \
	"""MACROEND:PYSDL2_DESTROYIMAGE""";

#endif
