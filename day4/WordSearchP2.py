import sys

input = open(sys.argv[1], 'r').readlines()
grid=[]
for line in input:    
    grid.append([letter for letter in str(line).strip()]) 

grid_size = (len(grid[0]), len(grid))
match = 0

for y in range(1, grid_size[1]-1):
    for x in range(grid_size[0]-1):
        if grid[y][x] == 'A':
            # If upright and downleft include M and S
            upright = grid[y-1][x+1]
            downleft = grid[y+1][x-1]
            letters = upright + downleft
            # If upleft and downright include M and S
            upleft = grid[y-1][x-1]
            downright = grid[y+1][x+1]
            letters2 = upleft + downright
            if "M" in letters and "S" in letters and "M" in letters2 and "S" in letters2:
                match += 1
print(f"X-MAS Matches: {match}")

