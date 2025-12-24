import re

def to_camel_case(text):
    split_string = re.split('[-_]', text)

    if len(split_string) == 1:
        return text
    
    camel_case_string = split_string[0]
    for word in split_string[1:]:
        camel_case_string += word.capitalize()
    return camel_case_string
