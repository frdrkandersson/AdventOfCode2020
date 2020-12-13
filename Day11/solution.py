from os.path import abspath, dirname, join 
from copy import deepcopy
import numpy as np

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  
  data = [list(row) for row in data]

data = np.array(data) # just for better printing

def applyRules(data, x, y):  
  value = data[x][y]
  if value == ".":
    return value

  directions = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
  counter = 0
  for direction in directions:
    dx, dy = direction
    if x+dx < 0 or y+dy < 0:
      continue
    try:      
      if data[x+dx][y+dy] == "#":
        if value == "L":
          return "L"
        elif value == "#":
          counter += 1
          if counter == 4:
            return "L"        
    except:
      continue
  return "#"

def applyRules2(data, x, y):    
  value = data[x][y]
  if value == ".": 
    return value

  directions = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))  
  dir = ("left-down", "down", "right-down", "right", "up-left", "up", "up-left", "left")
  counter = 0  

  for i, direction in enumerate(directions):    
    dx, dy  = direction    
    while True:                  
      try:                
        seat = data[x+dx][y+dy]
      except:
        break            

      if x+dx < 0 or y+dy < 0 or seat == "L":
        break                

      if seat == ".":
        dx += direction[0]
        dy += direction[1]
        continue

      if seat == "#":
        if value == "L":
          return "L"
        elif value == "#":          
          counter += 1                    
          if counter == 5:            
            return "L"
      break
  return "#"    

def part1(data):        
  while True:                 
    tempData = deepcopy(data)
    output = 0
    changeCounter = 0    
    for x in range(len(data)):
      for y in range(len(data[x])):        
        value = applyRules(data, x, y)
        if value == "#":
          output += 1
        if data[x][y] != value:
          changeCounter += 1
          tempData[x][y] = value        
    data = tempData    
    if changeCounter == 0:
      break  
  return output

def part2(data):          
  while True:                 
    tempData = deepcopy(data)
    output = 0
    changeCounter = 0            
    for x in range(len(data)):
      for y in range(len(data[x])):        
        value = applyRules2(data, x, y)
        if value == "#":
          output += 1
        if data[x][y] != value:
          changeCounter += 1          
          tempData[x][y] = value                              
    data = tempData                        
    if changeCounter == 0:
      break  
  return output

print(part1(data))
print(part2(data))