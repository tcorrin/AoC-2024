#!/usr/local/bin/python3.13

import re

def process_file(filename, process_conditionals):
  total = 0
  do = True

  with open(filename, 'r') as file:
    for line in file:
      if process_conditionals:
        matches = re.findall(r'mul\((\d+,\d+)\)|(do\(\))|(don\'t\(\))',line.strip())
      else:
        matches = re.findall(r'mul\((\d+,\d+)\)',line.strip())
      for match in matches:
        if not process_conditionals:
          numbers = match.split(",")
          total += int(numbers[0]) * int(numbers[1])
        else:
          if match[2] != '':
            do = False
          elif match[1] != '':
            do = True 
          else:
            numbers = match[0].split(",")
            if do:
              total += int(numbers[0]) * int(numbers[1])

  print("Processing " + filename + " - process_conditionals: " + str(process_conditionals) + " - Uncorrupted mul instructions total: " + str(total))      

process_file("day03-example.txt", False)
process_file("day03-example2.txt", True)
process_file("day03.txt", False)
process_file("day03.txt", True)
