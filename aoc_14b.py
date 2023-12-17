fin = open('input_14.txt')

g = {}

for r,row in enumerate(fin):
    for c,char in enumerate(row):
        if char == '.':
            continue
        else:
            g[(r,c)] = char

rmax = r+1
cmax = c

dirs = [(-1,0),(0,-1),(1,0),(0,1)]

repetition_detected = False
hashes = [0]
loads = [0]
cyclecount = 0

while not repetition_detected:
    cyclecount += 1
    for rd,cd in dirs:
        haschanged = True
        while haschanged:
            haschanged = False
            for r in range(rmax):
                for c in range(cmax):
                    if (r,c) in g and g[(r,c)] == 'O':
                        rn = r+rd
                        cn = c+cd
                        if 0 <= rn < rmax and 0 <= cn < cmax and (rn,cn) not in g:
                            g.pop((r,c))
                            g[(rn,cn)] = 'O'
                            haschanged = True
    load = 0
    for (r,c),char in g.items():
        if char == 'O':
            load += (rmax-r)

    hash = 0
    for (r,c),char in g.items():
        if char == 'O':
            hash += (r+1)*7919+(c+1)*15485863
    print(cyclecount, hash, load)
    if hash in hashes:
        repetition_detected = True
        found = hashes.index(hash)
        print(found)
        print(loads[(10**9-found)%(cyclecount-found)+found])
    else:
        hashes.append(hash)
        loads.append(load)
