from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().splitlines()  

def boot(data):
  ran = set()
  acc = 0
  i = 0      
  while i < len(data):                
    if i in ran:
      break

    ins, arg = data[i].split()                
    ran.add(i)

    if ins == "jmp":
      i += int(arg) 
      continue

    elif ins == "acc":
      acc += int(arg)                  

    i += 1      
  return acc, i


def part1(data):  
  ans, _ = boot(data)
  return ans

def part2(data):  
  i = 0            
  while i < len(data):
    ins = data[i].split()[0]     
    if ins == "nop":
      data[i] = data[i].replace("nop", "jmp")
      acc, resultindex = boot(data)
      data[i] = data[i].replace("jmp", "nop")
      
    elif ins == "jmp":
      data[i] = data[i].replace("jmp", "nop")         
      acc, resultindex = boot(data)
      data[i] = data[i].replace("nop", "jmp")

    if resultindex == len(data):
      return acc
    i += 1        

print(part1(data))
print(part2(data))