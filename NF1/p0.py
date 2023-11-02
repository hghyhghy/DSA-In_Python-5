

# python program to check wheather a class has a subclass or not 

# creating the class

class Base:
    
    pass

# inheriting the class 

class Derived(Base):

    pass

# driver code 

print(issubclass(Derived,Base))

print(issubclass(Base,Derived))

# creating the objects to this class 

d=Derived()

b=Base()


print(isinstance(b,Derived))  # returns true if it is inherited from 

# the other class 

print(isinstance(d,Base))
