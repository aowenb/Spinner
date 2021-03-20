import numpy as np

list_awal = [[1,2,3],[4,5,6],[7,8,9]]

def counterClockwise(x): # pakai fucntion numpy untuk rotate list 90 derajat
    return np.rot90(x)

print(counterClockwise(list_awal))