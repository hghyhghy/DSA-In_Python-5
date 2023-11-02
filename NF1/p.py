

from collections import Counter

# counter problems in python 

coun=Counter()

# creating a list


coun.update([1,2,3,5,4,1,1,2,9])

print("The occurances of the numbers are ")

print(coun)

coun.update([3,7,4])

print("After update the occurances are ")

print(coun)

# counting the occurances of a list of strings

# creating a list 

z=["blue","black","yellow","blue","cock","hen","cock"]

print(Counter(z))

# iterating through a dictionary 

my_counter=Counter('abcfgadasdsdsfgsg')

# printing the keys 

print(my_counter.keys())

#printing the values 

print(my_counter.values())

# printing them both 

print(my_counter.items())





