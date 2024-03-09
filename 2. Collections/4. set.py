set1 = {"apple", "banana", 23, 3.4, True}     # Unordered collection of various data types.
set1 = {"apple", "banana", 23, 3.4, "apple", True, 1, False, 0}     # "apple", 1, and 0 will be ignored as they are duplicate to "apple", True and False.

# print(set[2])     # Index based access is not possible with Set.

# in and not in can be use for checking if an item exists in set.
if "apple" in set1:
    print("Yes")


set1.add("mango")    # Add a new item into the set.

set2 = {"abc", "xyz", 33}
set1.update(set2)   # All elements of set2 is added into set1.

list1 = ["item1", "item2"]
set1.update(list1)  # All elements of list1 is added into set1. Possible to add List, Tuples, Dictionary (Any iterable object).

set1.remove("banana")   # Removes an item from the set. If item not found, it will throw an error!
set1.discard("banana")  # Removes an item from the set. If item not found, it will NOT throw an error!

#------------------------------------------------

set1 = {"apple", "banana", "mango"}
set2 = {"microsoft", "google", "apple"}

set3 = set1.union(set2)     # Performs a UNION between set1 and set2
set4 = set1.intersection(set2)     # Performs an INTERSECTION between set1 and set2
set5 = set1.difference(set2)     # Performs set1 DIFFERENCE set2
set6 = set2.difference(set1)     # Performs set2 DIFFERENCE set1. Output will be different from set1.difference(set2).

#------------------------------------------------

set1 = {"a", "b", "c"} #subset
set2 = {"f", "e", "d", "c", "b", "a"} #superset

set1.issubset(set2)     # Returns TRUE
set2.issubset(set1)     # Returns FALSE
set2.issuperset(set1)   # Returns TRUE
set1.issuperset(set2)   # Returns FALSE