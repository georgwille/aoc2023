# somewhat similar to AoC 2022/24!
import heapq

field = open('input_17.txt').read().strip().split('\n')

rmax = len(field)
cmax = len(field[0])

job = []
# first two start options
heapq.heappush(job, (0,0,0,0,1,0))
heapq.heappush(job, (0,0,0,1,0,0))
# heatloss, row, column, r_direction, c_direction, 
# number of steps in this direction
# when comparing tuples (as heapq does), it is done
# element by element in order, therefore heatloss first
finalized = set()

while job:
    hl, r, c, dr, dc, steps = heapq.heappop(job)
    if r == rmax-1 and c == cmax-1 and steps > 3:
        print(hl)
        break
    if (r,c,dr,dc,steps) in finalized:
        continue
    finalized.add((r,c,dr,dc,steps))

    if steps < 10: # continue straight
        nr = r+dr
        nc = c+dc
        if 0<=nr<rmax and 0<=nc<cmax:
            heapq.heappush(job,(hl+int(field[nr][nc]),nr,nc,dr,dc,steps+1))
    if steps > 3:
        for (ndr, ndc) in [(dc,dr),(-dc,-dr)]: # two orthogonal directions
            nr = r+ndr
            nc = c+ndc
            if 0<=nr<rmax and 0<=nc<cmax:
                heapq.heappush(job,(hl+int(field[nr][nc]),nr,nc,ndr,ndc,1))

print(len(finalized))