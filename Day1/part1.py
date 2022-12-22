with open ("Day1\input.txt", "r") as input:
    data = input.read()

data = data.split("\n\n")
data = [list(map(int,row.split("\n"))) for row in data]
summed_rows = [sum(row) for row in data]
max_value = max(summed_rows)
elf_number = summed_rows.index(max_value) + 1 # No 0th Elf.

print(f"Elf Number {elf_number} has the most calories. He is carrying {max_value} calories.")