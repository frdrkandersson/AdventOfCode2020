from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  
  data = [int(i) for i in data]

def sumExist(data, i, preamble):  
  preamble = set(data[i-preamble:i])  
  val = data[i]
  for num in preamble:
    if val-num in preamble:      
      return True
  return False

def part1(data, preamble = 25):  
  for i in range(preamble, len(data)):    
    if not sumExist(data, i, preamble):
      return data[i]

def part2(data, searchValue):  
  for i in range(len(data)):
    val = data[i]    
    next = i+1
    while val < searchValue and next < len(data):
      val += data[next]
      next += 1
    if val == searchValue:
      numrange = data[i:next-1]
      return min(numrange) + max(numrange)

searchValue = part1(data)
print(searchValue)
print(part2(data, searchValue))