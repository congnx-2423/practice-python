import math
a = float(input())
b = float(input())

def checkRightTriangle(a, b, c):
    if (((a * a) == (b * b) + (c * c)) or ((b * b) == (a * a) + (c * c)) or ((c * c) == (a * a) + (b * b))):
        return True

    return False

try:
    c = math.sqrt((a**2) + (b**2))
    if (checkRightTriangle(a, b, c)):
        area = (0.5) * a * b
        print(f"hypotenuse: {c}")
        print(f"area: {area}")
    else:
        print('not right triagle')
except ValueError:
        print('enter number')
