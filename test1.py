#Turtle Graphics Game
import turtle
import math
import random
import os
import time
import threading

speed = 1	


def fundamentals():
	#Set up screen
	wn=turtle.Screen()
	wn.bgcolor("white")
	wn.setup(700,550)
	wn.screensize(660,480)
	wn.bgpic("giphy.gif")
	wn.tracer(2)

	#draw border
	mypen = turtle.Turtle()
	mypen.speed(0)
	mypen.penup()
	mypen.setposition(-320,-230)
	mypen.pendown()
	mypen.pensize(3)
	for side in range(2):
		mypen.forward(640)
		mypen.left(90)
		mypen.forward(460)
		mypen.left(90)
	mypen.hideturtle()

	lastpen = turtle.Turtle()
	lastpen.speed(0)
	
	timepen = turtle.Turtle()
	timepen.speed(0)
	timepen.hideturtle()


	#Create player turtle
	player=turtle.Turtle()
	player.color("cyan")
	player.shape("triangle")
	player.penup()
	player.speed("slowest")

	"""
	#create enemy
	goal=turtle.Turtle()
	goal.color("red")
	goal.shape("circle")
	goal.penup()
	#goal.speed(0)
	goal.setposition(random.randint(-315,315),random.randint(-225,225))
	"""
	#forage
	forage=turtle.Turtle()
	forage.color("yellow")
	forage.shape("square")
	forage.penup()
	forage.setposition(random.randint(-310,310),random.randint(-220,220))


	#create barriers
	maxbarrier = 10
	barrier = []
	
	for barr in range (maxbarrier):
		barrier.append(turtle.Turtle())
		barrier[barr].color("black")
		barrier[barr].shape("square")
		barrier[barr].penup()
		barrier[barr].speed(0)
		barrier[barr].setposition(random.randint(-315,315),random.randint(-220,220))	


	
	#create enemys
	maxenemy = enemy_numbers
	enemy = []

	for count in range (maxenemy):
		enemy.append(turtle.Turtle())
		enemy[count].color("red")
		enemy[count].shape("circle")
		enemy[count].penup()
		enemy[count].speed(0)
		enemy[count].setposition(random.randint(-315,315),random.randint(-225,225))
		enemy[count].right(random.randint(0,360))


	#set speed variable
	

	#define functions
	def turnleft():
		player.left(90)
		player.forward(3)

	def turnright():
		player.right(90)
		player.forward(3)
		
	def increasespeed():
		global speed
		speed += 1
		
	def reducespeed():
		global speed
		speed -= 1
	
	def stop():
		global speed
		speed = 0

	def quit_game():
		 wn.bye()
	"""
	def jet():
		player.forward(100)
"""
	def isCollision(t1,t2):
		d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
		if d < 20:
			return True
		else:
			return False

	#set keyboard bindings
	turtle.listen()
	turtle.onkey(turnleft,"Left")
	turtle.onkey(turnright,"Right")
	turtle.onkey(increasespeed,"Up")
	turtle.onkey(reducespeed,"Down")
	turtle.onkey(stop,"s")
	turtle.onkey(quit_game,"q")
	#turtle.onkey(jet," ")

	#life
	life = 3
	lastpen.penup()
	lastpen.hideturtle()
	lastpen.setposition(-280,230)
	lifestring = "life: %s"%life
	lastpen.write("life: 3",False,align="left",font=("Arial",10,"normal"))

	#score
	score = 0
	mypen.penup()
	mypen.hideturtle()
	mypen.setposition(-240,230)
	scorestring = "score: %s"%score
	mypen.write("score: 0",False,align="left",font=("Arial",10,"normal"))
	
	"""#timee
	time=10
	for i in range(time):
		time.sleep(1)
		time=time-i
		lastpen.penup()
		lastpen.hideturtle()
		lastpen.setposition(-220,230)
		timestring = "time: %s"%time
		lastpen.write(timestring,False,align="left",font=("Arial",10,"normal"))

		#if isCollision(player, enemy[count]):
			"""	

	def game_over():
		global enemy_numbers
		if life<1:
			wn.bgcolor("black")
			player.hideturtle()
			for count in range (enemy_numbers):
				enemy[count].hideturtle()
				
			mypen.pencolor("cyan")
			mypen.setposition(-200,100)
			mypen.write("İDİOT YOU DIED",False,align="left",font=("Arial",40,"normal"))
			lastpen.pencolor("cyan")
			lastpen.setposition(-180,0)
			lastpen.write("Your Score: %s"%score,False,align="left",font=("Arial",40,"normal"))
		

	while life>0:
		player.forward(speed)
		
	
		#boundry checking
		if player.xcor()>320 or player.xcor()<-320:
			player.right(180)
			#os.system("smb_bump.wav&") #add voice
	
		#boundary checking
		if player.ycor()>230 or player.ycor()<-230:
			player.right(180)
			#os.system("")
	
		if isCollision(player, barrier[barr]):
				player.left(180)
					
		
		#move the goal
		for count in range(maxenemy):
			enemy[count].forward(1)
		
			#boundry checking
			if enemy[count].xcor()>310 or enemy[count].xcor()<-310:
				enemy[count].right(180)
	
			#boundary checking
			if enemy[count].ycor()>220 or enemy[count].ycor()<-220:
				enemy[count].right(180)
		
			#collision checking
			if isCollision(player, enemy[count]):
				enemy[count].setposition(random.randint(-320,320),random.randint(-230,230))
				enemy[count].right(random.randint(0,360))
				life-=1
				#draw the life on the screen
				lastpen.undo()
				lastpen.penup()
				lastpen.hideturtle()
				lastpen.setposition(-280,230)
				lifestring = "life: %s"%life
				lastpen.write(lifestring,False,align="left",font=("Arial",10,"normal"))
				print("enemy collision %s"%(3-life))


			if isCollision(player, forage):
				forage.setposition(random.randint(-320,320),random.randint(-230,230))
				score+=10			
				mypen.undo()
				mypen.penup()
				mypen.hideturtle()
				mypen.setposition(-240,230)
				scorestring = "score: %s"%score
				mypen.write(scorestring,False,align="left",font=("Arial",10,"normal"))
				print("eat %s forage"%(score/10))
				

			




	game_over()
	
	"""
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







	wn.onkey(quit_game,"q")
	#wn.onkey(pause_game,"p")
	wn.onkey(turn_left, "Left")
	wn.onkey(turn_right, "Right")
	wn.onkey(turn_up, "Up")
	wn.onkey(turn_down, "Down")


	"""



	wn.exitonclick()



def level1():
	enemy_numbers=10
	fundamentals()
	t = threading.Timer(3.0, game_over)
	t.start()  # after 30 seconds, "hello, world" will be printed
	
	
	








def game_over():
		global enemy_numbers
		if life<1:
			wn.bgcolor("black")
			player.hideturtle()
			for count in range (enemy_numbers):
				enemy[count].hideturtle()
				
			mypen.pencolor("cyan")
			mypen.setposition(-200,100)
			mypen.write("İDİOT YOU DIED",False,align="left",font=("Arial",40,"normal"))
			





#welcome page

select_mode=input("""\n\nWelcome to My First Game \n\n_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - -      Select Mode a)classic b)free
_/﹋\_\n\n \n""")

if select_mode=="b":
	enemy_numbers=int(input("You want how many enemies = "))
	fundamentals()
elif select_mode=="a":
	which_level = int(input("Which level do you want to (if your first time you say 1) = "))
	if which_level==1:
		enemy_numbers=10
		#t = threading.Timer(3.0,game_over )		
		#t.start()		
		fundamentals()
		  # after 30 seconds, "hello, world" will be printed
	
	

else:
	print("""\n\n\nenter correctly good by idiot try again

☺ /
/▌
/\\
 """)	



















