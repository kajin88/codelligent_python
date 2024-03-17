myOrgDetails = {
    "name" : "Codelligent",             # KEY = String, VALUE = String
    "headquarters": "Munich",           # KEY = String, VALUE = String
    "employees" : 650,                  # KEY = String, VALUE = Integer
    "locations" : (1212.23, 45645.3),   # KEY = String, VALUE = Tuple
    "depts" : [                         # KEY = String, VALUE = List of Dictionary elements
        {
            "name": "HR",
            "employees" : 30,
            "leads" : (                 # KEY = String, VALUE = Tuple of Dictionary elements
                {"name": "John", "location" : "USA"},
                {"name" : "Rahul", "location" : "Singapore"}
            )
        },
        {
            "name": "IT",
            "employees" : 250,
            "leads" : (
                {"name": "Alex", "location" : "Germany"},
                {"name" : "Raj", "location" : "India"}
            )
        }
    ],
    "offices": {"Germany", "USA", "Singapore", "India", "Denmark"}  # KEY = String, VALUE = Set
}

#--------------------------------------------------------------
# Who is the head of IT in India?
head = myOrgDetails["depts"][1]["leads"][1]["name"]
print("Head of IT dept in India is", head)
#--------------------------------------------------------------

# Where all we have offices for Codelligent?
offices = myOrgDetails["offices"]
for n in offices:
    print(n, end=",")

print() # Extra print to ge the next printing to new line.

#--------------------------------------------------------------

# How many employees are there in total and out of them how many are in HR dept?
totalEmps = myOrgDetails["employees"]
hrEmps = myOrgDetails["depts"][0]["employees"]

print("Total Employees:", totalEmps, "HR Employees:", hrEmps)   # Simple print with multiple parameters.

print(f"Total Employees are {totalEmps}, and HR employees are {hrEmps}.")   # Formatted printing with variables inserted inside a string.
#--------------------------------------------------------------