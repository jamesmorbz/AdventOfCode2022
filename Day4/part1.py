with open ("Day4\input.txt", "r") as input:
    data = (input.read()).split("\n")

data = [x.split(",") for x in data]

count = 0
for row in data:
    first_elf, second_elf = row
    first_elf_min, first_elf_max = first_elf.split("-")
    second_elf_min, second_elf_max = second_elf.split("-")
    first_elf_min = int(first_elf_min)
    first_elf_max = int(first_elf_max)
    second_elf_min = int(second_elf_min)
    second_elf_max = int(second_elf_max)

    first_elf_set = {i for i in range(first_elf_min, first_elf_max+1)}
    second_elf_set = {i for i in range(second_elf_min, second_elf_max+1)}
    
    if first_elf_set.intersection(second_elf_set) == second_elf_set or first_elf_set.intersection(second_elf_set) == first_elf_set:
        count += 1

print(f"Number of Elves Sections overlapping - {count}")