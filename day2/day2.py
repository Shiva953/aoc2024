def read_input_file(filename):
    input_array = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = [int(num) for num in line.strip().split()]
                input_array.append(row)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except ValueError:
        print("Error: Invalid input. Ensure all entries are integers.")
        return []
    
    return input_array


inputList = read_input_file("input.txt")

#part 1
def check_safe_part_1(arr):
    ans = True
    # check strictly inc/dec + max (diff btw 2 adjacent nums) = 3, min diff = 1
    for i in range(0, len(arr)-1):
        if(((arr[0] < arr[1] and arr[i] < arr[i+1]) or (arr[0] > arr[1] and arr[i] > arr[i+1])) and (1 <= abs(arr[i+1] - arr[i]) <= 3)):
            continue;
        else: 
            return False;
    return ans;

safeRows = 0
for row in inputList:
    if(check_safe_part_1(row)):
        safeRows +=1;

print(f"Safe Rows Part 1 {safeRows}")


#part 2
def check_safe_part_2(arr):
    if(check_safe_part_1(arr)):
        return True;
    #same check, just try removing one element each time
    ans = False
    for i in range(0,len(arr)):
        if(check_safe_part_1((arr[:i] + arr[i+1:]))):
            return True;
        else:
            continue;
    return ans

safeRowsWithPoppin = 0
for row in inputList:
    if(check_safe_part_2(row)):
        safeRowsWithPoppin +=1;

print(f"Safe Rows Part 2 {safeRowsWithPoppin}")
    