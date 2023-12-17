# fin = open('input_05_sample.txt')
fin = open('input_05.txt')

numbers = [int(x) for x in fin.readline().strip().split(': ')[1].split()]
seeds = [(x,x+y-1) for x,y in zip(numbers[::2],numbers[1::2])]

fin.readline()

def transform(seeds, transformer):
    partial = []
    temp = []
    while seeds:
        cur_left, cur_right = seeds.pop(0)
        tr_left = transformer[1]
        tr_right = transformer[1]+transformer[2]-1
        diff = transformer[1]-transformer[0]
        overlap_left = max(tr_left, cur_left)
        overlap_right = min(tr_right, cur_right)
        if overlap_left <= overlap_right:
            partial.append((overlap_left-diff, overlap_right-diff))
            if cur_left < overlap_left:
                temp.append((cur_left, overlap_left-1))
            if cur_right > overlap_right:
                temp.append((overlap_right+1,cur_right))
        else:
            temp.append((cur_left, cur_right))
    seeds = temp.copy()
    return partial, seeds

new_seeds = []

for line in fin:
    if line.strip() == '':
        continue
    if line.strip().endswith('map:'):
        new_seeds.extend(seeds)
        seeds = new_seeds.copy()
        new_seeds = []
        continue
    transformer = [int(x) for x in line.strip().split()]
    partial, seeds = transform(seeds,transformer)
    new_seeds.extend(partial)

new_seeds.extend(seeds)
left_bounds = [x for (x,y) in new_seeds]
print(min(left_bounds), len(left_bounds))
