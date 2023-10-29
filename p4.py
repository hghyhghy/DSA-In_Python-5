

# python code to print key val pairs of dictionary 


d={1:"subham",2:"His Mom"}

print("The key value pair of the dictionary is ")

for i,j in d.items():

    print(i,j)


# printing the list in a sorted oreder 


# creating a list 


lis=[1,3,2,1,4,5,9,8]

print("The list in the  sorted order is ")

# using for loop 

for i in sorted(lis):

    print(i, end=" ")



# loops for removing dulicate occurances 

print("The sorted list without duplicate numbers are")


for k in  sorted(set(lis)):

    print(k,end=" ")


# printing the list in a reversed  order 


l=[1,2,3,4,5,7,6]

print(f"The list {l} in a reversed order is ")

for i in reversed(l):

    print(i, end=" ")


# printing numbers in a gap of 3  from  1 to 10

for i in reversed(range(1,10,3)):

    print(i)