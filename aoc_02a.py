fin = open("input_02.txt")

maxcol = {'red':12, 'green':13, 'blue':14}
gamesum = 0

for line in fin:
    gnumber = int(line.split(':')[0].split(' ')[1])
    draws = line.split(':')[1].split(';')
    valid = True
    for draw in draws:
        cubes = draw.split(',')
        for cube in cubes:
            for color in ['red', 'green', 'blue']:
                if color in cube:
                    if int(cube.split(' ')[1]) > maxcol[color]:
                        valid = False
    if valid:
        gamesum += gnumber

print(gamesum)
