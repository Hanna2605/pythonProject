import re

with open('text_homework.txt', 'r', encoding='UTF8') as file:
    data = file.read()

# 1. Search for HTML-colors from file:
    print('1. HTML-colors in the text are:')

    pattern_color = re.compile(r'#[0-9A-Fa-f]{6}')
    matches_color = pattern_color.finditer(data)
    for match in matches_color:
        print(match.group())
    print('\n')

# 2. Definition in the text of numbers that are not followed by a '+' sign:
    print('2. Numbers that are not followed by a '+' sign are:')

    pattern_plus = re.compile(r'(\d)[^+^\n]')
    matches_plus = pattern_plus.finditer(data)
    for match in matches_plus:
        print(match.group(1))
    print('\n')

# 3. Find the time in the text:
    print('3. Find the time in text:')

    data_time = ('Завтрак в 09:00, обед в 14:30, сон в 23:30. Конец света в 55:71')
    pattern_time = re.compile(r'\b([01][0-9]|2[0-3]):([0-5][0-9])\b')
    matches_time = pattern_time.finditer(data_time)
    for match in matches_time:
        print(match.group())
    print('\n')

# 4. Find all names, surnames and addresses in the text:
    print('4. Find all names, surnames and addresses in text:')

with open('people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()

    pattern_name = re.compile(r'^[A-Z][a-z]+ [A-Z][a-z]+', re.M)
    matches_name = list(pattern_name.finditer(people_data))
    pattern_address = re.compile(r'\d{3} [A-Z|0-9][a-z]+ St., [A-Z][a-zA-z\-\']+( ([A-Z][a-z]+))? [A-Z]{2} \d{5}',
                                 re. M)
    matches_address = list(pattern_address.finditer(people_data))
    limit = len(matches_name)
    for i in range(0, limit):
        print(f'{matches_name[i].group()}: {matches_address[i].group()}')
    print('\n')

# 5. String validation:
    print('5. Make string validation:')

    data_string = input('Input string: ')
    pattern_string = re.compile(r'[A-Za-z0-9]*')
    matches_string = pattern_string.fullmatch(data_string)
    if matches_string == None:
        print("Sorry,your string doesn't meet the condition!")
    else:
        print('Congratulations, everything is OK!')
    print('\n')

# 6. Isikukood:
    print('6. Check ISIKUKOOD validation:')

    data_id = input('Input ISIKUKOOD: ')
    pattern_id = re.compile(r'[1-6][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
    matches_id = pattern_id.fullmatch(data_id)
    if matches_id == None:
        print("Sorry,your isikukood is invalid!")
    else:
        print('Congratulations, your isikukood is valid!')
