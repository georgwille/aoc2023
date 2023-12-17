fin = open("input_01.txt")

total = 0

replace = {"one":1,
           "two":2,
           "three":3,
           "four":4,
           "five":5,
           "six":6,
           "seven":7,
           "eight":8,
           "nine":9,
           "1":1,
           "2":2,
           "3":3,
           "4":4,
           "5":5,
           "6":6,
           "7":7,
           "8":8,
           "9":9}
           
def leftdigit(string):
    newvalue = -1
    indexmin = 999
    for x,y in replace.items():
        index = string.find(x)
        if 0 <= index <= indexmin:
            indexmin = index
            newvalue = y
    return newvalue

for line in fin:
    leftmost = leftdigit(line)*10
    for i in range(1,len(line)+1):
        rightmost = leftdigit(line[-i:])
        if rightmost > -1:
            break
    print(line, leftmost, rightmost)
    number = leftmost + rightmost
    total += number

print(total)
