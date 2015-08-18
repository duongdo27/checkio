def moveable(first, second):
    ls = [a==b for a, b in zip(str(first), str(second))]
    return sum(ls) == 2


def recursive(available, current, target, acc):
    if moveable(current, target):
        return acc + [target]
    possible = [n for n in available if moveable(current, n)]
    ls = []
    for p in possible:
        next_value = recursive(set(available)-{p}, p, target, acc+[p])
        if next_value:
            ls.append(next_value)
    if len(ls) == 0:
        return None
    return sorted(ls, key=len)[0]


def checkio(numbers):
    return recursive(numbers[1:-1], numbers[0], numbers[-1], [numbers[0]])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"


