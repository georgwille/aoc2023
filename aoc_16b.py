field = open('input_16.txt').read().strip().split('\n')

rmax = len(field)-1
cmax = len(field[0])-1

def energization(lights):
    # lights = [(0,-1,0,1)] # row, col, drow, dcol
    energized = set()
    used_beamsplitters = set()

    while lights:
        r,c,dr,dc = lights.pop(0)
        r += dr
        c += dc
        if not (0<=r<=rmax and 0<=c<=cmax):
            continue
        energized.add((r,c))
        f = field[r][c]
        if f == '.':
            lights.append((r,c,dr,dc))
        elif f == '-' and dc**2==1:
            lights.append((r,c,dr,dc))
        elif f == '-' and dr**2==1:
            if (r,c) in used_beamsplitters:
                continue
            else:
                lights.append((r,c,0, 1))
                lights.append((r,c,0,-1))
                used_beamsplitters.add((r,c))
        elif f == '|' and dr**2==1:
            lights.append((r,c,dr,dc))
        elif f == '|' and dc**2==1:
            if (r,c) in used_beamsplitters:
                continue
            else:
                lights.append((r,c, 1,0))
                lights.append((r,c,-1,0))
                used_beamsplitters.add((r,c))
        elif f == '/' and dc==1:
            lights.append((r,c,-1,0))
        elif f == '/' and dc==-1:
            lights.append((r,c,1,0))
        elif f == '/' and dr==1:
            lights.append((r,c,0,-1))
        elif f == '/' and dr==-1:
            lights.append((r,c,0,1))
        elif f == '\\' and dc==1:
            lights.append((r,c,1,0))
        elif f == '\\' and dc==-1:
            lights.append((r,c,-1,0))
        elif f == '\\' and dr==1:
            lights.append((r,c,0,1))
        elif f == '\\' and dr==-1:
            lights.append((r,c,0,-1))
        else:
            assert False
    return len(energized)

max_energy = 0

for dr in [-1,0,1]:
    for dc in [-1,0,1]:
        if dr*dr+dc*dc==1:
            for r in [-1,rmax+1]:
                for c in range(cmax):
                    e = energization([(r,c,dr,dc)])
                    max_energy = max(max_energy, e)
            for c in [-1,cmax+1]:
                for r in range(rmax):
                    e = energization([(r,c,dr,dc)])
                    max_energy = max(max_energy, e)

print(max_energy)
