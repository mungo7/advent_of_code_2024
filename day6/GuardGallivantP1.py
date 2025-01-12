import numpy as np
import sys

visited = set()

def process_input(input):
    lab_grid=[]
    guard_pos = np.array([0,0])
    y_tracker = 0 
    for line in input:
        lab_grid.append([letter for letter in line.strip()])
        for letter in line:
            if letter == '^': # Get guard pos
                guard_pos = [y_tracker, line.index(letter)]
        y_tracker+=1
    return lab_grid, guard_pos

def guard_walk(lab_grid, guard_pos, direction):
    end = False
    while not end:
        visited.add(tuple(guard_pos))
        new_pos = [guard_pos[0]+direction[0], guard_pos[1]+direction[1]]
        if any(new_pos[i] == -1 or new_pos[i] == len(lab_grid) for i in range(2)):
            break
        if lab_grid[new_pos[0]][new_pos[1]] == '#':
            rotation_matrix = np.array([[0,1], [-1,0]])
            direction = np.dot(rotation_matrix, direction)
        else:
            guard_pos = new_pos

def main():
    input = open(sys.argv[1]).readlines()
    lab_grid, guard_pos = process_input(input)
    direction = np.array([-1, 0])
    guard_walk(lab_grid, guard_pos, direction)
    print(f"Unique visited locations: {len(visited)}")

if __name__=="__main__":
    main()