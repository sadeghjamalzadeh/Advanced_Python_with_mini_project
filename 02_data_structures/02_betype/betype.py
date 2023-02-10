string = input()
true_string_list = []
string_to_list = [i for i in string]
for char in string_to_list:
    if char != '=':
        true_string_list.append(char)
    elif char == '=' and len(true_string_list) != 0:
        true_string_list.pop()
print(''.join(true_string_list))


