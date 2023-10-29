

# introduction of chainmap

# it is uesd to ecapsulate all dictionaries elements 

from collections import ChainMap

# creating  dictionaries 

d={1:"s",2:"u"}

d1={3:"b",4:"h"}

d2={5:"a",6:"m"}

# encapsulating the elements 

c=ChainMap(d,d1,d2)

print(c)