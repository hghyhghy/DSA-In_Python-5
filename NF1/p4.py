

# sorting opertion in the list 

l1=[3,2,5,4,7,6,9,8,0,1]

print("The original list is ")


for i in l1:

    print(i, end=" ") 

# sorting the elements 

l1.sort()

print("The list after sorting ")

for j in range(0,len(l1)):

    print(l1[j], end=" ")



# reversing the  elements 

l1.reverse()


print("After reversing the list becomes")

for m in range(0,len(l1)):

    print(l1[m], end=" ")

# extending the list by another 

l2=[66,77,89,99]

l1.extend(l2)

print("After extending the list becomes ")

for n in range(0,len(l1)):

    print(l1[n], end=" ")


    