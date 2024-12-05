#!/usr/local/bin/python3.13

def process_file(filename):
  letters = []
  word_count = 0
  cross_count = 0

  with open(filename, 'r') as file:
    for line in file:
      letters.append(list(line.strip()))

  for y, row in enumerate(letters):
    for x, letter in enumerate(row):
      word_count += check_for_word(x, y, "XMAS", letters)
      cross_count += check_for_cross(x, y, letters)
  
  print("Total number of words: " + str(word_count))
  print("Total number of x-mas: " + str(cross_count))

def check_for_word(x, y, word, data):
  max_y = len(data)
  max_x = len(data[0])
  word = list(word)
  word_len = len(word)
  directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
  word_match_count = 0
  for direction in directions:
    if y + direction[0] * (word_len - 1)  < max_y and y + direction[0] * (word_len - 1) > -1 and \
       x + direction[1] * (word_len - 1) < max_x and x + direction[1] * (word_len - 1) > -1:
      for i, letter in enumerate(word):
        if data[direction[0] * i + y][direction[1] * i + x] != letter:
          break
        elif i + 1 == word_len:
          word_match_count += 1
  return word_match_count

def check_for_cross(x, y, data):
  max_y = len(data)
  max_x = len(data[0])
  result = 0
  if y + 1  < max_y and y -1  > -1 and x + 1 < max_x and  x - 1 > -1:
    if data[y][x] == "A":
      if (data[y-1][x-1] == "M" and  data[y+1][x-1] == "M" and data[y+1][x+1] == "S" and data[y-1][x+1] == "S") or \
         (data[y+1][x-1] == "M" and  data[y+1][x+1] == "M" and data[y-1][x-1] == "S" and data[y-1][x+1] == "S") or \
         (data[y+1][x+1] == "M" and  data[y-1][x+1] == "M" and data[y-1][x-1] == "S" and data[y+1][x-1] == "S") or \
         (data[y-1][x+1] == "M" and  data[y-1][x-1] == "M" and data[y+1][x-1] == "S" and data[y+1][x+1] == "S"):
        result = 1

  return result

process_file('day04-example.txt')
process_file('day04.txt')
