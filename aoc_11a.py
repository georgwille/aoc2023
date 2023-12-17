fin = open('input_11.txt')

f = []
for line in fin:
    clean = line.strip()
    f.append(clean)
    if '#' not in clean:
        f.append(clean)

def is_col_empty(c):
    for r in f:
        if r[c] == '#':
            return False
    return True

c = 0
while c < len(f[0]):
    if is_col_empty(c):
        for ii,r in enumerate(f):
            f[ii]=r[:c]+'.'+r[c:]
        c += 1
    c += 1

gals = set()

for r,line in enumerate(f):
    for c,char in enumerate(line):
        if char=='#':
            gals.add((r,c))

total = 0

for r1,c1 in gals:
    for r2,c2 in gals:
        total += abs(r1-r2)+abs(c1-c2)

print(total//2)

