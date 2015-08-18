def calculate_matrix(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    result = 0
    for index, value in enumerate(matrix[0]):
        lower = matrix[1:]
        matrix_inner = map(lambda row: row[:index] + row[index+1:], lower)
        result += (-1)**index * value * calculate_matrix(matrix_inner)
    return result


def checkio(matrix):
    transpose_matrix = [map(lambda x: x[i], matrix) for i in range(len(matrix[0]))]
    return calculate_matrix(matrix) + calculate_matrix(transpose_matrix) == 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
