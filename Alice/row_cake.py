from itertools import combinations


def straight((p1, p2, p3)):
    return (p3[1] - p2[1])*(p3[0] -p1[0]) == (p3[1] - p1[1])*(p3[0] -p2[0])


def checkio(cakes):
    ls = []
    for c in combinations(cakes, 3):
        if straight(c):
            c = {tuple(e) for e in c}
            flag = True
            for index, element in enumerate(ls):
                if len(c&element) >= 2:
                    ls[index] = c|element
                    flag = False
                    break
            if flag:
                ls.append(c)
    return len(ls)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6