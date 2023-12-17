# fin = open("input_09_sample.txt")
fin = open("input_09.txt")

total = 0

for line in fin:
    numbers = []
    diff_level = 0
    numbers.append([int(x) for x in line.split()])
    while any(numbers[diff_level]):
        diff_level += 1
        numbers.append([])
        for ii in range(len(numbers[diff_level-1])-1):
            numbers[diff_level].append(numbers[diff_level-1][ii+1]-numbers[diff_level-1][ii])
    print(numbers)
    extrapolation = numbers[diff_level][0]
    while diff_level>0:
        diff_level -= 1
        extrapolation = numbers[diff_level][0] - extrapolation
    print(extrapolation)
    total += extrapolation

print(total)
