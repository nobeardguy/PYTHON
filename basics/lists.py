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

userinput = (23,34,100,54,45)

# a fn that takes a tuple of scores, converts it to a list, and then finds the max and min scores.
def convert_to_list(userinput):
    userlist = list(userinput) 
    max_score = np.max(userlist)
    min_score = np.min(userlist)
    print(f"The maximum score is: {max_score} and the minimum score is: {min_score}")



convert_to_list(userinput) 

#new file and loissts