lines = open('input_18.txt').read().strip().split('\n')

start = (0,0)
lagoon = [start]

dirs = {'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(0,-1)}

for line in lines:
    d, length, color = line.split()
    for steps in range(int(length)):
        lastr, lastc = lagoon[-1]
        dr, dc = dirs[d]
        lagoon.append((lastr+dr, lastc+dc))

rmin = 999
rmax = -999
cmin = 999
cmax = -999

for r,c in lagoon:
    rmin = min(rmin, r)
    rmax = max(rmax, r)
    cmin = min(cmin, c)
    cmax = max(cmax, c)

print(rmin,rmax,cmin,cmax)

brmin = rmin-2
brmax = rmax+2
bcmin = cmin-2
bcmax = cmax+2

front = [(rmin-1,cmin-1)]
flood = set()
flood.add(front[0])
while front:
    r,c = front.pop(0)
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if brmin<=nr<=brmax and bcmin<=nc<=bcmax and (nr,nc) not in flood and (nr,nc) not in lagoon:
            front.append((nr,nc))
            flood.add((nr,nc))

print((brmax-brmin+1)*(bcmax-bcmin+1)-len(flood))

# for r in range(brmin,brmax+1):
#     for c in range(bcmin,bcmax+1):
#         if (r,c) in flood:
#             print('o',end='')
#         elif (r,c) in lagoon:
#             print('#',end='')
#         else:
#             print('.',end='')
#     print()
