import turtle
# Define a list of colors for our spiral
colors = ['red', 'yellow', 'white',
          'purple', 'aqua', 'orange']

# Create a Turtle object
t=turtle.Pen()
t.speed() # Set the drawing speed to the maximum
turtle.bgcolor('black') # Set the background color to black

# Cycle through the colors
for x in range(200):
        t.pencolor(colors[x%6])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
turtle.done()
t.speed(10)
turtle.bgcolor('black')
for x in range(200):
        t.pencolor(colors[x%6])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(60)
# Hide the Turtle graphics window
turtle.done()