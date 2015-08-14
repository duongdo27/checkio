def checkio(number):
    stri = str(number)
    if number % 3 == 0 and number % 5 == 0:
        stri = "Fizz Buzz"
    elif number % 5 == 0:
        stri = "Buzz"
    elif number % 3 == 0:
        stri = "Fizz"
    return stri


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
