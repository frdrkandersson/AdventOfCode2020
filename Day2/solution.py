import numpy as np
import math
from os.path import abspath, dirname, join

filename = abspath(join(dirname(__file__), 'input.txt'))
data = open(filename, 'r').read().splitlines()

def parseData(data):
  output = list()
  for row in data:
    input = row.split()   
    range = input[0].split('-')    
    char = input[1].replace(':', '')    
    output.append((int(range[0]), int(range[1]), char, input[2]))
  return output

def isPasswordValid2(pw):  
  input = pw.split()   
  range = input[0].split('-')
  pos1 = int(range[0])
  pos2 = int(range[1])
  char = input[1].replace(':', '')
  pw = input[2]    

  bool1 = char == pw[pos1-1]
  bool2 = char == pw[pos2-1]

  if bool1 != bool2:
    return 1

  # if count in range(min, max):
  #   return 1
  return 0

def part1(data):  
  ans = 0
  for i in data:    
    ans += isPasswordValid2(i)    
  return ans  

def p1(data):
  ans = 0
  for i in data:
    min, max, char, pw = i
    count = pw.count(char)
    if min <= count <= max:
      ans += 1
  return ans

def p2(data):
  ans = 0
  for i in data:
    pos1, pos2, char, pw = i
    if (char == pw[pos1-1]) ^ (char == pw[pos2-1]):
      ans += 1
  return ans

input = parseData(data)
print(p1(input))
print(p2(input))