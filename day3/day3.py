import re

def parse_corrupted_memory(memory_string):
    pattern = r'mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

    matches = re.findall(pattern, memory_string)
    results = []
    for x, y in matches:
        results.append(int(x) * int(y))
    
    return results

def solve_corrupted_memory(memory_string):
    mul_results = parse_corrupted_memory(memory_string)
    total_sum = sum(mul_results)
    
    return total_sum, mul_results

#part1
def solve_puzzle_from_file(filename):
    with open(filename, 'r') as file:
        memory_string = file.read().strip()

    total, results = solve_corrupted_memory(memory_string)
    
    print("Puzzle Solution:")
    print(f"Valid mul instructions: {results}")
    print(f"Total sum of multiplications: {total}")
    
    return total

solve_puzzle_from_file('input.txt')
