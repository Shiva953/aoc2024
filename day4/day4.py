def read_input(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    
    row_array = lines
    
    num_columns = len(lines[0])
    column_array = [''.join(line[col] for line in lines) for col in range(num_columns)]
    
    return row_array, column_array

row_array, column_array = read_input('input.txt')

#horizontal search(left + right)
c1 = 0
for row in row_array:
    c_a = row.count('XMAS')
    c_rev_1 = row[::-1].count('XMAS')
    c1 += c_a + c_rev_1

#vertical search(top + down)
c2 = 0
for column in column_array:
    c_b = column.count('XMAS')
    c_rev_2 = column[::-1].count('XMAS')
    c1 += c_b + c_rev_2

def has_xmas(rowCount, col):
    x1 = (rowCount <= len(row_array) - 4 and col <= len(column_array) - 4) and (row_array[rowCount][col] == 'X' and row_array[rowCount+1][col+1] == 'M' and row_array[rowCount+2][col+2] == 'A' and row_array[rowCount+3][col+3] == 'S')
    x2 = (rowCount <= len(row_array) - 4 and col >= 3) and (row_array[rowCount][col] == 'X' and row_array[rowCount+1][col-1] == 'M' and row_array[rowCount+2][col-2] == 'A' and row_array[rowCount+3][col-3] == 'S')
    x3 = (rowCount >= 3 and col >= 3) and ((row_array[rowCount][col] == 'X' and row_array[rowCount-1][col-1] == 'M' and row_array[rowCount-2][col-2] == 'A' and row_array[rowCount-3][col-3] == 'S'))
    x4 = (rowCount >= 3 and col <= len(column_array) - 4) and ((row_array[rowCount][col] == 'X' and row_array[rowCount-1][col+1] == 'M' and row_array[rowCount-2][col+2] == 'A' and row_array[rowCount-3][col+3] == 'S'))
    return x1 or x2 or x3 or x4

# Diagonal search (top left, top right, bottom left, bottom right)
c3 = 0
for rowCount in range(len(row_array)):
    for col in range(len(column_array)):
        # Bottom right diagonal
        if (rowCount <= len(row_array) - 4 and col <= len(column_array) - 4):
            if (row_array[rowCount][col] == 'X' and 
                row_array[rowCount+1][col+1] == 'M' and 
                row_array[rowCount+2][col+2] == 'A' and 
                row_array[rowCount+3][col+3] == 'S'):
                c3 += 1

        # Bottom left diagonal
        if (rowCount <= len(row_array) - 4 and col >= 3):
            if (row_array[rowCount][col] == 'X' and 
                row_array[rowCount+1][col-1] == 'M' and 
                row_array[rowCount+2][col-2] == 'A' and 
                row_array[rowCount+3][col-3] == 'S'):
                c3 += 1

        # Top left diagonal
        if (rowCount >= 3 and col >= 3):
            if (row_array[rowCount][col] == 'X' and 
                row_array[rowCount-1][col-1] == 'M' and 
                row_array[rowCount-2][col-2] == 'A' and 
                row_array[rowCount-3][col-3] == 'S'):
                c3 += 1

        # Top right diagonal
        if (rowCount >= 3 and col <= len(column_array) - 4):
            if (row_array[rowCount][col] == 'X' and 
                row_array[rowCount-1][col+1] == 'M' and 
                row_array[rowCount-2][col+2] == 'A' and 
                row_array[rowCount-3][col+3] == 'S'):
                c3 += 1

ans = c1 + c2 + c3
print(ans)

#part2