dict1 = {"name":"Alex", 
         "location": "Germany",
         ("latitude", "logitude"): (1234.23, 456.232),     # A Tuple as both KEY and VALUE.
         "interests": ["photography", "coding", "hiking"], # A List as a VALUE.
         "phone": 49234234,
         "kids":{"Thomas":12, "Ana": 9}     # A Dcitionary as VALUE. This is a Nested Dictionary.
         }

dict1["name"] = "John"  # Updating the Value for existing Key.
dict1["pincode"] = 123456   # Adding new Key-Value pair, since the Key doesn't exist already.

print(dict1["interests"])
print(dict1.get("interests"))
print(dict1.get("SomeRandomKey", "Not Found!")) # Get with default Value if the Key is not found.

if "name" in dict1:
    print(dict1["name"])

if "SomeKey" not in dict1:
    print("Not Found!")

print("All Keys:", dict1.keys())     # Gets all Keys only.
print("All Values:", dict1.values())   # Gets all Values only.
print("All Items:", dict1.items())    # Gets all Key-Value pairs as Tuples.

dict1.pop(("latitude", "logitude"))     # Delete an entry based on the Key passed.

# Extracting all the Key-Value pairs one by one.
print("\n\n--- All Items in Dictionary ---\n")
for k, v in dict1.items():
    print(k, v, sep=" => ")