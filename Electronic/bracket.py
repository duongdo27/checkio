def checkio(expression):
    brackets = {'[': ']', '{': '}', '(': ')'}
    ls = []
    for char in expression:
        if char in brackets:
            ls.append(char)
        elif char in brackets.values():
            if len(ls) == 0 or char != brackets[ls.pop()]:
                return False
    return len(ls) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"

