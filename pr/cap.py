def convert_and_insert_space(input_string):
    result = ""
    for char in input_string:
        if char.isalpha():
            result += char.upper()
        elif char.isnumeric():
            result += " " + char
        else:
            result += char

    return result

# call function to execute:
result = convert_and_insert_space("uzb034")
print(result)
