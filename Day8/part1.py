with open ("Day8\input.txt", "r") as input:
    data = (input.read()).split("\n")
data = [list( map(int,i) ) for i in data]

count = 0 
for row_index, row in enumerate(data):
    for column_index, cell in enumerate(row):
        if column_index == 0 or row_index == 0 or column_index == len(row)-1 or row_index == len(data)-1:
            count += 1
        elif cell > max(data[row_index][:column_index]):
            count += 1
        elif cell > max(data[row_index][column_index+1:]):
            count += 1
        else:
            up_list = []
            down_list = []
            for row_counter, row in enumerate(data):
                if row_counter < row_index:
                    up_list.append(row[column_index])
                elif row_counter > row_index:
                    down_list.append(row[column_index])
            if up_list and cell > max(up_list):
                count += 1
            elif down_list and cell > max(down_list):
                count += 1
print(count)