ls1 = ["one", "two", "three", "four",  "five"]

ls1.append("ten")   # Adds element at the end of list
ls1.insert(3,"eight")   # Inserts the element at index 3
ls1.remove("two")   # Removes the element with value "two", if found!
value = ls1.pop(4)  # Removes the element at index 4
ls1.sort()      # Sorts the actual list in ascending order
ls1.sort(reverse = True)      # Sorts the actual list in descending order

ls2 = ls1[1:4]  # Slices the list and creates new one with elements from index 1 to 3 (i.e. 4-1)

ls3 = ls1   # Giving another name to existing list. Action on new list WILL effect old list.
ls4 = ls1.copy()    # Shallow copy of existing list. Action on new list WILL NOT effect old list.

ls5 = ls1 + ls2     # Joins two lists and creates a new list.
ls2.extend(ls1)     # Elements of first list is appended at the end of second list

#--------------------------------------------
# LIST COMPREHENSION
ls6 = [e for e in ls1 if "o" in e]

# This is same as:

ls6 = []
for e in ls1:
    if "o" in e:
        ls6.append(e)

#--------------------------------------------
