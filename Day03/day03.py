from collections import Counter

def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())

def common(str1,str2):
     
    # convert both strings into counter dictionary
    dict1 = Counter(str1)
    dict2 = Counter(str2)
 
    # take intersection of these dictionaries
    commonDict = dict1 & dict2
 
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

file = open("input.txt", "r")
lines = file.readlines()
rugsack = 0
for line in lines:
    n = len(line)
    item1 = line[0:n//2]
    item2 = line[n//2:]
    rugsack += 1
    print (f"rugsack {rugsack}")
    print (f"Item 1: {item1}")
    print (f"Item 2: {item2}")
    print (f"Number of common char found: {shared_chars(item1, item2)}")
    print (f"Common char: {common(item1, item2)}\n---")