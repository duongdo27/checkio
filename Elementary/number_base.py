def checkio(str_number, radix):
    result = 0
    for index, char in enumerate(str_number):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - ord('A') + 10
        if value >= radix:
            return -1
        result += value*(radix**(len(str_number) - index - 1))
    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
