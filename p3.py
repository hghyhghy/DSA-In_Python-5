

# different looping techniques in python

# enumerator 

for key,value in enumerate(["vijay","sujay","dhananjay","kalisay"]):

    print(key,value)

for key,value in enumerate(["vijay","sujay","dhananjay","kalisay"]):
    
    print(value,end=" ")



# creating two lists 

names=["subham","shreyoshi","nabanita"]

age=(20,19,21)

# using zip() to combine two containers 

for n,a in zip(names,age):

    print("Name",n)

    print("Age",a)

    print()

