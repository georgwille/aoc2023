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

d = 'n'

stepcounter = 0

while f[r][c] != 'S' or stepcounter == 0:
    stepcounter += 1
    r = r+drc[d][0]
    c = c+drc[d][1]
    d = dirs[f[r][c]][d]

print(stepcounter//2)
