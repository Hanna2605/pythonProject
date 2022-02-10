import csv
import time
from operator import itemgetter

def user_input():
    global user_country
    user_country = input('Please select how many countries out of 156 you would like to compare (type EXIT to quit): ')
    if user_country.lower() == 'exit':
        quit()
    else:
        try:
            if int(user_country) <= 0 or int(user_country) > numCountries:
                print('Number is out of range')
                return False
        except ValueError:
            print('Value you entered is not numeric!')
            return False
    return True

def comparison():
    global user_compare
    user_compare = int(input('Please choose number what do you want to know or do:\n'
                        '1. Score\n'
                        '2. GDP per capita\n'
                        '3. Social support\n'
                        '4. Healthy life expectancy\n'
                        '5. Freedom to make life choices\n'
                        '6. Generosity\n'
                        '7. Perceptions of corruption\n'
                        '8. Сhoose another number of countries to compare\n'
                        '9. Quit program\n'))
    if user_compare == 9:
        quit()
    if user_compare == 8:
        return False
    return True

def Sort_values(j):
    global datalist
    print(f'{header[1]}, {header[j]}')
    datalist = sorted(datalist, key=itemgetter(j), reverse=True)
    i = 0
    for data in datalist:
        if i < int(user_country):
            print(f'{datalist[i][1]}, {datalist[i][j]}')
            i += 1
    return

with open('2019.csv', 'r', encoding='UTF8') as csv_file:
    csv_reader = csv.reader(csv_file)
    datalist = []
    header = next(csv_reader)
    for line in csv_reader:
        datalist.append(line)
    numCountries = len(datalist)
    while True:
        while user_input() == True:
            while comparison() == True:
                if user_compare < 1 or user_compare > 9:
                    print('Сhoice beyond possibility')
                    continue
                Sort_values(user_compare + 1)
                time.sleep(2.5)
















