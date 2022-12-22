with open ("Day3\input.txt", "r") as input:
    data = (input.read()).split("\n")

item_score = 0
chunk_size = 3
data = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

for chunk in data:
    firstpart, secondpart, thirdpart = chunk
    x = {a for a in firstpart}
    y = {a for a in secondpart}
    z = {a for a in thirdpart}
    intersection = x.intersection(y, z)
    for letter in intersection:
        if ord(letter) > 96:
            item_score += ord(letter) - 96
        elif ord(letter) > 64:
            item_score += ord(letter) - 64 + 26

print(f"Score of Overlapping Items are {item_score}")