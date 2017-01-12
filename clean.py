# cleaner

#first screen and game is start with press space
#second arrow keys

import turtle
import math
import random
import os
import threading

# welcome page
select_mode=input("""\n\nWelcome to My First Game \n\n_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - -      Select Mode a)classic b)free
_/﹋\_\n\n \n""")

if select_mode.lower() == "b":
	max_enemy = int(input("You want how many enemies (max = 15) \n="))
elif select_mode.lower() == "a":
	which_level = int(input("Which level do you want to (if your first time you say 1) = "))
	if which_level == 1:
		max_enemy = 5
		live = 20
		
	elif which_level == 2:
		max_enemy = 7
		live = 15
	
	elif which_level == 3:
		max_enemy = 9
		live = 10	
	elif which_level == 4:
		max_enemy = 11
		live = 5
	elif which_level == 5:
		max_enemy = 13
		live = 5

else:
	print("""\n\n\nenter correctly try again

☺ /
/▌
/\\
 """)	



# general things
speed = 1
#live = 15
tScore = 0
eScore = 0


# setup screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(700,550)
wn.screensize(660,480)
wn.bgpic("giphy.gif")
wn.tracer(2)

# pens
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.penup()
pen1.setposition(-320,-230)
pen1.pensize(3)

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.hideturtle()

pen4 = turtle.Turtle()
pen4.speed(0)
pen4.penup()
pen4.hideturtle()

# draw tables
def draw_tScore(pen,score):	
	pen.pensize(1)
	pen.setposition(-248,232)
	pen.color("red")
	score_str = "score: %s"%score
	pen.write(score_str,False,align="left",font=("Arial",10,"italic"))
	pen.hideturtle()

draw_tScore(pen2,eScore)

def draw_eScore(pen,score):	
	pen.pensize(1)
	pen.setposition(-290,245)
	pen.color("red")
	score_str = "enemy score: %s"%score
	pen.write(score_str,False,align="left",font=("Arial",10,"italic"))
	pen.hideturtle()

draw_eScore(pen4,eScore)

def draw_live(pen,live):
	pen.pensize(1)
	pen.color("red")
	pen.setposition(230,232)
	live_str = "live: %s"%live 
	pen.write(live_str,False,align="left",font=("Arial",15,"normal"))
	pen.hideturtle()

draw_live(pen3,live)

def draw_finish(pen,tab,score):
	pen.pensize(1)
	wn.bgcolor("black")
	pen.setposition(-300,-50)
	pen.color("pink")
	pen.write(tab,False,align="left",font=("Arial",30,"italic"))

def draw_border(pen):
	pen1.pendown()
	pen.color("blue")
	for side in range(2):
		pen.forward(640)
		pen.left(90)
		pen.forward(460)
		pen.left(90)
		pen.hideturtle()
	pen.penup()

draw_border(pen1)

# create player

player = turtle.Turtle()
player.color("cyan")
player.shape("triangle")
player.penup()
player.speed("slowest")



# create enemies
#max_enemy = 10
enemy = []

for enmy in range (max_enemy):
	enemy.append(enmy)
	enemy[enmy] = turtle.Turtle()
	enemy[enmy].color("red")
	enemy[enmy].shape("circle")
	enemy[enmy].penup()
	enemy[enmy].speed(0)
	enemy[enmy].setposition(random.randint(-315,315),random.randint(-225,225))
	enemy[enmy].left(random.randint(0,360))

# create barriers
max_barr = 10
barrier = []

for brr in range(max_barr):
	barrier.append(brr)
	barrier[brr] = turtle.Turtle()
	barrier[brr].shape("square")
	barrier[brr].color("yellow3")
	barrier[brr].penup()
	barrier[brr].speed(0)
	barrier[brr].setposition(random.randint(-315,315),random.randint(-225,225))

# create forage
forage = turtle.Turtle()
forage.penup()
forage.shape("square")
forage.color("blue")
forage.setposition(random.randint(-315,315),random.randint(-225,225))

# create big forage
b_forage = turtle.Turtle()
b_forage.penup()
b_forage.hideturtle()

