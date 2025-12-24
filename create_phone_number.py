def create_phone_number (n: list[int]) -> str:
    part_one = "".join(str(num) for num in n[0:3])
    part_two = "".join(str(num) for num in n[3:6])
    part_three = "".join(str(num) for num in n[6:10])

    return f"({part_one}) {part_two}-{part_three}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
phone_number = create_phone_number(numbers)
print(phone_number)  # Output: (123) 456-7890


#####

def teste_com_lista_e_numeros(n: list[int]) -> str:
    return f"{"".join(str(num) for num in n)}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = teste_com_lista_e_numeros(numbers)
print(result)  # Output: 123