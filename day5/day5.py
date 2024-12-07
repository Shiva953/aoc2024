def parse_input_file(filename):
    pairs_list = []
    number_lists = []

    parsing_pairs = True
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if ',' in line:
                parsing_pairs = False
                number_lists.append([int(num) for num in line.split(',')])
            elif '|' in line:
                pair = [int(num) for num in line.split('|')]
                pairs_list.append(pair)
    
    return pairs_list, number_lists

pairlist, arr2 = parse_input_file('input.txt')

#part1&2
def is_valid_order(arr, pairlist):
    #better way to do the same [O(N) complexity]
    #here, instead of iterating in each element of arr and then having another loop, we are just comparing the indexes of pairlist [a,b]s in the given arr
    for x, y in pairlist:
        if x in arr and y in arr:
            if arr.index(x) >= arr.index(y):
                return False
    return True

def check(arr, pairlist):
    a = arr
    isValid = True
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] != arr[j]):
                if([arr[i], arr[j]] in pairlist):
                    continue
                else:
                    isValid = False
                    a[i], a[j] = a[j], a[i]
    return (isValid, a)


ans = 0
ans_2 = 0
for arr in arr2:
    x = check(arr, pairlist);
    if(x[0]):
        ans += arr[(len(arr)-1)//2]
    else:
        corrected_arr = x[1]
        ans_2 += corrected_arr[(len(arr)-1)//2]


print(len(arr2))
print(ans)
print(ans_2)