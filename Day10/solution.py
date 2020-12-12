from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  
  data = [int(i) for i in data]

data.append(0)
data.sort()
data.append(max(data) + 3)

def part1(data):    
  data.sort()
  start = 0
  oneJolt = 0
  threeJolt = 0
  for num in data:    
    if num <= start + 3:           
      if num - start == 1:        
        oneJolt += 1
      elif num - start == 3:
        threeJolt += 1
      start = num  
  return oneJolt * threeJolt

def wayCount(data, base, visited):
  if base == len(data)-1:
    return 1

  if base in visited:
    return visited[base]

  output = 0    
  for i in range(base+1, len(data)):
    if data[i]-data[base] <= 3:
      output += wayCount(data, i, visited)

  visited[base] = output
  return output

def part2(data):          
  visited = {}
  return wayCount(data, 0, visited)

print(part1(data))
print(part2(data))