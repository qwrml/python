def square(side):
    area = side * side
    if side == int(side):
        return area
    else:
        return int(area) + 1
print(square(5))
print(square(3.2))
print(square(4.7))