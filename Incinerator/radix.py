def checkio(number):
    ls = map(lambda x: int(x) if x.isdigit() else ord(x) - ord('A') + 10, number)
    print ls
    for k in range(max(ls)+1, 37):
        value = 0
        for index, num in enumerate(ls):
            value += num * k**(len(ls)-index-1)
        if value % (k-1) == 0:
            return k
    print value, k
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    print('Local tests done')
