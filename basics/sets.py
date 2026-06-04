# set exercises
# sets are unordered collections of unique items. you can add or reomve items.
A = {"maths","science","english"}
B = {"science","history","geography"}

joined_sets = A.union(B)    # joining sets 
print(f"Joined sets: {joined_sets}")

# getting the common items in both sets
common_items = A.intersection(B)
print(f"Common items: {common_items}")

# getting the unique items
unique_items = A ^ B
#unique_items = A.symmetric_difference(B)  
print(f"Unique items: {unique_items}")

# converting a list to a set to print unique values
list = [11,11,22,22,33,44,44]
list_to_set = set(list)     
        # converting list to set
print(f"Original list: {list}")
print(f"List as set with unique values: {list_to_set}") 

# list in ascending order
sorted_list = sorted(list,reverse=False) 
print(f"List in ascending order: {sorted_list}") 
