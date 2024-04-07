#-------------------- 1 Start --------------------
# Exception case with no Exception Handling!
print("First Line")
print(myvar)  # Variable myvar is not defined.
print("Last Line")  # This line will never get executed!
#-------------------- 1 End --------------------

#-------------------- 2 Start --------------------
# Simple Try and Except blocks
print("First Line")
try:
    print(myvar)  # Variable myvar is not defined.
except:
    print("The variable is not defined!")

print("Last Line")
#-------------------- 2 End --------------------

#-------------------- 3 Start --------------------
# Try with Except and Else blocks
print("First Line")
try:
    print("All is well")
except:
    print("This except block is not called.")
else:
    print("This else block is called if there is no exception.")
print("Last Line")

#-------------------- 3 End --------------------

#-------------------- 4 Start --------------------
# Try with Except, Else and Finally blocks
print("First Line")
try:
    print("All is well")
except:
    print("This except block is not called.")
else:
    print("This else block is called if there is no exception.")
finally:
    print("This finally block is always called irrespective of exception!!")
print("Last Line")

#-------------------- 4 End --------------------

#-------------------- 5 Start --------------------
# Proper Example for Error Handling!

print("--- Division of Numbers ---")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    # Convert the user input from string to integer type.
    num1 = int(num1)
    num2 = int(num2)

    # Perform the division.
    result = num1/num2
except ValueError:
    print("Error: Only numeric values are allowed!")
except ZeroDivisionError:
    print("Error: You cannot divide a number with Zero!")
except:
    print("Error: Some unknown exception occurred!")
else:
    print(f"Result is {result}")
finally:
    print("\n--- Thanks for using the calculator ---")

#-------------------- 5 End --------------------

#-------------------- 6 Start --------------------
# Raising an Exception intentionally
age = int(input("Enter your age:"))

if age < 0:
    raise ValueError("Age cannot be negative!")

print(f"Hi, you are {age} years old!")

#-------------------- 6 End --------------------