# fin = open('input_10_sample.txt')
fin = open('input_10.txt')

f = []

dirs = {'-':{'n': None, 's': None, 'w': 'w', 'e': 'e'},
        '|':{'n': 'n', 's': 's', 'w': None, 'e': None},
        'F':{'n': 'e', 's': None, 'w': 's', 'e': None},
        'L':{'n': None, 's': 'e', 'w': 'n', 'e': None},
        '7':{'n': 'w', 's': None, 'w': None, 'e': 's'},
        'J':{'n': None, 's': 'w', 'w': None, 'e': 'n'},
        'S':{'n': None, 's': 'w', 'w': None, 'e': 'n'},
        }

drc = {'n':(-1,0),
       's':( 1,0),
       'w':(0,-1),
       'e':(0, 1),
       }

for ii,line in enumerate(fin):
    clean = line.strip()
    f.append(clean)
    if 'S' in clean:
        c = clean.index('S')
        r = ii

for startdir, steps in drc.items():
    try:
        if dirs[f[r+steps[0]][c+steps[1]]][startdir]:
            d = startdir
    except:
        continue

loop = set()
stepcounter = 0

while f[r][c] != 'S' or not loop:
    r = r+drc[d][0]
    c = c+drc[d][1]
    d = dirs[f[r][c]][d]
    loop.add((r,c))

print(len(loop)//2)

border_above_count = [0]*len(f[0])
internal = 0

for r in range(1,len(f)):
    for c in range(len(f[0])):
        # how many horizontal loop lines (at the right edge of the tile)
        # must be crossed to get here from above? Is it an odd number?
        # Then we have found an enclosed tile.
        if f[r-1][c] in 'LF-' and (r-1,c) in loop:
            border_above_count[c] += 1
        if (r,c) not in loop and border_above_count[c] % 2:
            internal += 1

print(internal)
