# Lists store multiple items in a single variable, and they are ordered and changeable.
thislist = ["apple", "banana", "cherry"] 
print(thislist) 

#creating a list with the list() constructor
fruits = list(("banana","Watermelon","grapes")) 
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

import numpy as np 
# Exercises
counties = list(("Meru","Garissa","Nairobi","machakos","kisumu"))
favcounties = counties[0],counties[4] 

print(favcounties)  #print the 1st and last item

#add one more county and remove one
counties.append("Mombasa")
counties.remove("machakos")
print(counties)

scores = [45,78,56,89,90]
ave = np.mean(scores)      # average of the scores 
print(ave) 

descScores = sorted(scores,reverse=True) # sorting the scores in descending order
print(descScores) 

# replace score <50 with Fail
for i in range(len(scores)):
    if scores[i] < 50:
        scores[i] = "Fail"
        print(scores)

userinput = (23,34,100,54,451)

# a fn that takes a tuple of scores, converts it to a list, and then finds the max and min scores.
def convert_to_list(userinput):
    userlist = list(userinput) 
    max_score = np.max(userlist)
    min_score = np.min(userlist)
    print(f"The maximum score is: {max_score} and the minimum score is: {min_score}")



convert_to_list(userinput) 

# Write a program that asks the user for 10 numbers, stores them in a list, and then:
#Prints only the even numbers.
#Prints the sum of all odd numbers.

def even_odd_numbers():
    numbers = []
    #for i in range(numbers,10):
    num = int(input("Enter 10 numbers:"))
    numbers.append(num)
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2!= 0]
    print(f"Even numbers: {even_numbers}")
    print(f"Sum of Odd numbers: {sum(odd_numbers)}") 

#even_odd_numbers() 

#Create a list of student names. Sort them alphabetically, then reverse the order.
students = ["Hassan","KG","Musa","Aisha","Zahara"]

print(f"students sorted alphabetically: {sorted(students)}") 
print(f"students in reverse order: {sorted(students, reverse=True)}")

#Given a list of counties, remove duplicates while keeping the original order
counties = ["Meru","Garissa","Nairobi","machakos","kisumu","Meru","Nairobi"]

unique_counties = list(set(counties))  #removes duplicates but does not maintain the original order.
print(unique_counties)

print(list(dict.fromkeys(counties))) # another way to remove duplicates while keeping the original order.