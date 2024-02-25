tup1 = ("one", "two", "three")  # Usual way of declaring Tuple.
tup2 = "one", "two", "three"    # Another way of declaring Tuple.

tup3 = ("one")  # This is NOT a tuple, but a plain string.
tup4 = ("one",) # Must use a comma if a Tuple needs to be created with only one element.

print(tup1[2])  # Can access elements using index.
# tup1[2] = "abc"   # CANNOT modify the elements of a tuple!

tup5 = tup1 + tup2  # Joins two Tuples and creates a new Tuple.
tup6 =  tup1 * 3    # Creates a Tuple with repeating all elements in other Tuple 3 times.

tup1.count("one")   # Returns the number of times "one" exists in the Tuple.
tup1.index("one")   # Returns the index of FIRST occurance of the element "one" in the Tuple.

var1, var2, var3 = tup1 # Unpacking of a Tuple. Elements of tuple is unpacked into the variables. Number of variables MUST be equal to number of elements in tuple.

#---------------------------------
# When to use Tuples?

# EXAMPLE 1
resolution_width = 1920
resolution_height = 1080
# Instead of individual variables for this kind of related values, a Tuple can be created.
resolution = (1920, 1080)

#---------------------------------

# EXAMPLE 2
coord_x = 100
coord_y = 130
coord_z = 54
# Instead of individual variables for this kind of related values, a Tuple can be created.
coordinates = (100, 130, 54)

#---------------------------------