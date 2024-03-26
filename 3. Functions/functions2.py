#-------------------- 1 Start --------------------
# Function with Arbitrary Arguments which takes n number 
# of values for performing addition.

def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

print("Sum is:", add())             # From zero to any number of arguments can be passed.
print("Sum is:", add(2,3,4))
print("Sum is:", add(4,5,6,7,8,9))

#-------------------- 1 End ----------------------

#-------------------- 2 Start --------------------
# Function with two mandatory and then Arbitrary Arguments 
# which takes n number of values for performing addition.

def add(a, b, *nums):
    sum = a + b
    for n in nums:
        sum += n
    return sum

print("Sum is:", add(2,3))          # Passing minimum TWO arguments is Mandatory!
print("Sum is:", add(4,5,6,7,8,9))

#-------------------- 2 End ----------------------

#-------------------- 3 Start --------------------
# Calling a function with keyword arguments.

def greetings(fname, lname, timeOfDay):
    if timeOfDay == "morning":
        print(f"Good Morning, {fname} {lname}!")
    elif timeOfDay == "afternoon":
        print(f"Good Afternoon, {fname} {lname}!")
    else:
        print(f"Good Day, {fname} {lname}!")

greetings(fname = "Alex", lname = "Smith", timeOfDay = "morning")
greetings(timeOfDay = "morning", lname = "Smith", fname = "Alex")   # Can pass the arguments in any order with named arguments!

#-------------------- 3 End ----------------------

#-------------------- 4 Start --------------------
# Using Arbitrary Keyword Arguments to pass any number of
# keyword arguments.

def showExperience(**exps):
    print(f"The experience list is:")
    for k,v in exps.items():
        print(f"{k} = {v}")

showExperience(google = 3, microsoft = 2, siemens = 6)

#-------------------- 4 End ----------------------


#-------------------- 5 Start --------------------
# Mixing mandatory positional arguments, Arbitrary Arguments
# and Arbitrary Keyword Arguments.

def showExperience(fname, lname, *skills, **exps):
    print(f"Employee Name: {fname} {lname}")
    print("Skill set:")
    counter = 1
    for s in skills:
        print(f"{counter}. {s}")
        counter+=1

    print(f"Experience:")
    for k,v in exps.items():
        print(f"{k} = {v} years")

showExperience("Alex", "Smith", "C#", "Python", "Django", "Flask", "AWS", google = 3, microsoft = 2, siemens = 6)
# "Alex" and "Smith" goes into fname and lname respectively. All other non-keyword arguments go into skills.
# All keyword arguments go into exps.

#-------------------- 5 End ----------------------


