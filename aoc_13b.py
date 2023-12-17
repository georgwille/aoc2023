# fin = open('input_13_sample.txt')
fin = open('input_13.txt')

fields = fin.read().split('\n\n')

total = 0

for field in fields:
    lines = field.strip().split('\n')
    # check vertical symmetry
    for cand in range(1,len(lines[0])):
        smudges = 0
        for line in lines:
            for diff in range(1,len(line)):
                p1 = cand-diff
                p2 = cand+diff-1
                if p1<0 or p2>=len(line):
                    break
                if line[p1] != line[p2]:
                    smudges += 1
        if smudges == 1:
            total += cand
            break
    # check horizontal symmetry
    for cand in range(1,len(lines)):
        smudges = 0
        for col_idx in range(len(lines[0])):
            for diff in range(1,len(lines)):
                p1 = cand-diff
                p2 = cand+diff-1
                if p1<0 or p2>=len(lines):
                    break
                if lines[p1][col_idx] != lines[p2][col_idx]:
                    smudges += 1
        if smudges == 1:
            total += cand*100
            break
print(total)
