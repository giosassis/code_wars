# def is_triangle(a: int, b: int, c: int) -> bool:
#     return a + b > c and a + c > b and b + c > a


## option with lambda 

is_triangle = lambda a, b, c: a + b > c and a + c > b and b + c > a

print(is_triangle(1, 2, 3))  # False
print(is_triangle(3, 4, 5))  # True
print(is_triangle(5, 10, 25))  # False
print(is_triangle(7, 10, 5))  # True
print(is_triangle(10, 10, 10))  # True
