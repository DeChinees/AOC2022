from collections import Counter

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

file = open("Day03/test.txt", "r")
lines = file.readlines()

sum = 0
rugsack = 0
priority=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", \
          "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for line in lines:
    n = len(line)
    item1 = line[0:n//2]
    item2 = line[n//2:]
    rugsack += 1
    print (f"rugsack {rugsack}")
    print (f"Item 1: {item1}")
    print (f"Item 2: {item2}")
    print (f"Common char: {common(item1, item2)[0]} @ {priority.index(common(item1, item2)[0])}\n---") 
    sum += 1 + priority.index(common(item1, item2)[0]) # plus one to correct array count 

print (f"Sum: {sum}")