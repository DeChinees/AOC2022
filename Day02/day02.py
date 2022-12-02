def outcome(player1, player2):
    score = 0    
    # player 2 losed
    if player1.lower() == 'a' and player2.lower() == 'z':
        score += 0 + 3
    if player1.lower() == 'c' and player2.lower() == 'y':
        score += 0 + 2
    if player1.lower() == 'b' and player2.lower() == 'x': 
        score += 0 + 1
    
    # player 2 wins
    if player1.lower() == 'c' and player2.lower() == 'x':
        score += 6 + 1
    if player1.lower() == 'b' and player2.lower() == 'z':
        score += 6 + 3
    if player1.lower() == 'a' and player2.lower() == 'y':
        score += 6 + 2
   
    # player 2 draw
    if player1.lower() == 'a' and player2.lower() == 'x':
        score += 3 + 1
    if player1.lower() == 'b' and player2.lower() == 'y':
        score += 3 + 2
    if player1.lower() == 'c' and player2.lower() == 'z':
        score += 3 + 3

    return score
    
file = open("input.txt", "r")
lines = file.readlines()
total = 0
count = 0

for line in lines:
    count += 1
    total += outcome(line[0], line[2])

print (f'{total}')