from math import sqrt
import ipdb


def fomat(num):
    num = round(num, 2)
    if int(num) == num:
        return int(num)
    return num


def checkio(data):
    x1, y1, x2, y2, x3, y3 = map(int, str(data).translate(None, '()').split(','))
    mx1, my1 = (x1 + x2)/2.0, (y1 + y2)/2.0
    mx2, my2 = (x1 + x3)/2.0, (y1 + y3)/2.0
    kx1, ky1 = y1-y2, x2-x1
    kx2, ky2 = y1-y3, x3-x1
    # y-my1 = (ky1/kx1)(x-mx1) --> kx1*(y-my1) = ky1*(x-mx1) --> kx1*kx2*(y-my1) = kx2*ky1*(x-mx1)
    # y-my2 = (ky2/kx2)(x-mx2) --> kx2*(y-my2) = ky2*(x-mx2) --> kx1*kx2*(y-my2) = kx1*ky2*(x-mx2)
    # --> (my2-my1) * kx1 * kx2 = x(kx2*ky1-kx1*ky2) + mx2*kx1*ky2 - mx1*kx2*ky1
    x = ((my2-my1) * kx1 * kx2 - mx2*kx1*ky2 + mx1*kx2*ky1)/(kx2*ky1-kx1*ky2)
    y = ((mx2-mx1) * ky1 * ky2 - my2*ky1*kx2 + my1*ky2*kx1)/(ky2*kx1-ky1*kx2)
    r = sqrt((x-x1)**2 + (y-y1)**2)
    x, y, r = fomat(x), fomat(y), fomat(r)
    #replace this for solution
    result = "(x-{})^2+(y-{})^2={}^2".format(x, y, r)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
