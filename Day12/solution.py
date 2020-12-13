from os.path import abspath, dirname, join 

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  

def part1(data):
  directions = [[1,0], [0,-1], [-1,0], [0,1]] # E, S, W, N
  direction = 0
  grid = [0, 0]    
  for ins in data:    
    action, value = ins[:1], int(ins[1:])
    if action == "N":
      grid[1] += value
    elif action == "S":
      grid[1] -= value
    elif action == "E":
      grid[0] += value
    elif action == "W":
      grid[0] -= value
    elif action == "L":
      direction = (direction - value // 90) % 4
    elif action == "R":
      direction = (direction + value // 90) % 4
    elif action == "F":      
      grid[0] += directions[direction][0] * value
      grid[1] += directions[direction][1] * value       
  return abs(grid[0]) + abs(grid[1])

def part2(data):          
  grid = [0, 0]    
  waypoint = [10, 1]
  for ins in data:    
    action, value = ins[:1], int(ins[1:])
    if action == "N":
      waypoint[1] += value
    elif action == "S":
      waypoint[1] -= value
    elif action == "E":
      waypoint[0] += value
    elif action == "W":
      waypoint[0] -= value                    
    elif action == "L":
      for _ in range(value // 90):
        waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]            
    elif action == "R":            
      for _ in range(value // 90):
        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]  
    elif action == "F":      
      grid[0] += waypoint[0] * value
      grid[1] += waypoint[1] * value             
  return abs(grid[0]) + abs(grid[1])

print(part1(data))
print(part2(data))