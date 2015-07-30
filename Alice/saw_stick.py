from math import sqrt


def checkio(number):
    estimate = int(sqrt(2*number))
    if estimate * (estimate+1) > 2 * number:
        max_index = estimate - 1
    else:
        max_index = estimate
    for start_index in range(1, max_index+1):
        check_sum = 0
        for follow_index in range(start_index, max_index + 1):
            check_sum += follow_index*(follow_index+1)/2
            if check_sum == number:
                return map(lambda x: x*(x+1)/2, range(start_index, follow_index+1))
            if check_sum > number:
                break
    return []

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"

