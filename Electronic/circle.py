from math import sqrt

def checkio(data):
   # data = [char for char in data if char.isdigit()]
    mid1 = (int(data[0][0]) + int(data[1][0]))/2, (int(data[0][1]) + int(data[1][1]))/2
    mid2 = (int(data[0][0]) + int(data[2][0]))/2, (int(data[0][1]) + int(data[2][1]))/2
    k1 = -1.0*((int(data[1][1])- int(data[0][1]))/(int(data[1][0])- int(data[0][0])))
    k2 = -1.0*((int(data[2][1])- int(data[0][1]))/(int(data[2][0])- int(data[0][0])))
    x0 = mid1[0] + k1 * (mid1[0]-mid2[0])/(k2-k1)
    y0 = mid1[1] + k1 * (mid1[1]-mid2[1])/(k2-k1)
    r = sqrt((x0-mid1[0])**2 + (y0-mid1[1])**2))
    #replace this for solution
    return "(x-{})^2+(y-{})^2={}^2".format(x0, y0, r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"