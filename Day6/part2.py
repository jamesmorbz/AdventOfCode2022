with open ("Day6\input.txt", "r") as input:
    data = input.read()

store = []
for counter, char in enumerate(data):
    store.append(char)
    if len(store) > 14:
        store.pop(0)
    if len(set(store)) == 14:
        print(f"First Buffer Signal Found {counter+1}")
        break