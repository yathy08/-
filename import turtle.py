import turtle
import time

# Function to draw a heart
def draw_heart():
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('red')
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

# Function to write text with animation
def write_text(text, position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.color('black')

    # Animate writing one letter at a time
    for char in text:
        turtle.write(char, align="center", font=("Arial", 16, "normal"))
        position = turtle.position()
        position = (position[0] + 15, position[1])  # Move to the right for the next letter
        turtle.goto(position)
        time.sleep(0.2)  # Adjust the speed of animation as needed

# Set up turtle
turtle.speed(0)

# Draw heart
draw_heart()

# Animate writing text
write_text("I will see you soon my lady.kisses kisses kisses", (0, 50))

# Keep window open until closed by user
turtle.done()
