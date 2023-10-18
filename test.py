def transform_input(input_string):
    # Remove any non-digit characters from the input string
    digits = ''.join(filter(str.isdigit, input_string))

    # Perform some operations on the digits to create the desired result
    result = ''
    for digit in digits:
        if int(digit) % 2 == 0:
            result += chr(ord('A') + int(digit) // 2)  # Convert even digits to uppercase letters
        else:
            result += str(int(digit) // 2)  # Convert odd digits to half their value

    # final_str = result[:8].ljust(8, '0')
    # final_str = convert_special_string(result)

    return result

def convert_special_string(special_string):
    # Remove any non-alphanumeric characters from the input string
    alphanumeric_string = ''.join(char for char in special_string if char.isalnum())
    
    # If the alphanumeric string is already 8 characters long, return it as is
    if len(alphanumeric_string) == 8:
        return alphanumeric_string
    
    # If the alphanumeric string is shorter than 8 characters, pad it with random characters
    if len(alphanumeric_string) < 8:
        padding_length = 8 - len(alphanumeric_string)
        padding = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(padding_length))
        padded_string = alphanumeric_string + padding
        return padded_string
    
    # If the alphanumeric string is longer than 8 characters, truncate it to 8 characters
    if len(alphanumeric_string) > 8:
        truncated_string = alphanumeric_string[:8]
        return truncated_string

input_string = "2122170208060103"
result = transform_input(input_string)
print(result)
