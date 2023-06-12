def max_conc_num(str_list):
    sorted_list = sorted(str_list, reverse=True)
    max_number = "".join(sorted_list)
    return int(max_number)


strings = ["21", "99990", "4", "35"]
result = max_conc_num(strings)
print(result)