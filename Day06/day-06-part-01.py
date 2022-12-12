# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw

with open('Day06/input.txt', 'r') as file:
    line = file.read()

    
stream = list(line)
streamlenth = len(stream)
window_size = 4


def dubcheck(block):
    hist=""
    for c in (block):
        if c in hist: 
            return False
        hist += c
    print(f"hist: {hist}")
    return True
        

if len(stream) <= window_size:
    print(f"{stream}")
for i in range(len(stream)):
    print(stream[i:i+window_size])
    if dubcheck(stream[i:i+window_size]):
        print (f"{i+window_size}")
        break
    
