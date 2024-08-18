import csv
import random
import math

#define random function
def randomizer(x,seed=None):
  # set seed if you want to shuffle variables in the same way order
  random.seed(seed)
  for i in reversed(range(1,len(x))):
    j = math.floor(random.random() * (i +1))
    x[i], x[j] = x[j], x[i]
  return(x)

with open('/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/condition_files/Words.csv', 'r') as file:
  csvreader = csv.reader(file)
  words = []
  for row in csvreader:
    words.append(row[0])
words = randomizer(words[1:len(words)])

print(words)
print(len(words))

with open('/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/condition_files/NonWord.csv', 'r') as file:
  csvreader = csv.reader(file)
  nonwords = []
  for row in csvreader:
    nonwords.append(row[0])

nonwords = randomizer(nonwords[1:len(nonwords)])


# with open('/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/condition_files/target_words.csv', 'r') as file:
#   csvreader = csv.reader(file)
#   targets = []
#   for row in csvreader:
#     targets.append(row[0])

# targets = randomizer(targets[1:len(targets)])
