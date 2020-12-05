from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()
    
data_ints = [int(i) for i in data]

def part1(ints):
  for i in ints:
    search_val = 2020 - i
    if search_val in ints:      
      return i * search_val

def part2(ints):    
  for i in range(len(ints)):
    for j in range(i, len(ints)):  
      search_val = 2020 - ints[i] - ints[j]
      if search_val in ints:
        return ints[i] * ints[j] * search_val

print(part1(data_ints))  
print(part2(data_ints))  
