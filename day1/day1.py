def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        column1 = []
        column2 = []

    for line in lines:
        numbers = line.strip().split()

        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))
    
    return column1, column2

first_column, second_column = read_input_file("input.txt")

first_column.sort()
second_column.sort()

#part 1
total_dist = sum(abs(first_column[i] - second_column[i]) for i in range(len(first_column)))
print(total_dist)

# part 2
# res = sum(each element in left list * no of times it appears in the right list)
res = sum(el*second_column.count(el) for el in first_column)

print(f"Result: {res}")
