import ipdb


def sequece(ls):
    last_num = None
    count = 0
    for num in ls:
        if num == last_num or last_num is None:
            count += 1
            if count >= 4:
                return True
        else:
            count = 1
        last_num = num
    return False


def checkio(matrix):
    for row in matrix:
        if sequece(row):
            return True
    for i in range(len(matrix)):
        col = map(lambda x: x[i], matrix)
        #ipdb.set_trace()
        if sequece(col):
            return True
        diagional = [matrix[j][i-j] for j in range(i+1)]
        if sequece(diagional):
            return True
        diagional = [matrix[j][i+j] for j in range(len(matrix)-i)]
        if sequece(diagional):
            return True
        diagional = [matrix[i+j][j] for j in range(len(matrix)-i)]
        if sequece(diagional):
            return True
        diagional = [matrix[len(matrix)-1-j][i+j] for j in range(len(matrix)-i)]
        if sequece(diagional):
            return True
        print diagional
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
