fin = open("input_01.txt")

total = 0

for line in fin:
    for char in line:
        if char.isdigit():
            a = int(char)
            break
    for char in line[::-1]:
        if char.isdigit():
            b = int(char)
            break
    number = a*10+b
    total += number

print(total)