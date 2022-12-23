from collections import defaultdict

with open ("Day7\input.txt", "r") as input:
    data = (input.read()).split("\n")

size = defaultdict(int)
path = []
for line in data:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])
        for i in range(1, len(path)+1):
            size['/'.join(path[:i])] += sz

max_used = 70000000 - 30000000
total_used = size['/']
need_to_free = total_used - max_used


count = 10000000000
for k,v in size.items():
    if v>=need_to_free:
        count = min(count, v)

print(count)