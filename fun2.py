import turtle
turtle.goto(0,0)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = None

def up():
    global direction
    direction = UP
    print("You pressed the up key.")
    on_move()

def down():
    global direction
    direction = DOWN
    print("You pressed the down key.")
    on_move()

def left():
    global direction
    direction = LEFT
    print("You pressed the left key.")
    on_move()

def right():
    global direction
    direction = RIGHT
    print("You pressed the right key.")
    on_move()

turtle.listen()    
turtle.onkey(up, "Up")
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')



def on_move():
    xChange = 50
    yChange = 50
    x,y = turtle.pos()
    if direction == UP:
        turtle.goto(x,y + yChange)
    if direction == DOWN:
        turtle.goto(x,y - yChange)
    if direction == RIGHT:
        turtle.goto(x + xChange,y)
    if direction == LEFT:
        turtle.goto(x - xChange,y)
        
    




    
    
    

'''
def on_move():
    xChange = 100
    yChange = 0
    x, y = turtle.position()
    newyup = y + yChange
    newydown = y - yChange
    newxright = xChange + x
    newxleft = xChange-x
    if up() :
        turtle.goto(x,newyup)
    if down() :
        turtle.goto(x,newydown)
    if right() :
        turtle.goto(newxright,y)
    if left() :
        turtle.goto(newxleft,y)


on_move()
'''
