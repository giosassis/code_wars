def spin_words(string: str) -> str:
    words = string.split()
    new_list = []

    for word in words: 
        if len(word) > 5:
            new_list.append(word[::-1])
        else:
            new_list.append(word)
    return " ".join(new_list)

test_string = "Hello everyone this is a simple test string"
result = spin_words(test_string)
print(result)  # Output: "Hello enoyreve this is a elpmis test