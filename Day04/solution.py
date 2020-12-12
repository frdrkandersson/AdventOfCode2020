from os.path import abspath, dirname, join
import re

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split("\n\n")
    data = [row.replace("\n", " ") for row in data]
    data = [row.split() for row in data]
    passports = [dict(pair.split(":") for pair in row) for row in data]

def fieldValidation(passport):
  fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}      
  return all(items in passport for items in fields)  

def baseValidation(passports):  
  return [p for p in passports if fieldValidation(p)]  

def isValidExtended(passport):  
  validations = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: int(x[:-2]) and (
        (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or
        (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)
    ),
    "hcl": lambda x: re.fullmatch("#[0-9a-f]{6}", x),
    "ecl": lambda x: re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", x),
    "pid": lambda x: int(x) and len(x) == 9,    
  }

  for field, func in validations.items():
    if field not in passport.keys():
      continue      
    try:
      if not func(passport[field]):
        return 0      
    except:
      return 0
  return 1  

def part1(passports):  
  return len(baseValidation(passports))

def part2(passports):  
  return sum(isValidExtended(p) for p in baseValidation(passports))

print(part1(passports))
print(part2(passports))