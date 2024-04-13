#-------------------- 1 Start --------------------
# Import modules from the package.
from myutilities import lengthutility, timeutility

print(lengthutility.mtrtocm(3))
print(timeutility.hourstosec(2))
#-------------------- 1 End --------------------

#-------------------- 2 Start --------------------
# Import methods from a module of a package.
from myutilities.lengthutility import mtrtocm
from myutilities.timeutility import hourstosec

print(mtrtocm(3))
print(hourstosec(2))
#-------------------- 2 End --------------------

#-------------------- 3 Start ----------------------
# Importing all the modules of a package in one shot.

# NOTE: This is possible ONLY if the __all__ list is 
# overridden in the __init__.py file of the package
# to include all the modules names.
from myutilities import *

print(mathutility.mul(3,5))
#-------------------- 3 End --------------------