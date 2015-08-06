import ipdb


def normalize(word):
    return ''.join([c for c in word.lower() if c.isalpha()])


def likeness(word1, word2):
    result = 0
    if word1[0] == word2[0]:
        result += 10
    if word1[-1] == word2[-1]:
        result += 10
    result += 30.0 * min(len(word1), len(word2))/max(len(word1), len(word2))
    result += 50.0 * len(set(word1) & set(word2)) / len(set(word1) | set(word2))
    return result


def find_word(message):
    words = message.split()
    words = map(normalize, words)
    scores = []
    for index, word in enumerate(words):
        score = 0
        for other in words[:index] + words[index+1:]:
            score += likeness(word, other)
        scores.append(score)
    max_i = len(scores) - scores[::-1].index(max(scores)) - 1
    return words[max_i]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"


