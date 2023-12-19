lines = open('input_18.txt').read().strip().split('\n')

r,c = 0,0
area = 0

for line in lines:
    foo, bar, code = line.split()
    length = int(code[2:-2],base=16)
    d = {'0':'R', '1':'D', '2':'L', '3':'U'}[code[-2]]
    if d == 'R':
        area -= 2*r*length
        c += length
    elif d == 'D':
        area += 2*c*length
        r += length
    elif d == 'L':
        area += 2*r*length
        c -= length
    elif d == 'U':
        area -= 2*c*length
        r -= length
    area += 2*length

print(area//4+1)
