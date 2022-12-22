with open ("Day1\input.txt", "r") as input:
    data = input.read()

data = data.split("\n\n")
data = [list(map(int,row.split("\n"))) for row in data]
summed_rows = [sum(row) for row in data]
max_values = sorted(summed_rows, reverse=True)[:3]
elf_numbers = [summed_rows.index(max_value)+1 for max_value in max_values]  # No 0th Elf.

print(f"Elf Numbers {elf_numbers} have the most calories. They are carrying {sum(max_values)} calories.")