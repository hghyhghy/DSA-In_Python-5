

# popping the list from the list 

# creating a list first 

l1=[3,2,5,4,7,6,9,8,0,1]


print("The original list elements are ")


#using a for loop

for i in l1:

    print(i, end=" ") 

#popping element from the list 


l1.pop(5)

print("After popping the list becomes ")

for k in range(0,len(l1)):

    print(l1[k],end=" ")



# inserting new element in the list 

l1.insert(3,88)

print("After inserting the list becomes ")

for j in range(0,len(l1)):

    print(l1[j], end=" ")



# using remove func 

l1.remove(9)

print("After removing  one  element the list becomes ")

for m in range(0,len(l1)):

    print(l1[m], end=" ")







