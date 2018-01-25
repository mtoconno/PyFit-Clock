import math

def setup():
    size(1500, 1500)
    
def returnOffset( XorY, size, degrees ):
    if XorY == "x":
        return size * math.tan( math.radians( degrees ) )
    elif XorY == "y":
        return size
    else:
        print "ERROR"
        return 0
    
def translateOffset( XorY, origin, size ):
    if XorY == "x":
        offset = returnOffset( "x", size, 49 ) + returnOffset( "x", size, 41 ) + ( size * 10 )
        return offset
    elif XorY == "y":
        offset = size * 12 #size * 10 + size + size
        offset = math.cos( math.radians( 8 ) ) * ( returnOffset( "x", size, 41 ) +
                          returnOffset( "x", size, 49 ) + ( size * 10 ) )
        return offset
    else:
        print "ERROR"
        return 0
    
def angularOffset( size ):
    #calculate the offset required because the segment is at an angle
    # size/5 adds padding to make it align nicer
     return returnOffset( "x", size, 49 ) + size / 2

def drawHSegment( x, y, size ):
    #x, y shall be left-most vertex point of a horizontal
    #segment. rotation and scaling are defined in draw
    #[x,y]Offset is the offset for the triangluar portion
    #x1, y1 are going left to right from x, y
    #hOffset is the offset for the rectangular portion
    
    x1Offset = returnOffset("x", size, 41 )
    y1Offset = returnOffset("y", size, 41 )
    
    x2Offset = returnOffset( "x", size, 49 )
    y2Offset = returnOffset( "y", size, 49 ) 
    
    hOffset = size * 10
    fill(255, 0, 0)
    beginShape()
    vertex(x, y)
    vertex(x + x1Offset, y + y1Offset)
    vertex(x + x1Offset + hOffset, y + y1Offset)
    vertex(x + x1Offset + x2Offset + hOffset, y)
    vertex(x + x2Offset +hOffset, y - y2Offset)
    vertex(x + x2Offset, y - y2Offset)
    endShape(CLOSE)
    
    
def drawVSegment( x, y, size ):
    #x, y shall be left-most vertex point of a horizontal
    #segment. rotation and scaling are defined in draw
    #[x,y]Offset is the offset for the triangluar portion
    #x1, y1 are going left to right from x, y
    #hOffset is the offset for the rectangular portion
    
    x1Offset = returnOffset("x", size, 49 )
    y1Offset = returnOffset("y", size, 49 )
    
    x2Offset = returnOffset( "x", size, 41 )
    y2Offset = returnOffset( "y", size, 41 )  
    
    hOffset = size * 10
    fill(255, 0, 0)
    beginShape()
    vertex(x, y)
    vertex(x + x1Offset, y + y1Offset)
    vertex(x + x1Offset + hOffset, y + y1Offset)
    vertex(x + x1Offset + x2Offset + hOffset, y)
    vertex(x + x2Offset +hOffset, y - y2Offset)
    vertex(x + x2Offset, y - y2Offset)
    endShape(CLOSE)
    



def draw():
    #draw segment D
    xOrigin = 200
    yOrigin = 1300
    size = 50
    drawHSegment( xOrigin, yOrigin, size )

    #draw segment E
    pushMatrix()
    translate(xOrigin, yOrigin)
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()

    #draw segment C
    pushMatrix()
    translate( xOrigin + translateOffset("x", xOrigin, size ), yOrigin )
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()
    
    #draw segment G
    pushMatrix()
    translate( xOrigin + angularOffset( size ), 
              yOrigin - translateOffset( "y", yOrigin, size ) )
    drawHSegment( 0, 0, size )
    popMatrix()
    
    #draw segment F
    pushMatrix()
    translate( xOrigin + angularOffset( size ), 
              yOrigin - translateOffset( "y", yOrigin, size ) )
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()
    
    #draw segment B
    pushMatrix()
    translate( xOrigin + translateOffset("x", xOrigin, size) + angularOffset( size ), 
              yOrigin - translateOffset( "y", yOrigin, size ) )
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()

    #draw segment A
    pushMatrix()
    translate( xOrigin + ( 2 * angularOffset( size ) ), 
              yOrigin - translateOffset( "y", yOrigin, size ) -
              translateOffset( "y", yOrigin, size ) )
    drawHSegment( 0, 0, size )
    popMatrix()
    '''