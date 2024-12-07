#!/usr/local/bin/python3.13

def process_file(filename):
  equations = []
  total_calibration_result = 0

  with open(filename, 'r') as file:
    for line in file:
      numbers = []
      split = line.strip().split(": ")
      number_strings = split[1].split(" ")
      for number_string in number_strings:
        numbers.append(int(number_string))
      equations.append(((int(split[0])),numbers))
  print(equations)

  for equation in equations:
    if process_equation(equation):
      total_calibration_result += equation[0]

  print("Total calibration result: " + str(total_calibration_result))

def process_equation(equation):
  result = False

  return result

process_file("day07-example.txt")
#process_file("day07.txt")
