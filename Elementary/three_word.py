def checkio(words):
    ls = words.split()
    if len(ls) < 3:
        return False
    for i in range(len(ls) - 2):
        if not ls[i].isdigit() and not ls[i+1].isdigit() and not ls[i+2].isdigit():
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"