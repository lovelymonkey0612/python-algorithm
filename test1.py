import hashlib

def generate_special_code(number):
    # Convert the number to a string
    number_str = str(number)

    # Create a hash object using the SHA256 algorithm
    hash_object = hashlib.sha256()

    # Update the hash object with the number string
    hash_object.update(number_str.encode())

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

    # Convert the hexadecimal hash to a special code
    special_code = ""
    for char in hash_hex:
        if char.isdigit():
            special_code += chr(ord(char) + 16)
        else:
            special_code += chr(ord(char) - 16)

    result = convert_special_string(special_code)
    result1 = transform_input(result)

    return result1

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

def transform_input(input_string):
    convert_String = omit_special_String(input_string)
    digits = ''.join(filter(str.isdigit, str(convert_String)))

    # Perform some operations on the digits to create the desired result
    result = ''
    for digit in digits:
        if int(digit) % 2 == 0:
            result += chr(ord('A') + int(digit) // 2)  # Convert even digits to uppercase letters
        else:
            result += str(int(digit) // 2)  # Convert odd digits to half their value

    final_str = result[:8].ljust(8, '0')
    # final_str = convert_special_string(result)

    return final_str

def omit_special_String(input_string):
    special_char = "@"
    convert_string = input_string.replace(special_char, "")
    final_String = convert_string_number(convert_string)

    return final_String


def convert_string_number(string):
    mapping = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26
    }
    number = 0
    for char in string:
        number = number * 100 + mapping.get(char, 0)

    return number

def convert_string_number(string):
    mapping = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26
    }
    number = 0
    for char in string:
        number = number * 100 + mapping.get(char, 0)

    return number

# Example usage
input_number = 864556041199668
special_code = generate_special_code(input_number)
print(special_code)
