#-------------------- 1 Start --------------------
#Function with one parameter with default value.
def greetings(name = "World"):
    print(f"Hello {name}!")

greetings()
greetings("Codelligent")
#-------------------- 1 End ----------------------

#-------------------- 2 Start --------------------
#Function with return value.
def add(a,b):
    c = a+b
    return c

sum = add(3,4)
print(f"Sum is {sum}")
#-------------------- 2 End ----------------------

#-------------------- 3 Start --------------------
#Funtion with local variable same as a global variable.
location = "India"

def showLocation():
    location = "Germany"
    print(f"Inside -> {location}")

showLocation()
print(f"Outside -> {location}")
# OUTPUT:
# Inside -> Germany
# Outside -> India
#-------------------- 3 End ----------------------

#-------------------- 4 Start --------------------
#Funtion with using a global variable in local scope.
location = "India"

def showLocation():
    global location
    location = "Germany"
    print(f"Inside -> {location}")

showLocation()
print(f"Outside -> {location}")
# OUTPUT:
# Inside -> Germany
# Outside -> Germany
#-------------------- 4 End ----------------------

#-------------------- 5 Start --------------------
#Function with String and List parameters.
def showMenu(day, menu):
    print(f"Menu for {day} is:")
    index = 1

    for item in menu:
        print(f"{index}. {item}")
        index +=1


mondayMenu = ["Pizza", "Sandwich", "Pasta"]
tuesdayMenu = ["Burger", "Biriyani", "Subway", "Salad", "Cake"]

showMenu("Monday", mondayMenu)
showMenu("Tuesday", tuesdayMenu)
#-------------------- 5 End ----------------------