import math
a = float(input())
b = float(input())

try:
    c = math.sqrt((a**2) + (b**2))
    if ((a*a) == (b*b) + (c*c) or (b*b) == (a*a) + (c*c) or (c*c) == (a*a) + (b*b)):
        area = (0.5) * a * b
        print(f"hypotenuse: {c}")
        print(f"area: {area}")
    else:
        print('not right triagle')
except ValueError:
        print('enter number')
