def break_line(text):
    ls = str(text).split('\n')
    return map(lambda x: x.lower().replace(' ', ''), ls)


def tranpose_lines(lines):
    leng = max(map(len, lines))
    result = []
    for i in range(leng):
        column = map(lambda x: x[i] if i < len(x) else ' ', lines)
        result.append(''.join(column))
    return result


def checkio(text, word):
    word = str(word)
    lines = break_line(text)
    for row, line in enumerate(lines):
        if word in line:
            return [row+1, line.index(word)+1, row+1, line.index(word) + len(word)]
    columns = tranpose_lines(lines)
    for col, column in enumerate(columns):
        if word in column:
            return [column.index(word)+1, col+1, column.index(word) + len(word), col+1]



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]