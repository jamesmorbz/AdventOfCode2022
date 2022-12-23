stacks = [
    ["D", "B", "J", "V"],
    ["P", "V", "B", "W", "R", "D", "F"],
    ["R", "G", "F", "L", "D", "C", "W", "Q"],
    ["W", "J", "P", "M", "L", "N", "D", "B"],
    ["H", "N", "B", "P", "C", "S", "Q"],
    ["R", "D", "B", "S", "N", "G"],
    ["Z", "B", "P", "M", "Q", "F", "S", "H"],
    ["W", "L", "F"],
    ["S", "V", "F", "M", "R"],
]

with open ("Day5\input.txt", "r") as input:
    data = (input.read()).split("\n")[10:]

for row in data:
    _ , number, _ , source, _ , target = row.split(" ")
    number = int(number)
    source = int(source)
    target = int(target)

    for i in range(number):
        try:
            val = stacks[source-1].pop()
            stacks[target-1].append(val)
        except IndexError:
            pass

print("".join([l[-1] for l in stacks]))