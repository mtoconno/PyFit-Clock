import math
import time

#initialize start times to zero clock

#init the millisecond counter
startTenthSec = millis() % 1000

#init the minute digit
minInc = 0
oneMin = 0

#init the tens of seconds digit
tenSecInc = 0
tenSec = 0

#init the seconds digit
secInc = 0
oneSec = 0



def setup():
    size(1500, 600)
    global tenInc
    global oneSec
    tenInc = oneSec = 0
    
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

def drawD(xOrigin, yOrigin, size):    
    drawHSegment( xOrigin, yOrigin, size )
    
def drawE(xOrigin, yOrigin, size): 
    #draw segment E
    pushMatrix()
    translate(xOrigin, yOrigin)
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()

def drawC(xOrigin, yOrigin, size):
    #draw segment C
    pushMatrix()
    translate( xOrigin + translateOffset("x", xOrigin, size ), yOrigin )
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()
    
def drawG(xOrigin, yOrigin, size):    
    #draw segment G
    pushMatrix()
    translate( xOrigin + angularOffset( size ), 
              yOrigin - translateOffset( "y", yOrigin, size ) )
    drawHSegment( 0, 0, size )
    popMatrix()

def drawF(xOrigin, yOrigin, size):    
    #draw segment F
    pushMatrix()
    translate( xOrigin + angularOffset( size ), 
              yOrigin - translateOffset( "y", yOrigin, size ) )
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()
 
def drawB(xOrigin, yOrigin, size):
    #draw segment B
    pushMatrix()
    translate( xOrigin + translateOffset("x", xOrigin, size) + angularOffset( size ), 
              yOrigin - translateOffset( "y", yOrigin, size ) )
    rotate( radians( -82 ) ) #rotate 10 degrees
    drawVSegment( 0, 0, size )
    popMatrix()

def drawA(xOrigin, yOrigin, size):
    #draw segment A
    pushMatrix()
    translate( xOrigin + ( 2 * angularOffset( size ) ), 
              yOrigin - translateOffset( "y", yOrigin, size ) -
              translateOffset( "y", yOrigin, size ) )
    drawHSegment( 0, 0, size )
    popMatrix()


def drawPoint(xOrigin, yOrigin, size):
    ellipse(xOrigin, yOrigin, size, size)

def drawSecondsSeperator(xOrigin, yOrigin, size):
    verticalOffset = size * 3
    ellipse(xOrigin, yOrigin - verticalOffset, size, size)
    eSpace = size * 6
    xOffset = math.tan( math.radians(8)) * eSpace
    ellipse(xOrigin + xOffset, yOrigin - verticalOffset - eSpace, size, size)


def drawDigit(xOrigin, yOrigin, size, digit):
    
    if digit == 0:
        drawA(xOrigin, yOrigin, size)
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawD(xOrigin, yOrigin, size)
        drawE(xOrigin, yOrigin, size)
        drawF(xOrigin, yOrigin, size)
    elif digit == 1:
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
    elif digit == 2:
        drawA(xOrigin, yOrigin, size)
        drawB(xOrigin, yOrigin, size)
        drawD(xOrigin, yOrigin, size)
        drawE(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)
    elif digit == 3:
        drawA(xOrigin, yOrigin, size)
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawD(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)
    elif digit == 4:
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawF(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)
    elif digit == 5:
        drawA(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawD(xOrigin, yOrigin, size)
        drawF(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)
    elif digit == 6:
        drawA(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawD(xOrigin, yOrigin, size)
        drawE(xOrigin, yOrigin, size)
        drawF(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)
    elif digit == 7:
        drawA(xOrigin, yOrigin, size)
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
    elif digit == 8:
        drawA(xOrigin, yOrigin, size)
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawD(xOrigin, yOrigin, size)
        drawE(xOrigin, yOrigin, size)
        drawF(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)
    else:
        drawA(xOrigin, yOrigin, size)
        drawB(xOrigin, yOrigin, size)
        drawC(xOrigin, yOrigin, size)
        drawF(xOrigin, yOrigin, size)
        drawG(xOrigin, yOrigin, size)


def draw():
    background(0)
    xOrigin = 500
    yOrigin = 550
    size = 20
    i = 0
    global minInc
    global oneMin
    global tenSecInc
    global tenSec
    global secInc
    global oneSec
 
    #Zero out all the values so clock starts at 00:00.0  
    tenthSec =  millis() % 1000
    # tenthSec = ( 10 + startTenthSec - tenthSec ) % 10 #countdown
    tenthSec = ( 1000 + tenthSec - startTenthSec)
    if tenthSec >= 1000:
        tenthSec = tenthSec - 1000
    tenthSec  = tenthSec // 100
    
    #increment seconds
    if tenthSec == secInc == 0:
        oneSec = oneSec + 1
        secInc = 1
    elif tenthSec != 0:
        secInc = 0

    #increment tens of seconds
    if oneSec == 10 and tenSecInc == 0:
        oneSec = 0
        tenSec = tenSec + 1
        tenSecInc = 1
    elif oneSec != 10:
        tenSecInc = 0
     
    #increment minutes
    if tenSec == 6 and minInc == 0:
        oneSec = 0
        tenSec = 0
        oneMin = oneMin + 1
        minInc = 1
    elif tenSec != 6:
        minInc = 0
        
    
    drawDigit(xOrigin - 400, yOrigin, size, oneMin)
    drawSecondsSeperator(xOrigin - 50, yOrigin, size * 2)
    drawDigit(xOrigin, yOrigin, size, tenSec )
    drawDigit(xOrigin + 300, yOrigin, size, oneSec )
    drawPoint(xOrigin + 600, yOrigin, size * 2)
    drawDigit(xOrigin + 650, yOrigin, size, tenthSec )