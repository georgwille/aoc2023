from math import gcd

dirs, block2 = open('input_08.txt').read().split('\n\n')

ways = {}
startpos = []

for line in block2.strip().split('\n'):
    name = line[0:3]
    left = line[7:10]
    right = line[12:15]
    ways[name] = (left,right)
    if name.endswith('A'):
        startpos.append(name)

total = 1

for pos in startpos:
    steps = -1
    while True:
        steps += 1
        thisdir = dirs[steps%(len(dirs))]
        if thisdir == 'L':
            pos = ways[pos][0]
        else:
            pos = ways[pos][1]
        if pos.endswith('Z'):
            break

    total = (total*(steps+1))//gcd(total,steps+1)

print(total)
