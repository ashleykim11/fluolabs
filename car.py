x = 50
xSpeed = 1
def setup():
    #size(800, 800)
    fullScreen()
    
def draw(): 
    global x   
    background(0)
    fill(random(255), 0, 0)
    rect(x, height/2, 150, 75)
    x = x + xSpeed
    
    # display x on top
    fill(255)
    text("x: " + str(x) + "xSpeed:" + str(xSpeed), width/2, 32)
    
def mousePressed():
    global xSpeed


    # check mouseX
    if ( (mouseX > x) and (mouseX < x + 150)):    # horizantal
        if (( mouseY > height/2) and (mouseY < height/2 + 75)):
            xSpeed = xSpeed * -1
            if (xSpeed > 0):
                xSpeed = xSpeed + 1
            else:
                xSpeed = xSpeed - 1
    

    print(mouseX)
