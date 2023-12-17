import re

fin = open("input_03.txt")

field = []
stars = {}

for line in fin:
    field.append('.'+line.strip()+'.')

width = len(field[0])
field.insert(0,'.'*width)
field.append('.'*width)

def has_star(number, line_number, firstdigitpos, length):
    answer = False
    for offset in [-1,0,1]:
        for pos in range(firstdigitpos-1,firstdigitpos+length+1):
            if field[line_number+offset][pos] == '*':
                answer = True
                if (line_number+offset, pos) in stars:
                    stars[(line_number+offset, pos)].append(number)
                else:
                    stars[(line_number+offset, pos)] = [number]
    return answer

for line_no, line in enumerate(field[1:-1],1):
    cleanline = ''
    for char in line:
        if char.isdigit():
            cleanline += char
        else:
            cleanline += ' '
    numbers = cleanline.split(' ')
    numbers = [elem for elem in numbers if elem]
    positions = [m.start() for m in re.finditer('\d+', cleanline)]
    for number, position in zip(numbers, positions):
        if has_star(int(number), line_no, position, len(number)):
            pass
            # print(int(number), line_no, position, len(number))

total = 0

for star, numbers in stars.items():
    if len(numbers) >1:
        prod = 1
        for f in numbers:
            prod *= f
        total += prod

print(total)

# for lineno, line in enumerate(field):
#     print(line)
#     for charno, char in enumerate(line):
#         if (lineno,charno) in stars and len(stars[(lineno,charno)])==2:
#             print('X',end='')
#         else:
#             print(' ',end='')
#     print()

        