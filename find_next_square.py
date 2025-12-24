import math

def find_next_square(sq: int) -> int: 
    #check if number is a perfect square
    square_root = math.isqrt(sq)

    if square_root * square_root != sq:
        return -1
    
    return (square_root + 1) ** 2

# Test cases
test_values = [121, 625, 114, 144, 169]
for value in test_values:
    result = find_next_square(value)
    print(f"Next square after {value} is {result}")

    