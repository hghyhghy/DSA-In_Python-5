

# getting the double and cube of a number 


class X:

    # the constructor 

    def __init__(self,a):

        self.num=a

    def ofdouble(self):

        self.num*=2

# inheriting the class       

class Y(X):

    def __init__(self, a):
        
        X.__init__(self,a)
    

    def ofcube(self):

        self.num*=3


# creating an object 

obj=Y(4)

print(obj.num)

obj.ofdouble()

print(obj.num)

obj.ofcube()

print(obj.num)


      