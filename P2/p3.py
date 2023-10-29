

import collections

d=collections.deque([1,3,2,5,4,7,6,9,8,3])

print("The original deque is ")

print(d)

# extending the deque 

d.extend([99,98,90])

print("The deque after extending ")

print(d)

print("Extending from the left side ")

d.extendleft([54,43,65])

print(d)

# rotate the deque 

print("After rotating the deque ")


d.rotate(-3)

print(d)

# reversing the deque 

print("After reversing the deque becomes ")

d.reverse()

print(d)