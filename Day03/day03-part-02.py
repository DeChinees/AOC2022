import numpy as np
from collections import Counter

def common(str1,str2, str3):
     
    # convert both strings into counter dictionary
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    dict3 = Counter(str3)
 
    # take intersection of these dictionaries
    commonDict = dict1 & dict2 & dict3
 
    if len(commonDict) == 0:
        print (-1)
        return
 
    # get a list of common elements
    commonChars = list(commonDict.elements())
 
    # sort list in ascending order to print resultant
    # string on alphabetical order
    commonChars = sorted(commonChars)
 
    # join characters without space to produce
    # resultant string
    return (''.join(commonChars))

sum = 0
priority=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", \
          "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

items = []

with open('Day03/input.txt', 'r') as file:
    line = file.read()
    items = line.split("\n")

nparray = np.array(items)
newarr = nparray.reshape(100,3)

for x in newarr:
    # print(f"{x[0]}")
    # print(x)
    print (f"Common char: {common(x[0], x[1], x[2])[0]}") 
    sum += 1 + priority.index(common(x[0], x[1], x[2])[0]) # plus one to correct array count 

print (f"Sum: {sum}")