# fin = open('input_13_sample.txt')
fin = open('input_13.txt')

fields = fin.read().split('\n\n')

total = 0

for field in fields:
    lines = field.strip().split('\n')
    # check vertical symmetry
    for cand in range(1,len(lines[0])):
        has_vertical = True
        for line in lines:
            for diff in range(1,len(line)):
                p1 = cand-diff
                p2 = cand+diff-1
                if p1<0 or p2>=len(line):
                    break
                if line[p1] != line[p2]:
                    has_vertical = False
        if has_vertical:
            total += cand
            break
    # check horizontal symmetry
    for cand in range(1,len(lines)):
        has_horizontal = True
        for col_idx in range(len(lines[0])):
            for diff in range(1,len(lines)):
                p1 = cand-diff
                p2 = cand+diff-1
                if p1<0 or p2>=len(lines):
                    break
                if lines[p1][col_idx] != lines[p2][col_idx]:
                    has_horizontal = False
        if has_horizontal:
            total += cand*100
            break
print(total)