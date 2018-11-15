import turtle
import random
import winsound
import time

#Variable decleration
score=0
live=3

#Draw the screen
wn=turtle.Screen()
wn.title("Falling Sky game by Maryam Ali")
wn.bgpic("background.png")
wn.setup(width=800,height=600)
wn.tracer(9)
wn.register_shape("left_deer.gif")
wn.register_shape("right_deer.gif")
wn.register_shape("hunter.gif")
wn.register_shape("nut.gif")




#Add player
player=turtle.Turtle()
player.speed(0)
player.shape("right_deer.gif")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction="stop"

#Add pen to draw score box
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.clear()
pen.write("Score: {} Live: {}".format(score,live),align="center",font=("Courier",24,"normal"))

#Create list of good Falling object
objects=[]
#Add  good Falling object
for i in range(20):
	object=turtle.Turtle()
	object.speed(0)
	object.speed=random.randint(1,4)
	object.shape("nut.gif")
	object.color("black")
	object.penup()
	object.goto(random.randint(-380,380),250)
	objects.append(object)
	
#Create list of bad Falling object
zombies=[]
#Add  good Falling object
for i in range(10):
	zombie=turtle.Turtle()
	zombie.speed(0)
	zombie.speed=random.randint(1,4)
	zombie.shape("hunter.gif")
	zombie.color("red")
	zombie.penup()
	zombie.goto(random.randint(-380,380),250)
	zombies.append(zombie)

#Functions
def go_left():
	player.direction="left"
	player.shape("left_deer.gif")

def go_right():
	player.direction="right"
	player.shape("right_deer.gif")
	
#Keyboard bindings
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#Main game loop
while True:
	wn.update()
	
	#Check bouncing
	
	if player.xcor()<-390 or player.xcor()>390 or player.ycor()>290 or player.ycor()<-290:
		player.goto(0,-250)
	if live<0:
		pen.clear()
		pen.goto(0,0)
		pen.write("Game over",align="center",font=("courier",27,"normal"))
		time.sleep(5)
		wn.exitonclick()
	if player.direction=="left":
		x=player.xcor()
		x-=3
		player.setx(x)
	if player.direction=="right":
		x=player.xcor()
		x+=3
		player.setx(x)
	
	#Move the good objects
	for object in objects:
	#Object moving
		y=object.ycor()
		y-=object.speed
		object.sety(y)
	
	#Check if off the screen
		if object.ycor()<-300:
			x=random.randint(-380,380)
			y=random.randint(300,400)
			object.goto(x,y)
		
	#Check for collision
		if object.distance(player)<40:
			winsound.PlaySound("eat.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
			x=random.randint(-380,380)
			y=random.randint(300,400)
			object.goto(x,y)
			score+=10
			pen.clear()
			pen.write("Score: {} Live: {}".format(score,live),align="center",font=("Courier",24,"normal"))

			
	
	#Move the bad objects
	for zombie in zombies:
	#Object moving
		y=zombie.ycor()
		y-=zombie.speed
		zombie.sety(y)
	
	#Check if off the screen
		if zombie.ycor()<-300:
			x=random.randint(-380,380)
			y=random.randint(300,400)
			zombie.goto(x,y)
		
	#Check for collision
		if zombie.distance(player)<40:
			winsound.PlaySound("crash.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
			x=random.randint(-380,380)
			y=random.randint(300,400)
			zombie.goto(x,y)
			score-=10
			live-=1
			pen.clear()
			pen.write("Score: {} Live: {}".format(score,live),align="center",font=("Courier",24,"normal"))

		
		




wn.mainloop()

