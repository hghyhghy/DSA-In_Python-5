

# accessing elements from a deque 

import collections

d=collections.deque([1,3,2,5,4,7,6,9,8,3])

print("The original deque is ")
print(d)

print("The number 4 first occurance  ")

print(d.index(4))

# inserting new elements in the list 


d.insert(2,0)

print("After inserting new element the deque becomes ")

print(d)

# counting the occurances 

print(f"The occurance of no 3 in the deque {d} is ")

print(d.count(3))


# removing an element from the deque 

d.remove(3)

print("The  deque after removing one element")


print(d)