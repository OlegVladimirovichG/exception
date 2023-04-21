def sum2d(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(5):
            val = int(arr[i][j])
            sum += val
    return sum