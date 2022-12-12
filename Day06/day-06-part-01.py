# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw

with open('Day06/input.txt', 'r') as file:
    line = file.read()

    
str="mjqjpqmgbljsphdztnvjfqwrcgsmlb"
stream = list("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
streamlenth = len(stream)
window_size = 4
# e_pos = 3
# block = ""

# print(f"{stream}")
# #print(f"{stream[0:2]}")
# #print(f"First 3 chars: {start}")

# print(f"Starting at {stream[s_pos:e_pos]}")
# block = stream[s_pos:e_pos]



if len(stream) <= window_size:
    print(f"{stream}")
for i in range(len(stream)):
    print(stream[i:i+window_size])
    

        

# while s_pos < streamlenth -1:
#     print(F"e_pos: {stream[e_pos]}")
#     if (set(stream[e_pos]).issubset(set(block))):
#         print(f"at index {e_pos} the char {stream[e_pos]} is in subset of {block}")
#         s_pos=e_pos
#         e_pos = s_pos+3
#         block = stream[s_pos:e_pos]
#         print(f"new block: {block}")
#     else:
#         if not (set(stream[e_pos]).issubset(set(block))):
#             print(f"at index {stream.index(stream[e_pos])} the char {stream[e_pos]} is in NOT subset of {block}")
#             s_pos += 1          # we move block one step to right
#             e_pos = s_pos+3
#             block = stream[s_pos:e_pos]
        
#     if e_pos+1 >= streamlenth: 
#         break