from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

def parseData(data):
  output = list()
  for row in data:
    input = row.split()   
    range = input[0].split('-')    
    char = input[1].replace(':', '')    
    output.append((int(range[0]), int(range[1]), char, input[2]))
  return output

def part1(data):
  ans = 0
  for i in data:
    min, max, char, pw = i
    count = pw.count(char)
    if min <= count <= max:
      ans += 1
  return ans

def part2(data):
  ans = 0
  for i in data:
    pos1, pos2, char, pw = i
    if (char == pw[pos1-1]) ^ (char == pw[pos2-1]):
      ans += 1
  return ans

input = parseData(data)
print(part1(input))
print(part2(input))