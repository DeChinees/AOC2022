#     [H]         [D]     [P]        
# [W] [B]         [C] [Z] [D]        
# [T] [J]     [T] [J] [D] [J]        
# [H] [Z]     [H] [H] [W] [S]     [M]
# [P] [F] [R] [P] [Z] [F] [W]     [F]
# [J] [V] [T] [N] [F] [G] [Z] [S] [S]
# [C] [R] [P] [S] [V] [M] [V] [D] [Z]
# [F] [G] [H] [Z] [N] [P] [M] [N] [D]
#  1   2   3   4   5   6   7   8   9 

s1=["F","C","J","P","H","T","W"]
s2=["G","R","V","F","Z","J","B","H"]
s3=["H","P","T","R"]
s4=["Z","S","N","P","H","T"]
s5=["N","V","F","Z","H","J","C","D"]
s6=["P","M","G","F","W","D","Z"]
s7=["M","V","Z","W","S","J","D","P"]
s8=["N","D","S"]
s9=["D","Z","S","F","M"]

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# s1=["Z","N"]
# s2=["M","C","D"]
# s3=["P"]


moves = []

with open('Day05/input.txt', 'r') as file:
    line = file.read()
    line2 = line.replace("move ","")
    line3 = line2.replace("from ",",")
    line4 = line3.replace("to ", ",")
    line5 = line4.split("\n")

for i in line5:
    moves.append([int(x) for x in i.split(",")])

#print(f"Moves: {moves}")

def shuffle(target, x):
    print(f"target {target}, crate: {x}")
    if target == 1:
        s1.append(x)
    if target == 2:
        s2.append(x)
    if target == 3:
        s3.append(x)
    if target == 4:
        s4.append(x)
    if target == 5:
        s5.append(x)
    if target == 6:
        s6.append(x)
    if target == 7:
        s7.append(x)
    if target == 8: 
        s8.append(x) 
    if target == 9:
        s9.append(x)

def movecrates(crates, source, target):
    print(f"crates: {crates}, source: {source}, target: {target}")
    if source == 1:
        y = s1[-crates:]
        for x in y:
            shuffle(target, x)
            del s1[-1]               
    if source == 2:
        y = s2[-crates:]
        for x in y:
            shuffle(target, x)
            del s2[-1]
    if source == 3:
        y = s3[-crates:]
        for x in y:
            shuffle(target, x)
            del s3[-1]
    if source == 4:
        y = s4[-crates:]            
        for x in y:
            shuffle(target, x)
            del s4[-1]
    if source == 5:
        y = s5[-crates:]            
        for x in y:
            shuffle(target, x)
            del s5[-1]
    if source == 6:
        y = s6[-crates:]            
        for x in y:
            shuffle(target, x)
            del s6[-1]
    if source == 7:
        y = s7[-crates:]            
        for x in y:
            shuffle(target, x)
            del s7[-1]
    if source == 8:
        y = s8[-crates:]            
        for x in y:
            shuffle(target, x)
            del s8[-1]
    if source == 9:
        y = s9[-crates:]            
        for x in y:
            shuffle(target, x)
            del s9[-1]

c = 0
for m in moves:
    c += 1
    print(f"Move {c}:\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}\n{s6}\n{s7}\n{s8}\n{s9}")
    movecrates(m[0],m[1],m[2])
    # if (c % 10) == 0:
    #     input("Press Enter to continue... ") 

print(f"Final: {s1}\n{s2}\n{s3}\n{s4}\n{s5}\n{s6}\n{s7}\n{s8}\n{s9}")
#print(f"{s1}\n{s2}\n{s3}")