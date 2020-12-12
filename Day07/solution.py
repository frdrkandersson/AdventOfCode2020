from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  

def parseData(data, withnumber):
  output = dict()
  for row in data:
    childs = []
    words = row.split()          
    for i, word in enumerate(words):
      if word.isdigit():
        childs.append(" ".join(words[i:i+3])) if withnumber else childs.append(" ".join(words[i+1:i+3]))                  
    parent = " ".join(words[:2])
    output[parent] = childs    
  return output

def part1(data, searchValue):      
  output = set()  
  for key, value in data.items():    
    if searchValue in value:           
      output.add(key)      
      output = output.union(part1(data, key))
  return output

def part2(data, root):        
  output = 0
  for child in data[root]:    
    contains = int(child[:1]) 
    output += contains
    output += (contains * part2(data, child[2:]))
  return output

print(len(part1(parseData(data, False), "shiny gold")))
print(part2(parseData(data, True), "shiny gold"))