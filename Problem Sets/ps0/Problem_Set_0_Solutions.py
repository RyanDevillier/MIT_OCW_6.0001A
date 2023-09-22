# Importing dependencies
import numpy

# Asks the user to enter a number "x"
x = int(input("Enter number x: "))

# Asks the user to enter a number "y":
y = int(input("Enter number y: "))

# Prints out the number "x", raised to the power "y":
x_to_y = x**y
print(f"x**y = {x_to_y}")

# Prints out the log (base 2) of "x":
log2 = numpy.log2(x)
print(f"log(x) = {int((log2))}") 
