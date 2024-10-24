import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black

# Create a turtle object (tree turtle)
tree_turtle = turtle.Turtle()
tree_turtle.shape("turtle")
tree_turtle.color("green")  # Set turtle color to green for branche
tree_turtle.speed(0)  # Fastest drawing speed

# Function to draw the fractal tree recursively
def draw_tree(branch_length, t):
    if branch_length > 5:  # Recursive case: continue drawing while the branch is long enough
        t.forward(branch_length)
        t.right(20)  # Turn right for one branch
        draw_tree(branch_length - 15, t)  # Recursive call with a shorter branch
        t.left(40)  # Turn left for the next branch
        draw_tree(branch_length - 15, t)  # Recursive call again with a shorter branch
        t.right(20)  # Restore original angle
        t.backward(branch_length)  # Move the turtle back to its starting position

# Position the turtle at the bottom center of the screen
tree_turtle.penup()
tree_turtle.goto(0, -250)  # Start at the bottom middle of the screen
tree_turtle.pendown()
tree_turtle.left(90)  # Point the turtle upwards to start drawing the tree

# Draw the fractal tree starting with the initial branch length
draw_tree(100, tree_turtle)

# Hide the turtle after drawing the tree
tree_turtle.hideturtle()

# Keep the turtle graphics window open until it's closed by the user
screen.mainloop()
