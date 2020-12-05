from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

max_x = len(data[0])

def getHits(dx, dy):
  counter = 0
  x = 0
  for y in range(dy, len(data), dy):
    x += dx
    if x >= max_x:      
      x -= max_x    

    if data[y][x] == '#':
      counter += 1    

  return counter

print(getHits(3, 1))
print(getHits(1, 1) * getHits(3, 1) * getHits(5, 1) * getHits(7, 1) * getHits(1, 2))