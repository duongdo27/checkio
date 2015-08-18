def compute(first, second, mode):
    ls1 = map(int, bin(first)[2:])
    ls2 = map(int, bin(second)[2:])
    result = 0
    for num1 in ls1:
        if mode == 'AND':
            ls = [num1 & num2 for num2 in ls2]
        elif mode == 'OR':
            ls = [num1 | num2 for num2 in ls2]
        else:
            ls = [num1 ^ num2 for num2 in ls2]
        result += int(''.join(map(str, ls)), 2)
    return result


def checkio(first, second):
    return compute(first, second, 'AND') + compute(first, second, 'OR') + compute(first, second, 'XOR')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18