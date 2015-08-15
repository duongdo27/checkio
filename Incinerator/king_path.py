def convert_to_loc(cells):
    start, end = str(cells).split('-')
    return (ord(start[0])-ord('a'), int(start[1])-1), (ord(end[0])-ord('a'), int(end[1])-1)


def next_locs(loc):
    result = set()
    for dx, dy in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        next_x, next_y = loc[0] + dx, loc[1] + dy
        if 0 <= next_x < 8 and 0 <= next_y < 8:
            result.add((next_x, next_y))
    return result


def checkio(cells):
    start, end = convert_to_loc(cells)
    step = 0
    current = {start}
    while True:
        step += 1
        ls = map(next_locs, current)
        current = reduce(set.union, ls)
        if end in current:
            return step

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"b1-d5") == 2, "1st example"
    assert checkio(u"a6-b8") == 1, "2nd example"
    assert checkio(u"h1-g2") == 4, "3rd example"
    assert checkio(u"h8-d7") == 3, "4th example"
    assert checkio(u"a1-h8") == 6, "5th example"
