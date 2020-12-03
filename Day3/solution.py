from os.path import abspath, dirname, join

filename = abspath(join(dirname(__file__), 'input.txt'))
data = open(filename, 'r').read().splitlines()
max_x = len(data[0])
max_y = len(data)

def part1(dx, dy):
  counter = 0
  x = 0
  for y in range(dy, max_y, dy):
    x += dx
    if x >= max_x:      
      x -= max_x    

    if data[y][x] == '#':
      counter += 1    

  return counter

def part2():
  return part1(1, 1) * part1(3, 1) * part1(5, 1) * part1(7, 1) * part1(1, 2)  

print(part1(3, 1))
print(part2())