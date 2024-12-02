#!/usr/local/bin/python3.13

def process_file(filename, dampener_enabled):
  
  safe_total = 0

  with open(filename, 'r') as file:
    for line in file:
      input_data = line.strip().split(" ")
      if is_safe_data(input_data):
        safe_total += 1
      elif dampener_enabled:
        for i, c in enumerate(input_data):
          dampener_data = input_data[:i] + input_data[i+1:]
          if is_safe_data(dampener_data):
            safe_total += 1
            break

    print("Processing " + filename + " - Dampener Enabled: " + str(dampener_enabled) + " - Safe Total: " + str(safe_total))

def is_safe_data(input_data):
  is_safe = True
  
  descending = False
  ascending = False
  
  for i, item in enumerate(input_data):
    if i > 0:
      item = int(item)
      previous_item = int(input_data[i-1])

      if abs(previous_item - item) > 3:
        is_safe = False
        break
      elif previous_item == item:
        is_safe = False
        break
      elif previous_item > item:
        if ascending:
          is_safe = False
          break
        else:
          descending = True
      elif previous_item < item:
        if descending:
          is_safe = False
          break
        else:
          ascending = True

  return is_safe

process_file('day02-example.txt', False)
process_file('day02-example.txt', True)
process_file('day02.txt', False)
process_file('day02.txt', True)
