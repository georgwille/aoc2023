fin = open('input_11.txt')

age = 10**6

f = []
for line in fin:
    clean = line.strip()
    if '#' not in clean:
        f.append(len(clean)*'*')
    else:
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
            f[ii]=r[:c]+'*'+r[c+1:]
    c += 1

# for line in f:
#     print(line)

gals = set()

for r,line in enumerate(f):
    for c,char in enumerate(line):
        if char=='#':
            gals.add((r,c))

total = 0

for r1,c1 in gals:
    for r2,c2 in gals:
        for r in range(min(r1,r2),max(r1,r2)):
            total += (1 if f[r][c1]!='*' else age)
        for c in range(min(c1,c2),max(c1,c2)):
            total += (1 if f[r1][c]!='*' else age)

print(total//2)

