# def xo (string: str) -> bool: 
#     string_lower = string.lower()
#     count_x = string_lower.count("x")
#     count_o = string_lower.count("o")

#     return count_x == count_o

# string = "XoXoXoO"
# result = xo(string)
# print(result)  


def xo(string: str) -> bool: 
    return string.lower().count("x") == string.lower().count("o")