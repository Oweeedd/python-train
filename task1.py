import re

def convert_special_numbers(string):
    pattern = r"(\d{2,4}\\\d{2,5})"
    matches = re.findall(pattern, string)
    for match in matches:
        special_number = match.split("\\")
        good_number = [num.zfill(4) for num in special_number]
        converted_number = "\\".join(good_number)
        string = string.replace(match, converted_number)
    return string


if __name__ == "__main__":
    input_string = "Адрес 5467\\456. Номер 405\\549 " \
                   "347\\406 42\\329 " \
                   "112\\123 " \
                   "Адрес 23\\6. Номер 404\\54 "
    converted_string = convert_special_numbers(input_string)
    print(converted_string)
