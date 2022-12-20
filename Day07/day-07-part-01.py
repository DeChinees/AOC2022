import pathlib

dir_size = {}
dir_stack = []

input = pathlib.Path('Day07/test.txt').read_text().split("\n")
print(f"{input}")

for i in input:
    match i.split(" "):
        case '$', 'cd', directory:
            if directory == '..':
                dir_stack.pop()
            else:
                dir_stack.append(directory)
        case '$', 'ls':
            continue
        case 'dir', _:
            continue
        case size, _:
            for idx in range(len(dir_stack)):
                curr_path = '/' if idx == 0 else '/'.join(dir_stack[:idx+1])[1:]
            if curr_path not in dir_size:
                dir_size[curr_path] = 0
            dir_size[curr_path] += int(size)
        case other:
            continue        


s=0
# #s = sum([size for size in dir_size.values() if size <= 100000])
# for size in dir_size.values():
#     if size <= 100000:
#         print(f"dir_size:{size}")
#         s += size
# print(f"total:{s}")
# #print(f"dir_stack:{dir_stack}")

for dir, size in dir_size.items():
    if size <= 100000:
        print(f"dir: {dir} - size:{size}")
    