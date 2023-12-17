fin = open('input_05.txt')

seeds = [int(x) for x in fin.readline().strip().split(': ')[1].split()]
print(seeds)
used = [False]*len(seeds)

def transform(seeds, used, transformer):
    for ii, seed in enumerate(seeds):
        if used[ii]:
            continue
        if transformer[1] <= seed <= transformer[1]+transformer[2]:
            seeds[ii] = seed - transformer[1] + transformer[0]
            used[ii] = True


for line in fin:
    if line.strip() == '':
        used = [False]*len(seeds)
        continue
    if line.strip().endswith('map:'):
        continue
    transformer = [int(x) for x in line.strip().split()]
    transform(seeds,used,transformer)

print(seeds, min(seeds))
