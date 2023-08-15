# Note: რადგანაც txt ფაილი აღიქმება როგორც სტრიქონი, მასში მონაცემები(რიცხვები) წერია " " სიმბოლოების გარეშე.
# ყველა დავალება აღქმულია როგორც დამოუკიდებელი დავალება, შესაბამისად მასში მეორდება ცვლადები.

file_path = 'numbers.txt'
# 1
with open(file_path) as file:
    content = file.read()
    print(content)


# # 2
result_path = 'logged_numbers.txt'
with open(file_path) as file, open(result_path, 'w') as f2:
    content = file.read()
    result_strings = content.split(',')

    l_numbers = []

    for str_num in result_strings:
        l_numbers.append(int(str_num.strip()))
    result = sum(l_numbers) / len(l_numbers)

    f2.write(str(result))


# 3
result_path = 'standard_occasions.txt'
with open(file_path) as file, open(result_path, 'a') as f3:
    content = file.read()
    result_string = content.split(',')
    l_numbers = []

    for str_num in result_string:
        l_numbers.append(int(str_num.strip()))
    avg = sum(l_numbers) / len(l_numbers)

    new_list = []
    for num in l_numbers:
        new_list.append(pow((num - avg), 2))
    std_dev = (sum(new_list) / len(new_list)) ** 0.5
    std_error = std_dev / (len(new_list) ** 0.5)

    f3.write(str(std_dev) + '\n')
    f3.write(str(std_error))

# შემდეგ დავალებებში ზედმიწევნითი დუპლიკაციებისგან თავიდან ასარიდებლად
# გამოყენებულია მესამე დავალებაში გამოთვლილი ცვლადები - l_numbers, avg, std_dev


# 4
result_path = 'above_border.txt'
with open(result_path, 'w') as f4:
    border = avg + std_dev
    my_list = []
    for each in l_numbers:
        if each > border:
            my_list.append(str(each))
    result = ', '.join(my_list)

    f4.write(result)

# 5
my_dict = {}
for value in l_numbers:
    my_dict[value] = my_dict.get(value, 0) + 1

max_value = max(my_dict.values())
res = ''

for i in range(max_value):
    row = ''
    for value in my_dict:
        if my_dict[value] >= (max_value - i):
            if value > (avg + std_dev):
                row += '^ '
            else:
                row += '* '
        else:
            row += '  '
    res += row[:-1] + '\n'

print(res)
