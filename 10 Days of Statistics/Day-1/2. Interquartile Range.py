s = int(input())
n = list(map(int, input().split()))
f = list(map(int, input().split()))

ndata = []
for i in range(len(n)):
    for j in range(f[i]):
        ndata.append(n[i])
ndata = sorted(ndata)

s = int(len(ndata))
if s % 2 == 0:
    dlow = ndata[0:int(s/2)]
    dhigh = ndata[int(s/2):s]
else:
    dlow = ndata[0:int(s/2)]
    dhigh = ndata[int(s/2)+1:s]


def median(s, v):
    if s % 2 == 0:
        median = (v[int(s/2)-1] + v[int(s/2)]) / 2
    else:
        median = float(v[int(s/2)])
    return median


l = median(len(dlow), dlow)
h = median(len(dhigh), dhigh)
print(h - l)