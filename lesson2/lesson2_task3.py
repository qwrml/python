import math
def square(side):
    area = side * side
    if side == int(side):
        return area
    else:
        return math.ceil(area)
print(square(5))
print(square(3.2))
print(square(4.7))