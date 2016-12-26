#Ibrahim ERGIN 130709019
#Huseyin CAKIR 130709025
import turtle
import random
import time
#import sound
NIM=input( "What is your Name?")
print(NIM)
#sounds=sound.sounds
color = ["yellow", "green", "red", "orange", "purple","Gold","Darkred","Cyan" ]


# Group Members: (fill this part with your name(s) and number(s)

cell_size = 27  # keep it odd
width = 11
height = 9
bg_color = "gray"   # background color
wall_color = "black"

# directions
(UP, DOWN, LEFT, RIGHT, STAND) = (1,2,3,4,5)
dir_updates = { UP:(0,1), DOWN:(0,-1), LEFT:(-1,0), RIGHT: (1,0) }

wn = turtle.Screen()
wn.bgcolor(bg_color)
wn.title("Maze")
wn.setup(910,710)
wn.screensize(900,700)


s_cr=turtle.Turtle()     #Score turtle
s_cr.penup()
s_cr.hideturtle()
s_cr.color("blue")
s_cr.goto(170,-305)
score1 = 0

mariol=turtle.Turtle()   #Lives turtle
mariol.penup()
mariol.hideturtle()
mariol.goto(-170,-305)

tenergy=turtle.Turtle()    #to write the left enery turtle
tenergy.penup()
tenergy.hideturtle()
tenergy.color("red")
tenergy.goto(-170,285)




def cell_to_coord(row, col, top_left = False):
    """ Returns the midpoint (or top_left corner) of the cell as screen
         coordinates """
    global cell_size
    x = row * cell_size
    y = col * cell_size
    if (top_left):
        x -= cell_size / 2
        y += cell_size / 2
    return (x,y)

def fill_rect(t,x,y,w,h):
    """ Makes turtle t to draw a filled rectangle where
        (x,y) is the top left corner, w is the width,
        h is the height """
    t.goto(x,y)
    t.begin_fill()
    t.goto(x+w,y)
    t.goto(x+w,y-h)
    t.goto(x,y-h)
    t.goto(x,y)
    t.end_fill()

def item_key(i,j):
    return "(" + str(i) + "," + str(j) + ")"

def drawer_write(message):
    (x,y) = cell_to_coord(0,height+1)
    y += cell_size / 2
    drawer.goto(x,y)
    drawer.write(message, font=("Arial", 12, "normal"), align="center")

def check_wall(i,j):
    """ returns True if this coordinate is an inner or outer wall
        otherwise returns False """
    global width, height, wall_coords
    return (abs(i) == width + 1)   or \
           (abs(j) == height + 1)  or \
           (i,j) in wall_coords

drawer = turtle.Turtle()
drawer.fillcolor(wall_color)
drawer.speed(0)
drawer.hideturtle()
drawer.penup()

# draw the borders of the maze
short_side = cell_size
long_side_w = (2*width+3)*cell_size
long_side_h = (2*height+3)*cell_size
(x,y) = cell_to_coord(-width-1, height+1, True)
fill_rect(drawer,x,y,short_side, long_side_h)
fill_rect(drawer,x,y,long_side_w,short_side)
(x,y) = cell_to_coord(-width-1, -height-1, True)
fill_rect(drawer,x,y,long_side_w,short_side)
(x,y) = cell_to_coord(width+1, height+1, True)
fill_rect(drawer,x,y,short_side,long_side_h)

rng = random.Random()

mario = { 'turtle': turtle.Turtle(), 'i':0, 'j':0, 'dir': STAND, 'score':0, 'lives':3}
mario['turtle'].shape('turtle')
mario['turtle'].shapesize(0.7, 0.7)
mario['turtle'].penup()
mario['turtle'].color("black", "blue")

# global variables needed in different functions
items = {}
wall_coords = []
bad_turtles = []
apple_coords = []

