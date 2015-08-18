def convert(numerator, denominator):
    ls1 = []
    ls2 = []
    whole = numerator/denominator
    num = numerator%denominator
    while True:
        if num == 0:
            return str(whole) + '.' + ''.join(map(str, ls2))
        if num in ls1:
            index = ls1.index(num)
            return str(whole) + '.' + ''.join(map(str, ls2[:index])) + '(' + ''.join(map(str, ls2[index:])) + ')'
        ls1.append(num)
        dec = 10*num/denominator
        ls2.append(dec)
        num = (10*num)%denominator


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"