# define functions
#def okey_():
	

def turn_left():
	player.setheading(180)
	#player.forward(3)

def turn_right():
	player.setheading(0)
	#player.forward(3)

def turn_up():
	player.setheading(90)
	#player.forward(3)

def turn_down():
	player.setheading(270)
	#player.forward(3)

def increase_speed():
	global speed
	speed += 1
	#player.forward(1)

def reduce_speed():
	global speed
	speed -= 1

def stop_player():
	global speed
	speed = 0

"""def stop_game():
	wn.stand()"""

def quit_game():
	wn.bye()


turtle.listen()
#turtle.onkey(okey_," ")
turtle.onkey(turn_left,"Left")
turtle.onkey(turn_up,"Up")
turtle.onkey(turn_down,"Down")
turtle.onkey(turn_right,"Right")
turtle.onkey(increase_speed," ")
turtle.onkey(reduce_speed,"b")
turtle.onkey(stop_player,"s")
turtle.onkey(quit_game,"q")

def bigbang(t1,t2):
	d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
	if d < 20:
		return True
	else:
		return False

def cBorder(t):
	if t.xcor()>320 or t.xcor()<-320 or t.ycor()>230 or t.ycor()<-230 :
		t.left(180)
		t.forward(5)
		

def infinitive_screen(t):
	if t.xcor()>320:
		t.speed(0)
		t.hideturtle()
		t.forward(-640)
		t.showturtle()
	if t.xcor()<-320:
		t.speed(0)
		t.hideturtle()
		t.forward(-640)
		t.showturtle()
	if t.ycor()>230:
		t.speed(0)
		t.hideturtle()
		t.forward(-460)
		t.showturtle()
	if t.ycor()<-230:
		t.speed(0)
		t.hideturtle()
		t.forward(-460)
		t.showturtle()

def forage_w(t1 ,score,pen):
	global forage 
	if bigbang(t1 ,forage):
		score +=10
		pen.undo()
		pen.undo()
		draw_[score](pen,score)
		forage.setposition(random.randint(-315,315),random.randint(-225,225))


def game_over():
	global max_enemy ,max_barr ,message
	if live<1:
		player.hideturtle()
		for count in range(max_enemy):
			enemy[count].hideturtle()
		for brr in range(max_barr):
			barrier[brr].hideturtle()
		message = ("""	come on man
you died I think you are very stupid
 because this game is so easy bro 

	your score: %s
	enemy score: %s"""%(tScore,eScore))
		draw_finish(pen1 ,message ,tScore)

	
while live>0:
	player.forward(speed)
	#cBorder(player)
	infinitive_screen(player)
	
	for enym in range (max_enemy):
		enemy[enym].forward(1)		
		cBorder(enemy[enym])
		#infinitive_screen(enemy[enym]) 
		
		if bigbang(player,enemy[enym]):
			live -= 1
			#player.setposition(random.randint(-315,315),random.randint(-225,225))
			#enemy[enym].left(180)
			pen3.undo()
			pen3.undo()
			draw_live(pen3,live)		
		
		if bigbang(enemy[enym] ,forage):
			eScore +=10
			pen4.undo()
			pen4.undo()
			draw_eScore(pen4,eScore)
			forage.setposition(random.randint(-315,315),random.randint(-225,225))
	
		for brr in range (max_barr):
			if bigbang(barrier[brr] ,enemy[enym]):
				enemy[enym].left(180)
				enemy[enym].forward(5)
			if bigbang(player ,barrier[brr]):
				player.left(180)
				player.forward(5)
		
			
	if bigbang(player ,forage):
		tScore +=10
		pen2.undo()
		pen2.undo()
		draw_tScore(pen2,tScore)
		forage.setposition(random.randint(-315,315),random.randint(-225,225))

	

game_over()


wn.exitonclick()


print("""
¶▅c●▄███████||▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅||█~ ::~ :~ :► IDIOTS
▄██ ▲  █ █ ██▅▄▃▂
███▲ ▲ █ █ ███████
███████████████████████►
◥☼▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙☼◤ """)
