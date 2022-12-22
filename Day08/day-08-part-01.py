# 30373
# 25512
# 65332
# 33549
# 35390

import numpy as np

data=np.empty((0,5),int)

file = open("Day08/test.txt", "r")
lines = file.readlines()

for line in lines:
    line = line.strip("\n")
    if len(line) > 0:
        part = [int(x) for x in line]
    data = np.append(data, np.array([part]), axis=0)

print(data)