# X = lose
# Y = draw
# Z = win
# A Y  
# B X
# C Z

def newoutcome(player1, result):
    score = 0    
    # Need to be a draw
    if player1.lower() == 'a' and result.lower() == 'y':
        score += 3 + 1
    if player1.lower() == 'b' and result.lower() == 'y':
        score += 3 + 2
    if player1.lower() == 'c' and result.lower() == 'y':
        score += 3 + 3

    # need to lose
    if player1.lower() == 'a' and result.lower() == 'x':
        score += 0 + 3
    if player1.lower() == 'b' and result.lower() == 'x':
        score += 0 + 1
    if player1.lower() == 'c' and result.lower() == 'x':
        score += 0 + 2

    # need to win
    if player1.lower() == 'a' and result.lower() == 'z':
        score += 6 + 2
    if player1.lower() == 'b' and result.lower() == 'z':
        score += 6 + 3
    if player1.lower() == 'c' and result.lower() == 'z':
        score += 6 + 1
    return score

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
total_part1 = 0
total_part2 = 0

for line in lines:
    total_part1 += outcome(line[0], line[2])
    total_part2 += newoutcome(line[0], line[2])

print (f'part 1: {total_part1}')
print (f'part 2: {total_part2}')
