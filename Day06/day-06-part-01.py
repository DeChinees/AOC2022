# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw

with open('Day06/test.txt', 'r') as file:
    line = file.read()

stream = list("bvwbjplbgvbhsrlpgdmjqwftvncz")
start = stream[0:]
print(f"{stream}")
print(f"First 3 chars: {start}")


for c in stream[1:]:
    if (c not in start):
        print(f"")
        start.append(c)
    if start:
        if (c == "j"):
            print(f"J found at index: {stream.index(c)}")