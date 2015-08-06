a_factaral = lambda x: 1+(x > 0 and x*a_factaral(x-1)-1)
print a_factaral(5)