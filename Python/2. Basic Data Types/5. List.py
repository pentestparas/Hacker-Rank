array = []
for _ in range(int(input())):
    n = input().strip().split(" ")
    x = n[0]
    if (x == "insert"):
        array.insert(int(n[1]), int(n[2]))
    elif (x == "print"):
        print(array)
    elif (x == "sort"):
        array.sort()
    elif (x == "reverse"):
        array.reverse()
    elif (x == "pop"):
        array.pop()
    elif (x == "remove"):
        array.remove(int(n[1]))
    elif (x == "append"):
        array.append(int(n[1]))