import sys
import re

input = open(sys.argv[1], 'r').readlines()
grid=[]
for line in input:    
    grid.append([letter for letter in str(line).strip()]) 

for row in grid:
    print(row)
            #  right  up      left      down 
directions = ((0, 1), (1, 0), (-1, 0), (0, -1), 
              (1, 1), (-1, 1), (-1, -1), (1, -1) )

grid_size = (len(grid[0]), len(grid))

def count_matches(line):
    pattern=r'XMAS'
    matches=list(re.findall(pattern, line))
    pattern=r'SAMX'
    matches += list(re.findall(pattern, line))
    return len(matches)

xmas = 0
# Horizontal matches
for y in range(grid_size[1]):
    line = ""
    for x in range(grid_size[0]):
        line += grid[y][x]
    xmas += count_matches(line)

# Vertical matches
for x in range(grid_size[0]):
    line = ""
    for y in range(grid_size[1]):
        line += grid[y][x]
    xmas += count_matches(line)

print(f"Matches after vertical: {xmas}")

# Diagonal up matches

# DU - Scan down

for z in range(grid_size[1]):
    y = z
    x = 0
    line = ""
    while y >= 0:
        line += grid[y][x]
        y-=1
        x+=1
    xmas += CountMatches(line)
    if CountMatches(line) > 0:
        print(line)

# DU - Scan right
for z in range(1, grid_size[0]):
    x = z
    y = grid_size[1]-1
    line = ""
    while x < grid_size[0]:
        #print(f"({x}, {y})")
        line += grid[y][x]
        x+=1
        y-=1
    xmas += count_matches(line)

# DD - Scanning down
for z in range(grid_size[1]):
    y = z
    x = 0
    line = ""
    while y < grid_size[1]:
        line += grid[y][x]
        y+=1
        x+=1
    xmas += count_matches(line)

# DD - Scanning right
for z in range(1, grid_size[0]):
    x = z
    y = 0
    line = ""
    while x < grid_size[0]:
        line += grid[y][x]
        x+=1
        y+=1
    xmas += count_matches(line)
