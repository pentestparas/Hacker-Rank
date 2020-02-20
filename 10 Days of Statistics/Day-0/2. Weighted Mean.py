n = int(input().strip())
x = list(map(int, input().split()))
w = list(map(int,input().split()))

wmean = 0
for i in range(n):
    wmean = wmean + (x[i] * w[i])
print(round(wmean/sum(w), 1))