def init_game():
    global items, wall_coords, bad_turtles,apple_coords
    items = {}
    wall_coords = []
    item_coords = []
    apple_coords = []
    drawer.color("black", "darkgreen")
    drawer.shape("circle")
    drawer.shapesize(0.8, 0.8)


    ibo=len(apple_coords)

    #Here the apples have random x and y
    while ( ibo < 5):
       i = rng.randint(-width+1, width-1)
       j = rng.randint(-height+1, height-1)
       if ((i == 0 and j == 0) or (i,j) in (wall_coords + item_coords)): continue
       else:
          apple_coords.append((i,j))
          ibo += 1

    for (i,j) in apple_coords:
        (x,y) = cell_to_coord(i,j)
        drawer.goto(x,y)
        stamp_id = drawer.stamp()
        item_coords.append((i,j))
        items[item_key(i,j)] = {'type':'apple', 'stamp': stamp_id}

    print("Items",items)

    #draw inner walls
    wall_count = 0
    while (wall_count < 5):
       i = rng.randint(-width+1, width-1)
       j = rng.randint(-height+1, height-1)
       if ((i == 0 and j == 0) or (i,j) in (wall_coords + item_coords)): continue
       else:
          wall_coords.append((i,j))
          wall_count += 1

    # print("Walls:",wall_coords)

    drawer.color(wall_color)
    for (i,j) in wall_coords:
        (x,y) = cell_to_coord(i,j,top_left=True)
        fill_rect(drawer, x,y,cell_size, cell_size)

    filled_coords = wall_coords + apple_coords + [(0,0)]
    bad_turtles = []
    while (len(bad_turtles) < 4):
       i = rng.randint(-width+1, width-1)
       j = rng.randint(-height+1, height-1)
       if (i,j) in filled_coords: continue
       else:   # found an empty cell
          new_color={}
          new_color['color'] = random.choice(color)
          new_turtle = turtle.Turtle()
          new_turtle.shape('turtle')
          new_turtle.shapesize(0.7, 0.7)
          new_turtle.penup()

          new_turtle.color(new_color['color'])
          (x,y) = cell_to_coord(i,j)
          new_turtle.goto(x,y)
          bad_turtle = { 'turtle': new_turtle, 'i':i, 'j':j }
          bad_turtle['dir'] = rng.choice([UP,DOWN,LEFT,RIGHT])


          bad_turtles.append(bad_turtle)
          filled_coords.append((i,j))





    drawer_write("Mario: {}, {}".format(mario['i'], mario['j']))





s_cr.goto(171,-306)   #the code is  misleading for  using undo


def score_write():
   global score1,apple_coords
   s_cr.undo()
   s_cr.write("SCORE = {}".format(score1),
       font=("Arial", 12, "normal"), align="left")

   score1 += 10


mariol.goto(-171,-306)    #the code is  misleading for  using undo
def mario_life():
        mario['lives']=mario['lives']-1
        mariol.undo()
        mariol.write("LIVES = {}".format(mario['lives']),
         font=("Arial", 12, "normal"), align="right")



ct=10

tenergy.goto(-171,306)    #the code is  misleading for  using undo
def mario_energy():
    global ct
    tenergy.undo()

    ct=ct-2

    tenergy.write("Energy  {}".format("I"*ct),
         font=("Arial", 14, "normal"), align="right")
    if mario['lives']==0 or len(items) == 0:
            ct=0
            tenergy.undo()
            tenergy.color("black")

            tenergy.color("black")


    if ct==0:
        mario_life()
        ct=8




#at the end of the game if all apples are collected player(NIM) will see  this screen
#also score depends on the left lives. For every left lives + 20 point.
def game_won():
    global score1
    wn.bgcolor("black")
    drawer.color("red")
    score1 = score1-10
    drawer.goto(0,0)
    drawer.write("Congratulations!!! {} :)\nYour SCORE = {}".format(NIM,score1+(mario['lives']*20)), font=("Times", 40, "normal"), align="center")
    drawer.goto(0,-50)
    drawer.write("Left LIVES = {}".format(mario['lives']), font=("Times", 20, "normal"), align="center")
    drawer.goto(0,-180)
    drawer.write("Copyleft 2015 Huseyin Cakir & Ibrahim Ergin\nPress 'q' for quit.", font=("Heveltica", 15, "normal"), align="center")
    if len(items)==0:
        wn.onkey(quit_game,"q")
       # sound.beep(sounds[1])



#at the end of the game if player dont have any live player(NIM) will see  this screen
def game_lost():
    global score1
    wn.bgcolor("black")
    drawer.color("red")
    score1 = score1-10
    drawer.goto(0,0)
    drawer.write("DEFEAT! {} :(\nYour SCORE = {}".format(NIM,score1), font=("Times", 50, "normal"), align="center")
    drawer.goto(0,-180)
    drawer.write("Copyleft 2015 Huseyin Cakir & Ibrahim Ergin\nPress 'q' for quit.", font=("Helvetica", 15, "normal"), align="center")
    if mario['lives']==0:
        wn.onkey(quit_game,"q")
        #sound.beep(sounds[3])







def quit_game():
     wn.bye()
     #sound.beep(sounds[4])


def turn_left():
   mario['dir'] = LEFT

def turn_right():
   mario['dir'] = RIGHT

def turn_up():
   mario['dir'] = UP

def turn_down():
   mario['dir'] = DOWN

