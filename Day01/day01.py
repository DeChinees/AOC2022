from curses.ascii import isdigit
from re import X


file = open("input.txt", "r")

list = []
x = 0

for line in file:
    if line != "\n":
        x += int(line)
    else:
        list.append(x)
        x=0    

# Most Calories 70509
print (f"Elf {list.index(max(list))} has the most calories of {max(list)}" )

# Top 3
sorted_list=list
sorted_list.sort(reverse=True)
print (f"Top 3: Elf #{list.index(sorted_list[0])} with {sorted_list[0]} \n \
      Elf #{list.index(sorted_list[1])} with {sorted_list[1]} \n \
      Elf #{list.index(sorted_list[2])} with {sorted_list[2]} \n \
Totals to {sorted_list[0]+sorted_list[1]+sorted_list[2]} ")