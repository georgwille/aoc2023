fin = open("input_02.txt")

maxcol = {'red':12, 'green':13, 'blue':14}
gamesum = 0
allsum = 0

for line in fin:
    mincol = {'red':0, 'green':0, 'blue':0}
    gnumber = int(line.split(':')[0].split(' ')[1])
    draws = line.split(':')[1].split(';')
    valid = True
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            for color in ['red', 'green', 'blue']:
                if color in cube:
                    mincol[color] = max(mincol[color],int(cube.split(' ')[1]))
                    if int(cube.split(' ')[1]) > maxcol[color]:
                        valid = False
    if valid:
        gamesum += gnumber
    allsum += mincol['red']*mincol['green']*mincol['blue']
print(gamesum)
print(allsum)