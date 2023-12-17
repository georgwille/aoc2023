fin = open("input_06.txt")

line = fin.readline()
times = [int(x) for x in line.split()[1:] if x]

line = fin.readline()
dists = [int(x) for x in line.split()[1:] if x]

chances = []
prod = 1

for time,dist in zip(times, dists):
    det = (time**2/4-dist)**0.5
    t1 = time/2+det
    t2 = time/2-det
    print(det, t1, t2)
    t1 = int(t1-0.0000001)
    t2 = int(t2+1)
    print(det, t1, t2)
    chances.append(t1-t2+1)
    prod *= t1-t2+1


print(chances, prod)
print(prod/(t1-t2+1))
