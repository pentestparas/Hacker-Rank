import statistics
import numpy

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(numpy.mean(arr))
print(numpy.median(arr))

def mode(arr):
    list_table = statistics._counts(arr)
    len_table = len(list_table)

    if len_table == 1:
        mmode = statistics.mode(arr)
    else:
        new_list = []
        for i in range(len_table):
            new_list.append(list_table[i][0])
        mmode = min(new_list) 
    return mmode

if __name__ == '__main__':
    print(mode(arr))