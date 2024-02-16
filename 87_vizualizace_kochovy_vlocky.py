from turtle import *

# The Koch class accepts parameters recursion depth and edge length
class Koch:
    def __init__(self, depth, lenght):
        self.depth = depth
        self.lenght = lenght
    
    # The draw method of this class draws a Koch flake using the koch_flake method
    def draw(self):
        self.koch_flake(self.depth, self.lenght)
        
    # Main function, that uses recursion to draw Koch flake
    def koch_curve(self, depth, lenght):
        if depth == 0:
            forward(lenght)
        else:
            for angle in [60, -120, 60, 0]:
                self.koch_curve(depth-1, lenght/3)
                left(angle)
                
    def koch_flake(self, depth, lenght):
        for _ in range(3):
            self.koch_curve(depth, lenght)
            right(120)
    
# Requesting input parameters
depth = int(input("Enter the degree of the Koch flake: "))
lenght = int(input("Enter the length of the side of the Koch flake: "))

# Setting the speed to maximum
speed(0)

# Move turtle to start position for better rendering
penup()
goto(-lenght/2, lenght/3)
pendown()

# Calling the function koch_flake with 3 parameters
koch = Koch(depth, lenght)
koch.draw()

# Close window after click
done()