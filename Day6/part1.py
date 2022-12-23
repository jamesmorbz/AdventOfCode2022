with open ("Day6\input.txt", "r") as input:
    data = input.read()

store = []
for counter, char in enumerate(data):
    store.append(char)
    if len(store) > 4:
        store.pop(0)
    if len(set(store)) == 4:
        print(f"First Buffer Signal Found {counter+1}")
        break