import re

fin = open("input_03.txt")

field = []

for line in fin:
    field.append('.'+line.strip()+'.')

width = len(field[0])
field.insert(0,'.'*width)
field.append('.'*width)

def adjacent_symbol(line_number, firstdigitpos, length):
    for offset in [-1,1]:
        if field[line_number+offset][firstdigitpos-1:firstdigitpos+length+1].count('.') != length+2:
            return True
    if field[line_number][firstdigitpos-1] != '.' or field[line_number][firstdigitpos+length] != '.':
        return True
    return False

partsum = 0

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
        if adjacent_symbol(line_no, position, len(number)):
            partsum += int(number)

print(partsum)
