

def fib(limit):

    a=0

    b=1

    # one by one yielding the values 

    while a<limit:

     yield a

     a,b=b,a+b



x=fib(6)

#printing the elements 


print(next(x))

print(next(x))

print(next(x))

print(next(x))

print(next(x))

print(next(x))


# generator expression using for loop 

generator_exp=(i*5 for i in range(5) if i%2==0)


for i in generator_exp:
   
   print(i)
