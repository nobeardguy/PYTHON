#Tuples
# tuples are ordered and unchangeable, & they allow duplicate values.they use parantheses,()
thistuple = ("volvo","bmw","ford")
print(thistuple)

#creating a tuple with the tuple() constructor
thistuple = tuple(("volvo","mazda","honda"))
print (thistuple) 

print(type(thistuple))
# Adding items to a tuple is not possible, but you can convert the tuple into a list, add the item, and convert it back into a tuple.
y= list(thistuple)
y.append("toyota") 
y.remove("mazda")    # removing an item from the list

#converting back to tuple
thistuple = tuple(y)
print(f"The updated tuple is: {thistuple}") 

print(type(thistuple))

# Excercises: create a tuple & access the 3rd item
months = tuple(("Jan","Feb","Mar","Apr", "May"))
third_month = months[2]
print(third_month)

# unpacking a tuple 
student = ("Eric", 24, "Mombasa")
name = student[0]
age = student[1]
location = student[2]
print(f"The student's name is {name}, he is {age} years old and lives in {location}")

# concanetating tuples
fruits = ("apple","melon","grapes","banana")
vegetables = ("cabbage","spinach","kale")

combined = fruits + vegetables 
total_no_of_items =  len(combined)      #finding the total no. of itemms in the combined tuples
print(f"The combined tuple has {total_no_of_items} items: {combined}") 

#Create a tuple of 7 days of the week. Print the weekend days only.
weekdays = tuple(("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")) 

weekend = weekdays[5],weekdays[6]
print(f"Weekend days are: {weekend}") 

#A program that takes a tuple of exam scores and finds the average without converting it to a list.
exam_scores = (54,56,78,90,75)
def average(scores):
    total = sum(scores)
    count = len(scores)
    avg = total/count
    print(f"The average score is: {avg}")

average(exam_scores)

#Combine two tuples of numbers and find the index of a specific number in the combined tuple.
tuple1 = (12,13,14,15)
tuple2 = (16,17,18,19)

combined = tuple1+ tuple2
index_of_number = combined.index(17)
print(f"The index of number 17 in the combined tuple is: {index_of_number}") 