def set_direction(bad_turtle):

    prob = rng.uniform(0,100)
    if 60 < prob < 80:
        bad_turtle['dir'] = rng.choice([UP,DOWN,LEFT,RIGHT])
    elif prob >= 80:  # turn towards mario
        (i1,j1) = (mario['i'], mario['j'])
        (i2,j2) = (bad_turtle['i'], bad_turtle['j'])
        p = rng.randint(1,2)
        if p == 1:
           if (i1 < i2): bad_turtle['dir'] = LEFT
           elif (i1 > i2): bad_turtle['dir'] = RIGHT
        else:
           if (j1 < j2): bad_turtle['dir'] = DOWN
           elif (j1 > j2): bad_turtle['dir'] = UP

def move_turtle(maze_turtle):
   """ Moves the turtle according to the latest direction if not facing a wall
       at the next step. Returns True if turtle moved successfully otherwise
       returns False """
   global UP, DOWN, LEFT, RIGHT, STAND
   if (maze_turtle['dir'] == STAND):
      return False
   else:
       old_heading = maze_turtle['turtle'].heading()
       if (maze_turtle['dir'] == LEFT): new_heading = 180
       elif (maze_turtle['dir'] == RIGHT): new_heading = 0
       elif (maze_turtle['dir'] == UP): new_heading = 90
       else: new_heading = 270
       if (old_heading != new_heading):  # turn maze_turtle
          old_speed = maze_turtle['turtle'].speed()
          maze_turtle['turtle'].speed(0)  # turn off animation
          maze_turtle['turtle'].setheading(new_heading)
          maze_turtle['turtle'].speed(old_speed)
       # determine new cell assuming maze_turtle can move
       (i1,j1) = (maze_turtle['i'], maze_turtle['j'])
       (offset_i,offset_j) = dir_updates[maze_turtle['dir']]
       (i2,j2) = (i1+offset_i,j1+offset_j)
       if not check_wall(i2,j2):
          maze_turtle['turtle'].forward(cell_size)
          maze_turtle['i'] = i2
          maze_turtle['j'] = j2
          return True
       else:  # maze_turtle can't move
          maze_turtle['dir'] = STAND
          return False

def update():
   moved = move_turtle(mario)
   global score1
   if moved:
      (i1,j1) = (mario['i'], mario['j'])
      drawer.undo()   # clear the previous message written
      drawer_write("Mario: {}, {}".format(i1, j1))
      item = items.get(item_key(i1,j1))

      if item != None:   # there is an item at this coordinate

         print(item["type"] + " eaten")
         stamp_id = item["stamp"]
         drawer.clearstamp(stamp_id)
         del items[item_key(i1,j1)]
         score_write()
         #sound.beep(sounds[0])
      for bad_turtle in bad_turtles:
         (i2,j2) = (bad_turtle['i'], bad_turtle['j'])
         if i1==i2 and j1==j2: # mario is at the same cell with bad_turtle

           print("Mario lost a life")
          # sound.beep(sounds[2])
           mario_life()


      wn.title("Mario at ({0}, {1}) DIR:{2}".format(mario['i'], mario['j'], mario['dir']))
   for bad_turtle in bad_turtles:
      set_direction(bad_turtle)
      moved = move_turtle(bad_turtle)
      if moved:
         (i1,j1) = (mario['i'], mario['j'])
         (i2,j2) = (bad_turtle['i'], bad_turtle['j'])
         if i1==i2 and j1==j2:
           print("Mario is eaten")
          # sound.beep(sounds[2])
           mario_life()


   if len(items) == 0 or mario['lives']==0:
      print("Game completed.")
      turtle.clearscreen()

      if mario['lives']==0:
        game_lost()
      elif len(items)==0:
        game_won()


   else:
      wn.ontimer(update, 200)

#it can only stop the mario.
def pause_game():
    mario['dir'] = STAND



wn.onkey(quit_game,"q")
wn.onkey(pause_game,"p")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(turn_up, "Up")
wn.onkey(turn_down, "Down")

init_game()  # fill items, walls etc.
update()      # start game
score_write()  #to write the score at the beging of the game.
mario_energy() #to write the left energy at the beging of the game.
#to lose energy for every 4 sec.
wn.ontimer(mario_energy, 4000)
wn.ontimer(mario_energy, 8000)
wn.ontimer(mario_energy, 12000)
wn.ontimer(mario_energy, 16000)
wn.ontimer(mario_energy, 20000)
wn.ontimer(mario_energy, 24000)
wn.ontimer(mario_energy, 28000)
wn.ontimer(mario_energy, 32000)
wn.ontimer(mario_energy, 36000)
wn.ontimer(mario_energy, 40000)
wn.ontimer(mario_energy, 44000)
wn.ontimer(mario_energy, 48000)
wn.ontimer(mario_energy, 52000)


#to write the lives at the beging of the game.
mariol.write("LIVES = {}".format(mario['lives']),
         font=("Arial", 12, "normal"), align="right")

wn.listen()  # listen events on this window
wn.mainloop()   # keep the window open
