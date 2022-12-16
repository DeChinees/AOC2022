import pathlib

# Represents a node of an n-ary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.child = []
   
 # Utility function to create a new tree node
def newNode(key):   
    temp = Node(key)
    return temp

def printTree(root):
    t = []
    t.append(root)
    print(f"{len(t)}")

if __name__== "__main__":
    input = pathlib.Path("Day07/test.txt").read_text().split("\n")
    print(f"{input}")

    root = newNode("/")
    for i in input:
        match i.split(" "):
            case "$", "cd", directory:
                if directory != "..":
                    print(directory)
                    (root.child).append(newNode(directory))
            case size, _:
                (root.child[0].child).append(newNode(666));
            case other:
                continue  

    printTree(root)