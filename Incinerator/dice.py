from math import factorial


def cal_combinator(k, n):
    return factorial(n)/(factorial(k)*factorial(n-k))


def probability(dice_number, sides, target):
    if dice_number > target or target > sides*dice_number:
        return 0
    result = 0
    for k in range((target-dice_number)/sides + 1):
        result += (-1)**k * cal_combinator(k, dice_number) * cal_combinator(dice_number-1, target-1-k*sides)
    return float(result)/sides**dice_number

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
