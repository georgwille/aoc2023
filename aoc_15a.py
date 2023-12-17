line = open('input_15.txt').read().strip().split(',')

def hash(string):
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current %= 256
    return current


total = 0

for entry in line:
    h = hash(entry)
    total += h

print(total)
