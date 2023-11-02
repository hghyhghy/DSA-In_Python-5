

# some list operations 

# creating a list first

l=[2,1,3,4,3,5,6]

print("The length of the list is ")

print(len(l))

print("The minimum element from the list is ")

print(min(l))

print("The maximum element from the list is ")

print(max(l))

print("The first occurance of 3 is")

print(l.index(3))

print("The total occurance of 3 is ")

print(l.count(3))

# deleting elements  from the list 

l1=[3,2,5,4,7,6,9,8,0,1]

del l1[2:5]

print("List  elements after deleting ")

# using a for loop 

for i in range(0,len(l1)):

    print(l1[i], end=" ")


print("\r")



 