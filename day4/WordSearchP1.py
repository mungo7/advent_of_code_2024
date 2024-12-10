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

def CountMatches(line):
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
        #print(f"{x}, {y}, {grid[y][x]}")
        line += grid[y][x]
    #print(f"Row: {y+1}")
    xmas += CountMatches(line)

print(f"Matches after horizontal: {xmas}")

# Vertical matches
for x in range(grid_size[0]):
    line = ""
    for y in range(grid_size[1]):
        line += grid[y][x]
    #print(f"Column: {x+1}")
    xmas += CountMatches(line)



print(f"Matches after vertical: {xmas}")

# Diagonal up matches
for z in range(grid_size[1]):
    y = z
    x = 0
    line = ""
    while y >= 0 and x < grid_size[0]:
        line += grid[y][x]
        y-=1
        x+=1
    xmas += CountMatches(line)
    if CountMatches(line) > 0:
        print(line)


for z in range(grid_size[0]):
    x = z
    y = grid_size[1]-1
    line = ""
    while x < grid_size[0] and y > grid_size[1]:
        #print(f"({x}, {y})")
        line += grid[y][x]
        x+=1
        y-=1
    xmas += CountMatches(line)
    if CountMatches(line) > 0:
        print(line)

print(f"Matches after diagonal up: {xmas}")

for z in range(grid_size[1]):
    y = z
    x = 0
    line = ""
    while y < grid_size[1] and x < grid_size[0]:
        #print(f"({x}, {y})")
        line += grid[y][x]
        y+=1
        x+=1
    xmas += CountMatches(line)
    if CountMatches(line) > 0:
        print(line)

for z in range(grid_size[0]):
    x = z
    y = 0
    line = ""
    while x < grid_size[0] and y < grid_size[1]:
        #print(f"({x}, {y})")
        line += grid[y][x]
        x+=1
        y+=1
    xmas += CountMatches(line)
    if CountMatches(line) > 0:
        print(line)

print(f"Matches after diagonal down: {xmas}")
