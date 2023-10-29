
#  use of generator object 


def simplegen():

    yield 1

    yield 2

    yield 3


# creating an object of that class 

x=simplegen()

# iterating over the generator 

# using next()

print(next(x))

print(next(x))

print(next(x))
