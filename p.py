

# generators in python 

def simplegenerator():

    yield 1

    yield 2

    yield 3


# the yield keyword is used to create generator

# driver code to check above generator 

for i in simplegenerator():

    print(i)

