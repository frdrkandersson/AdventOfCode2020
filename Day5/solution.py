from os.path import abspath, dirname, join
import re
import math

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()

def getId(str, min, max, upper, lower):
  for c in str:
    if max-min == 1:
      if c == lower:
        return min
      else:
        return max
    if c == upper:
      min += math.ceil((max-min) / 2)
    else:      
      max -= math.ceil((max-min) / 2)

def getSeatIds(data):
  highest = 0
  seatIds = []
  for i in data:
    rowStr, colStr = i[:7], i[7:]   
    
    row = getId(rowStr, 0, 127, 'B', 'F')
    col = getId(colStr, 0, 7, 'R', 'L')        
    seatId = row * 8 + col
    seatIds.append(seatId)
    highest = max(highest, seatId)
  return seatIds, highest  

def part1(data):
  _, highest = getSeatIds(data)
  return highest
    
def part2(data):  
  ids, _ = getSeatIds(data)
  list.sort(ids)    
  last = -1
  for id in ids:
    if id - last == 2 and last != -1: 
      return id-1
    last = id      

print(part1(data))
print(part2(data))