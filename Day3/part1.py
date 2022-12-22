with open ("Day3\input.txt", "r") as input:
    data = (input.read()).split("\n")

item_score = 0

for row in data:
    firstpart, secondpart = row[:len(row)//2], row[len(row)//2:]
    x = {a for a in firstpart}
    y = {a for a in secondpart}
    intersection = x.intersection(y)
    for letter in intersection:
        if ord(letter) > 96:
            item_score += ord(letter) - 96
        elif ord(letter) > 64:
            item_score += ord(letter) - 64 + 26

print(f"Score of Overlapping Items are {item_score}")