import turtle
turtle.pencolor("black")  #color of pen
turtle.pensize(4)         #size of pen
turtle.bgcolor("skyblue") #background color of screen
turtle.speed(5)           #speed of drawing

turtle.fillcolor("red")   #inside color 
turtle.begin_fill()

turtle.left(70)
turtle.forward(200)

turtle.right(140)
turtle.forward(100)

turtle.right(112)
turtle.forward(70)

turtle.end_fill()


#move downword

turtle.fillcolor("white")  #inside color
turtle.begin_fill()

turtle.left(112)
turtle.forward(100)

#move upword
turtle.left(140)
turtle.forward(100)
turtle.end_fill() 

#up to down

turtle.fillcolor("red")   #inside color 
turtle.begin_fill()

turtle.right(140)
turtle.forward(100)

#drow line right to left
turtle.right(112)
turtle.forward(67) 
turtle.end_fill()


turtle.fillcolor("red")  #inside color
turtle.begin_fill()
turtle.right(0)
turtle.forward(66) 

#revisting to node
turtle.right(108)
turtle.forward(100)
turtle.end_fill()

turtle.backward(100)
turtle.left(108)
#end

#move to down
turtle.left(75)
turtle.forward(200)

turtle.fillcolor("green")  #inside color 
turtle.begin_fill()
#last horizontal
turtle.left(107)
turtle.forward(70)


turtle.left(112)
turtle.forward(105)
turtle.end_fill() 


turtle.fillcolor("green")  #inside color 
turtle.begin_fill()
turtle.right(112)
turtle.forward(70)


turtle.left(115)
turtle.forward(100)
turtle.end_fill()


turtle.right(180)
turtle.forward(200)

turtle.left(140)
turtle.forward(94)

turtle.fillcolor("blue")  #inside color 
turtle.begin_fill()

turtle.left(0)
turtle.forward(94)

turtle.right(145)
turtle.forward(100)
turtle.end_fill()

turtle.fillcolor("blue")   #inside color
turtle.begin_fill()
turtle.right(0)
turtle.forward(100)
 
turtle.right(112)
turtle.forward(70)
turtle.end_fill()


turtle.right(108)
turtle.forward(103)

turtle.left(112)
turtle.forward(60)

turtle.fillcolor("blue")  #inside color
turtle.begin_fill()
turtle.left(104)
turtle.forward(99)

turtle.right(106)
turtle.forward(48)
turtle.end_fill()


turtle.fillcolor("green")  #inside color 
turtle.begin_fill()
turtle.right(0)
turtle.forward(77)
turtle.right(108)
turtle.forward(100)
turtle.end_fill()
turtle.penup()

#turtle.end_fill()
turtle.exitonclick()
