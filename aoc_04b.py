fin = open("input_04.txt")

total = 0
count = [1]*1000

for lineno,line in enumerate(fin,1):
    numbers = line.strip().split(': ')[1]
    winning, my = numbers.split(' | ')
    winning = [x for x in winning.split(' ') if x]
    my = [x for x in my.split(' ') if x]
    common = set(winning).intersection(set(my))
    for ii in range(lineno+1, lineno+1+len(common)):
        count[ii] += count[lineno]

print(sum(count[1:lineno+1]))
