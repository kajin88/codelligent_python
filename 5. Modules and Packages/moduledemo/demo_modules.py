#-------------------- 1 Start --------------------
# Simple import of another module.
import mathutility

print(mathutility.add(3,6))
#-------------------- 1 End ---------------------

#-------------------- 2 Start --------------------
# Rename a module with some other convinient name.
import mathutility as calc

print(calc.add(5,8))
#-------------------- 2 End ---------------------

#-------------------- 3 Start --------------------
# Import specific functions or variables from a module.
from mathutility import mul, pi_value

print(pi_value)
print(mul(10, pi_value))
#-------------------- 3 End --------------------

#-------------------- 4 Start --------------------
# Check the in-built modules provided by Python

print(help("modules"))      # On IDLE Shell you don't need print. Command will be >>> help("modules")

#-------------------- 4 End --------------------

#-------------------- 5 Start --------------------
# Import in-built modules of Python
from math import sqrt, sin, radians
from platform import system

print("Squareroot of 121 is:", sqrt(121))
print("sin of 90 degrees is:", sin(radians(90)))

print("Current OS:", system())
#-------------------- 5 End --------------------
