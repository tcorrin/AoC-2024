#!/usr/local/bin/python3.13

import copy

def process_file(filename, pt_two):
  grid = []
  current_pos = (0,0)
  current_dir = (0,-1)
  off_grid = False
  locations_visited = []
  loops = 0

  with open(filename, 'r') as file:
    for line in file:
      grid.append(list(line.strip()))

  for y, row in enumerate(grid):
    for x, icon in enumerate(row):
      if icon == "^":
        current_pos = (x,y)

  if not pt_two:
    while not off_grid:
      if current_pos not in locations_visited:
        locations_visited.append(current_pos)
      result = process_move(current_pos, current_dir, grid)
      current_pos = (result[0],result[1])
      current_dir = (result[2], result[3])
      off_grid = result[4]
  else:
    for y, row in enumerate(grid):
      for x, icon in enumerate(row):
        new_grid = copy.deepcopy(grid)
        new_grid[y][x] = "0"
        loops += run_patrol(current_pos, current_dir, new_grid)

  if not pt_two:
    print("Number of unique positions: " + str(len(locations_visited)))
  else:
    print("Number of loops: " + str(loops))

def run_patrol(current_pos, current_dir, grid):
  locations_visited = []
  off_grid = False
  while not off_grid:
    if (current_pos, current_dir) not in locations_visited:
      locations_visited.append((current_pos, current_dir))
    else:
      return 1

    result = process_move(current_pos, current_dir, grid)
    current_pos = (result[0],result[1])
    current_dir = (result[2], result[3])
    off_grid = result[4]
  return 0
  

def process_move(current_pos, direction, grid):
  max_x = len(grid[0])
  max_y = len(grid)
  if current_pos[0] + direction[0] >= max_x or \
     current_pos[0] + direction[0] < 0 or \
     current_pos[1] + direction[1] >= max_y or \
     current_pos[1] + direction[1] < 0:
    return (0, 0, 0, 0, True)
  next_x = current_pos[0]+direction[0]
  next_y = current_pos[1]+direction[1]
  next_step = grid[next_y][next_x]
  if next_step == '#' or next_step == '0':
    new_direction = rotate(direction[0], direction[1])
    return (current_pos[0], current_pos[1], new_direction[0], new_direction[1], False)
  else:
    return (next_x, next_y, direction[0], direction[1], False)
  
def rotate(x, y):
  if x == 0 and y == -1:
    return (1,0)
  if x == 1 and y == 0:
    return (0, 1)
  if x == 0 and y == 1:
    return (-1, 0)
  if x == -1 and y == 0:
    return(0,-1)

process_file("day06-example.txt", False)
process_file("day06-example.txt", True)
process_file("day06.txt", False)
process_file("day06.txt", True)
