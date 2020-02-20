def average(array):
    height = set(array)
    return sum(height) / len(height)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)