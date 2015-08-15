LETTERS = 'ADFGVX'


def convert_to_pair(char, secret_alphabet):
    index = secret_alphabet.index(char)
    row = index/len(LETTERS)
    column = index % len(LETTERS)
    return LETTERS[row] + LETTERS[column]


def refine_keyword(keyword):
    result = ''
    for char in keyword:
        if char not in result:
            result += char
    return result


def get_order(keyword):
    ls = sorted(enumerate(keyword), key=lambda x: x[1])
    return map(lambda x: x[0], ls)


def encode(message, secret_alphabet, keyword):
    keyword = refine_keyword(keyword)
    message = [c for c in message.lower() if c.isalnum()]
    level1 = ''.join([convert_to_pair(c, secret_alphabet) for c in message])
    patch = (len(keyword) - len(level1)) % len(keyword)
    level1 = list(level1) + [''] * patch
    ls = [level1[index:index+len(keyword)] for index in range(0, len(level1), len(keyword))]
    result = ''
    for column in get_order(keyword):
        result += ''.join(map(lambda x: x[column], ls))
    return result


def convert_to_letter(char, secret_alphabet):
    index = LETTERS.index(char[0]) * len(LETTERS) + LETTERS.index(char[1])
    return secret_alphabet[index]


def decode(message, secret_alphabet, keyword):
    keyword = refine_keyword(keyword)
    message = list(message)
    patches = range(len(message) % len(keyword), len(keyword))
    order = get_order(keyword)
    rows = len(message)/len(keyword) + 1
    for index in range(len(keyword)):
        if order[index] in patches:
            message.insert(index*rows+rows-1, '')
    pairs = ''
    for row in range(rows):
        for index in range(len(keyword)):
            column = order.index(index)
            loc = column*rows + row
            pairs += message[loc]
    ls = [''.join([pairs[i], pairs[i+1]]) for i in range(0, len(pairs)-1, 2)]
    print ls
    result = ''
    for element in ls:
        result += convert_to_letter(element, secret_alphabet)
    print result
    return result


if __name__ == '__main__':
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    # assert encode("attack at 12:00 am",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    # assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'attackat1200am', "decode attack"
    # assert encode("ditiszeergeheim",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    # assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    # assert encode("I am going",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    # assert decode("DXGAXAAXXVDDFGFX",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'iamgoing', "decode weasel == weasl"
