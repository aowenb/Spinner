clock = [[1,2,3],[4,5,6],[7,8,9]]

def counterClockwise(x):
    temp = [[0,0,0],[0,0,0],[0,0,0]]
    temp[0][0] = x[0][2]
    temp[0][1] = x[1][2]
    temp[0][2] = x[2][2]
    temp[1][0] = x[0][1]
    temp[1][1] = x[1][1]
    temp[1][2] = x[2][1]
    temp[2][0] = x[0][0]
    temp[2][1] = x[1][0]
    temp[2][2] = x[2][0]
    return temp
print(counterClockwise(clock))
