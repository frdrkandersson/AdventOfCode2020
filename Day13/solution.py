from os.path import abspath, dirname, join 
from functools import reduce

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  

# region https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
# endregion

def part1(data):
  time = int(data[0])
  busses = list(filter(lambda x: x != "x", data[1].split(",")))      
  while True:
    for bus in busses:
      if time % int(bus) == 0:                
        return int(bus) * (time - int(data[0]))
    time += 1  

def part2(data):  
  busses = list(data[1].split(",")) 
  n, a = [], []   
  for i, bus in enumerate(busses):    
    if bus == "x":
      continue
    else:
      n.append(int(bus))      
      a.append(int(bus)-i)
  
  return (chinese_remainder(n, a))
    
print(part1(data))
print(part2(data))