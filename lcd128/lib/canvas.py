def raiseError(*a, **k):
    raise NotImplementedError()


#@micropython.native
def clamp( aValue, aMin, aMax ) :
  return max(aMin, min(aMax, aValue))
  
  
class Canvas:

    width=128
    height=64
    clear = raiseError
    plot = raiseError
    redraw = raiseError
#    create_plotter = raiseError

    def line(self, x1, y1, x2, y2, set=True):
        diffX = abs(x2 - x1)
        diffY = abs(y2 - y1)
        shiftX = 1 if (x1 < x2) else -1
        shiftY = 1 if (y1 < y2) else -1
        err = diffX - diffY
        while True:
            self.plot(x1, y1, set=True)
            if x1 == x2 and y1 == y2:
                break
            err2 = 2 * err
            if err2 > -diffY:
                err -= diffY
                x1 += shiftX
            if err2 < diffX:
                err += diffX
                y1 += shiftY

###################################################################

    def fill_rect(self, x1, y1, x2, y2,  set=True):
        for y in range(y1, y2):
            self.line(x1, y, x2, y,  set=True)

    def rect(self, x1, y1, x2, y2,  set=True):
        self.line(x1, y1, x2, y1,  set=True)
        self.line(x2, y1, x2, y2,  set=True)
        self.line(x2, y2, x1, y2,  set=True)
        self.line(x1, y2, x1, y1,  set=True)
            
###################################################################
    def fillrect(self, x1, y1, aSize):
    
#        aStart = (x1,y1)
#        start = (clamp(aStart[0], 0, self._size[0]), clamp(aStart[1], 0, self._size[1]))
#        end = (clamp(start[0] + aSize[0] - 1, 0, self._size[0]), clamp(start[1] + aSize[1] - 1, 0, self._size[1]))

#        if (end[0] < start[0]):
#        	tmp = end[0]
#        	end = (start[0], end[1])
#        	start = (tmp, start[1])
#        if (end[1] < start[1]):
#        	tmp = end[1]
#        	end = (end[0], start[1])
#        	start = (start[0], tmp)
        	
#	x1 = start[0]
#	y1 = start[1]
#	x2 = end[0]
#	y2 = end[1]
#	print("x1")
#	print(x1)
		
    	# self.fill_rect(x1, y1, x2, y2, False)
    	self.plot(x1, y1, set=True)
        
###################################################################
        
#   @micropython.native
    def char( self, aPos, aChar, aFont, aSizes, nowrap = False ) :
    	# '''Draw a character at the given position using the given font and color.
    	# aSizes is a tuple with x, y as integer scales indicating the
    	# of pixels to draw for each pixel in the character.'''

        if aFont == None:
        	return

        startchar = aFont['Start']
        endchar = aFont['End']

        ci = ord(aChar)
        if (startchar <= ci <= endchar):
        	fontw = aFont['Width']
        	fonth = aFont['Height']
        	ci = (ci - startchar) * fontw

        charA = aFont["Data"][ci:ci + fontw]
        px = aPos[0]

	for c in charA :
        	py = aPos[1]
        	for r in range(fonth) :
        		if c & 0x01 :
        			self.fillrect(px, py, aSizes)
        		py += aSizes[1]
        		c >>= 1
        	px += aSizes[0]

###################################################################


#   @micropython.native
    def text( self, aPos, aString, aFont, aSize = 1, nowrap = False ) :
#    '''Draw a text at the given position.  If the string reaches the end of the
#       display it is wrapped to aPos[0] on the next line.  aSize may be an integer
#       which will size the font uniformly on w,h or a or any type that may be
#       indexed with [0] or [1].'''

    	if aFont == None:
    		return

    	#Make a size either from single value or 2 elements.
    	if (type(aSize) == int) or (type(aSize) == float):
    		wh = (aSize, aSize)
    	else:
    		wh = aSize

    	px, py = aPos
    	width = wh[0] * aFont["Width"] + 1
    	for c in aString:
    		self.char((px, py), c, aFont, wh)
    		px += width
    		#We check > rather than >= to let the right (blank) edge of the
    		# character print off the right of the screen.
    		if px + width > self._size[0]:
	    		if nowrap:
	    			break
	    		else:
	    			py += aFont["Height"] * wh[1] + 1
	    			px = aPos[0]

###################################################################


