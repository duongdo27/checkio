from math import pi, atanh, asin, sqrt


def checkio(height, width):
    c = height/2.0
    a = width/2.0
    volume = 4 * pi * a **2 * c/3
    if c > a:   # prolate
        e = sqrt(1-a**2/c**2)
        surface = 2*pi*a**2*(1 + c/(a*e)*asin(e))
    elif c < a:     # oblate
        e = sqrt(1-(c**2/a**2))
        surface = 2*pi*a**2*(1 + ((1-e**2)/e)*atanh(e))
    else:
        surface = 4 * pi * a**2
    return [round(volume, 2), round(surface, 2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"