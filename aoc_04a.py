fin = open("input_04.txt")

total = 0

for line in fin:
    numbers = line.strip().split(': ')[1]
    winning, my = numbers.split(' | ')
    winning = [x for x in winning.split(' ') if x]
    my = [x for x in my.split(' ') if x]
    print(winning, my)
    common = set(winning).intersection(set(my))
    print(common)
    if len(common) > 0:
        total += 2**(len(common)-1)

print(total)
