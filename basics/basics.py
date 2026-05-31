# Lists store multiple items in a single variable, and they are ordered and changeable.
thislist = ["apple", "banana", "cherry"] 
print(thislist) 

#creating a list with the list() constructor
fruits = list(("banana","Watermelon","grapes")) 
print(fruits) 

# deleting an item from a list
fruits.remove("banana")
print(fruits)

#looping through a list
people = ["Hassan","KG","Musa"] 
for x in people:
    print(x)
#list comprehension
people = ["Hassan","KG","Musa"]
newlist = [x for x in people if "a" not in x]

for x in newlist:
    print(f"{x} is the new number {1}") 

# tuples are ordered and unchangeable, & they allow duplicate values.
thistuple = ("volvo","bmw","ford")
print(thistuple)