assignments = []

with open('Day04/input.txt', 'r') as file:
    line = file.read()
    line2 = line.replace("-",",")
    line3 = line2.split("\n")

for i in line3:
    assignments.append([int(x) for x in i.split(",")])

sum = 0
for a in assignments:
    X = list(range(a[0],a[1]+1))
    Y = list(range(a[2],a[3]+1))
    print(f"X: {a[0]}-{a[1]} - Y: {a[2]}-{a[3]}")
    #print(f"X: {X} - Y: {Y}")
    if len(X) < len(Y):
        if (set(X).issubset(set(Y))):
            sum += 1
    else:
        if (set(Y).issubset(set(X))):
            sum += 1
print (f"Sum: {sum}")

