line = open('input_15.txt').read().strip().split(',')

def hash(string):
    current = 0
    for c in string:
        current += ord(c)
        current *= 17
        current %= 256
    return current

box = {}

for i in range(256):
    box[i] = ([],[])

for entry in line:
    if '=' in entry:
        boxlabel, focallength = entry.split('=')
    else:
        boxlabel = entry[:-1]
        focallength = -1
    boxnumber = hash(boxlabel)
    if focallength == -1:
        if boxlabel in box[boxnumber][0]:
            index = box[boxnumber][0].index(boxlabel)
            box[boxnumber][0].pop(index)
            box[boxnumber][1].pop(index)
    else:
        if boxlabel in box[boxnumber][0]:
            index = box[boxnumber][0].index(boxlabel)
            box[boxnumber][1][index] = focallength
        else:
            box[boxnumber][0].append(boxlabel)
            box[boxnumber][1].append(focallength)

total = 0

for index,content in box.items():
    for ii,focallength in enumerate(content[1],1):
        total += (index+1)*ii*int(focallength)
    
print(total)
