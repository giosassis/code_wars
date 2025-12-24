def unique_in_order(sequence):
    result = []

    for i in sequence:
        if not result or result[-1] != i:
            result.append(i)
    return result

sequence = 'AAAABBBCCDAABBB'
result = unique_in_order(sequence)
print(result)  # Output: ['A', 'B', 'C', 'D', 'A', 'B'] 