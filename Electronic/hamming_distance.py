def checkio(n, m):
    n = bin(n)[2:]
    m = bin(m)[2:]
    n = (32- len(n))*'0' + n
    m = (32- len(m))*'0' + m
    count = 0
    for index, value in enumerate(n):
        if value != m[index]:
            count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"