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
