from collections import Counter

cv = {'2':2,
      '3':3,
      '4':4,
      '5':5,
      '6':6,
      '7':7,
      '8':8,
      '9':9,
      'T':10,
      'J':11,
      'Q':12,
      'K':13,
      'A':14,
     }

# lines = open('input_07_sample.txt').read().strip().split('\n')
lines = open('input_07.txt').read().strip().split('\n')

print(lines)

def worth(line):
    hand, bid = line.split()
    value = 0
    hand_type = list(Counter(hand).values())
    hand_type.sort() 
    if hand_type == [5]:
        value += 1000000000000
    elif hand_type == [1,4]:
        value += 900000000000
    elif hand_type == [2,3]:
        value += 800000000000
    elif hand_type == [1,1,3]:
        value += 700000000000
    elif hand_type == [1,2,2]:
        value += 600000000000
    elif hand_type == [1,1,1,2]:
        value += 500000000000
    elif hand_type == [1,1,1,1,1]:
        value += 400000000000
    else:
        assert False
    for ii,c in enumerate(hand):
        value += 14**(4-ii)*cv[c]
    return value

for line in lines:
    print(worth(line))

lines.sort(key=worth)

total = 0

for ii,line in enumerate(lines,1):
    total += int(line.split()[1])*ii

print(total)
