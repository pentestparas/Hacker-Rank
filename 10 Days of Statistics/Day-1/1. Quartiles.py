def m(s, v):
    if s % 2 == 0:
        m = (v[int(s/2)-1] + v[int(s/2)]) / 2
    else:
        m = v[int(s/2)]
    return int(m)

s = int(input())
n = sorted(list(map(int, input().split())))

if s % 2 == 0:
    dlow = n[0:int(s/2)]
    dhigh = n[int(s/2):s]
else:
    dlow = n[0:int(s/2)]
    dhigh = n[int(s/2)+1:s]

print (m(len(dlow), dlow))
print (m(s, n))
print (m(len(dhigh), dhigh))