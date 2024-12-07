def read_grid_from_file(filename):
    """
    Read a grid from a file and convert it into a 2D list.
    
    Args:
        filename (str): Path to the input file
    
    Returns:
        list: 2D list representing the grid
    """
    with open(filename, 'r') as file:
        # Read all lines and strip whitespace
        lines = [line.strip() for line in file.readlines()]
    
    # Convert each line into a list of characters
    grid = [list(line) for line in lines]
    
    return grid

def print_grid(grid):
    """
    Print the grid in a readable format.
    
    Args:
        grid (list): 2D list representing the grid
    """
    for row in grid:
        print(''.join(row))

def count_characters(grid, char='#'):
    """
    Count the occurrences of a specific character in the grid.
    
    Args:
        grid (list): 2D list representing the grid
        char (str, optional): Character to count. Defaults to '#'.
    
    Returns:
        int: Number of occurrences of the character
    """
    count = sum(row.count(char) for row in grid)
    return count

def find_character_positions(grid, char='^'):
    """
    Find all positions of a specific character in the grid.
    
    Args:
        grid (list): 2D list representing the grid
        char (str, optional): Character to locate. Defaults to '^'.
    
    Returns:
        list: List of (row, column) tuples where the character is found
    """
    positions = []
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == char:
                positions.append((row_idx, col_idx))
    return positions

# Read the grid from input.txt
grid = read_grid_from_file('input.txt')

# Print basic grid information
print(f"Grid dimensions: {len(grid)} rows x {len(grid[0])} columns")

# Count '#' characters
hash_count = count_characters(grid, '#')
print(f"Number of '#' characters: {hash_count}")

# Find positions of special characters (like '^')
special_position_player = find_character_positions(grid, '^')
print("Character position of ^ : ", special_position_player[0])

# # Optional: Print the entire grid
# print("\nGrid contents:")
# print_grid(grid)

start_position = (-1,-1)
dir_unit_vectors = [(-1,0),(1,0),(0,1),(0,-1)] #left,right,top,down

#NOW, start the TETRIS and movement of ^ as a f(#, unit vectors)[it rotates by 90 deg right on hitting #, else forward in that unit vec dir]
start_position = special_position_player[0]
start_direction = (0,1)
direction = start_direction
#1. AS LONG AS # ISN'T ON THE NEXT ROW/COLUMN, DIRECTION REMAINS SAME
#2. ON HITTING #, (x,y) becomes (-y, x) where x,y => [-1,1,0][flip the 1s and 0s and multiply y by -1]

playerPositionCount = 0
position = start_position
# x = position[0]
# y = position[1]
# x_dir = direction[0]
# y_dir = direction[1]
#move the ^ on the unit vector by a unit each time until #
while(grid[position[0]][position[1]] != '#'):
    x_dir = direction[0]
    y_dir = direction[1]
    x = position[0]
    y = position[1]
    next_x = x + x_dir
    next_y = y + y_dir
    boundary = (next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]))
    if(not boundary):
        if((x == len(grid) and direction==(0,-1)) or (x == 0 and direction==(0,1)) or (y == len(grid) and direction==(1,0)) or (y == 0 and direction==(-1,0))):
            break;
        if(grid[x+x_dir][y+y_dir] == '#'):
            direction = (y_dir, -1*x_dir)
        else:
            position = (x + x_dir, y + y_dir)
            playerPositionCount+=1;

print(playerPositionCount)
    