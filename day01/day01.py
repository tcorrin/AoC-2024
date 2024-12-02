#!/usr/local/bin/python3.13

import re

def process_file(filename):
  locations_a = []
  locations_b = []
  how_far_apart = []
  similarity_score = []

  with open(filename, 'r') as file:
    for line in file:
      matches = re.search(r'^(\d+)   (\d+)$',line.strip())
      locations_a.append(int(matches.group(1)))
      locations_b.append(int(matches.group(2)))
  
  list.sort(locations_a)
  list.sort(locations_b)

  for i, location_a in enumerate(locations_a):
    how_far_apart.append(abs(location_a - locations_b[i]))
    similarity_score.append(locations_b.count(location_a)*location_a)

  print(filename + " - Total distance between lists: " + str(sum(how_far_apart)))
  print(filename + " - Total similarity score: " + str(sum(similarity_score)))

process_file('day01-example.txt')
process_file('day01.txt')
