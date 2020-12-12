from os.path import abspath, dirname, join
import math

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().split("\n\n")
  data = [row.replace("\n", " ") for row in data]

def part1(data):    
  return sum([len(''.join(set(grp.replace(" ", "")))) for grp in data])   

def part2(data):    
  output = 0
  for grp in data:      
    dups = ""    
    for p in grp.split(" "):
      if dups != "":                
        s1 = set(p)
        s2 = set(dups)
        dups = ''.join(s1&s2)
        if len(dups) == 0:
          break        
      else:        
        dups = p  
    output += len(dups)            
  
  return output

print(part1(data))
print(part2(data))