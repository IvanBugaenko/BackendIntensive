def nearest_zero(array: list):

    null_index = array.index(0)

    for i in range(0, len(array)):
        if array[i] == 0:
            null_index = i
        else:
            array[i] = abs(null_index - i)

    for i in range(len(array) - 1, -1, -1):
        if array[i] == 0:
            null_index = i
        else:
            array[i] = min(abs(null_index - i), array[i])

    print(*array)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    nearest_zero(arr)
