# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw

with open('Day06/test.txt', 'r') as file:
    line = file.read()

stream = list("bvwbjplbgvbhsrlpgdmjqwftvncz")
streamlenth = len(stream)
s_pos = 0
e_pos = 3
block = ""

#print(f"{stream}")
print(f"{stream[0:2]}")
#print(f"First 3 chars: {start}")

while s_pos < streamlenth -1:
    print(f"s_pos: {stream[s_pos:e_pos:]}")
    block = stream[s_pos:e_pos:]
    if not (set(stream[e_pos+1]).issubset(set(block))):
        print(f"at index {e_pos+1} the char {stream[e_pos+1]} is subset of {block}")
    else:
        s_pos += 1          # we move block one step to right
        e_pos = s_pos+3
        block = stream[s_pos:e_pos:]
    
