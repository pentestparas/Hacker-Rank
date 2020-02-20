import math

s = int(input())
n = list(map(int, input().split()))

def mean(data):
    return sum(data) / len(data)

def stddev(data, s):
    sum = 0
    for i in range(s):
        sum = sum + (data[i] - mean(data)) ** 2
    return math.sqrt(sum / s)

print(round(stddev(n, s), 1))

