def convert_number_to_string(number):
    mapping = {
        '0': 'J',
        '1': '0',
        '2': 'D',
        '3': '6',
        '4': 'e',
        '5': 'A',
        '6': 'B',
        '7': '6',
        '8': 'J',
        '9': '0'
    }
    
    result = ""
    number_str = str(number)
    
    for digit in number_str:
        result += mapping[digit]
    
    return result

number = 866210032898147
converted_string = convert_number_to_string(number)
print(converted_string)
