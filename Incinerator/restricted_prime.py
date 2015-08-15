def check_prime(number):
    one = int(True)
    num = one + one
    while num < number:
        a = num
        while a < number:
            a += num
            if a == number:
                return False
        num += one
    return True


assert check_prime(37) == True, "GG"