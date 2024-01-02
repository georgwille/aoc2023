dirs, block2 = open('input_08.txt').read().split('\n\n')

ways = {}

for line in block2.strip().split('\n'):
    name = line[0:3]
    left = line[7:10]
    right = line[12:15]
    ways[name] = (left,right)

print(ways)

steps = -1
pos = 'AAA'

while True:
    steps += 1
    thisdir = dirs[steps%(len(dirs))]
    if thisdir == 'L':
        pos = ways[pos][0]
    else:
        pos = ways[pos][1]
    if pos == 'ZZZ':
        break

print(steps+1)
