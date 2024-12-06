#!/usr/local/bin/python3.13

def process_file(filename):
  rules = []
  page_seqs = []
  correct_results = 0
  fixed_results = 0

  with open(filename, 'r') as file:
    rules_finished = False
    for line in file:
      line = line.strip()
      if line == "":
        rules_finished = True
      elif rules_finished:
        page_seqs.append(line.split(","))
      else:
        split = line.split("|")
        rules.append((split[0],split[1]))

  for seq in page_seqs:
#  for seq in page_seqs[3:4]:
    if check_seq(seq, rules):
      correct_results += int(seq[len(seq) // 2])
    else:
      fixed_results += int(fix_seq(seq, rules)[len(seq) // 2])

  print("Sum of correct middle page numbers: " + str(correct_results))
  print("Sum of fixed middle page numbers: " + str(fixed_results))

def check_seq(seq, rules):
  result = True
  for i, number in enumerate(seq):
    for rule in rules:
      if rule[0] == number and rule[1] in seq[:i]:
        result = False
  return result

def fix_seq(seq, rules):
  for i, number in enumerate(seq):
    for rule in rules:
      if rule[0] == number and rule[1] in seq[:i]:
        p = seq.index(rule[1])
        new_seq = seq[:p] + [rule[0]] + [rule[1]] + seq[p+2:]
#        print(seq)
#        print(number)
#        print(seq[:p])
#        print([rule[0]])
#        print(seq[p+1:])
#        print(new_seq)
        return fix_seq(new_seq, rules)
  return seq


process_file("day05-example.txt")
process_file("day05.txt")
