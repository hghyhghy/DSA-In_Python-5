

# some lamda function 

calc=lambda num:"Even number" if num%2==0 else "Odd number"

print(calc(20))

# printing the cube of a number by using a function and a lamda 

# creating a function

def ofcube(y):

    print(f"The cube of the number {y} is ")

    return y*y*y


# by using lamda function 

lambdacube=lambda num:num*num*num

print("Invoking the function with def keyword ")

print(ofcube(3))

print("Invoking the function with lamda keyword ")

print(lambdacube(4))
 
# using the lamda to filter out even numbers from the list 

mylist=[2,3,4,1,6,7]

my_list=list(filter(lambda x: x%2!=0,mylist))

print(mylist)