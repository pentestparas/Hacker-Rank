n = input()
x = set(map(int, input().split()))
m = input()
y = set(map(int, input().split()))

print(*sorted(x.symmetric_difference(y)),sep='\n')



