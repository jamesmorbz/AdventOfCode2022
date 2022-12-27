with open ("Day8\input.txt", "r") as input:
    data = (input.read()).split("\n")
data = [list( map(int,i) ) for i in data]

max = 0 
for row_index, row in enumerate(data):
    for column_index, cell in enumerate(row):
        left = 0
        down = 0
        up = 0
        right = 0
         
        if column_index == 0 or row_index == 0 or column_index == len(row)-1 or row_index == len(data)-1:
            continue

        for left_cell in data[row_index][column_index+1:]:
            left += 1
            if cell > left_cell:
                continue  
            if cell <= left_cell:
                break

        for right_cell in list(reversed(data[row_index][:column_index])):
            right += 1
            if cell > right_cell:
                continue 
            if cell <= right_cell:
                break
       
        for row in list(reversed(data[:row_index])):
            up += 1
            if cell > row[column_index]:
                continue 
            if cell <= row[column_index]:
                break
        
        for row in data[row_index+1:]:
            down += 1
            if cell > row[column_index]:
                continue 
            if cell <= row[column_index]:
                break

        current = up * down * left * right
     
        if current > max:
            max = current

print(max)