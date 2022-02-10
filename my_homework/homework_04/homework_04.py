import time

def input_id():
    global user_id
    user_id = input('Please enter you ID (type exit to quit): ')
    if user_id.lower() == 'exit':
        quit()
    else:
        try:
            int(user_id)
            if len(user_id) != 11:
                raise UserWarning
        except ValueError:
            print('ID you entered is not numeric!')
            return False
        except UserWarning:
            if len(user_id) > 11:
                print('ID is too long!')
                return False
            else:
                print('ID is too short!')
                return False
    return True

def user_in():
    global user_input
    user_input = input("Please choose what do you want to know:\n"
                       "1. owner\'s gender\n"
                       "2. owner\'s date of birth\n"
                       "3. owner\'s region of birth\n"
                       "4. is the ID valid?\n"
                       "5. exit the program\n")
    return user_input

def gender(gender):
    if gender > 0 and gender < 7:
        if gender % 2 == 1:
            print('He is male')
        else:
            print('She is female')
    else:
        print('Wrong 1 number of ID')

def birth(gender):
    day = user_id[5:7]
    month = user_id[3:5]
    year = user_id[1:3]
    if int(month) >= 1 and int(month) <= 12:
        print(day + '.' + str(month) + '.', end="")
        if gender == 1 or gender == 2:
            print('18' + year)
        elif gender == 3 or gender == 4:
            print('19' + year)
        elif gender == 5 or gender == 6:
            print('20' + year)
    else:
        print('Wrong 3 and 4 numbers of ID')

def region(region):
    if region >= 1 and region <= 10:
        print('Kuressaare haigla')
    elif region >= 11 and region <= 19:
        print('Tartu Ülikooli Naistekliinik')
    elif region >= 21 and region <= 150:
        print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
    elif region >= 151 and region <= 160:
        print('Keila haigla')
    elif region >= 161 and region <= 220:
        print('Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
    elif region >= 221 and region <= 270:
        print('Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi')
    elif region >= 271 and region <= 370:
        print('Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
    elif region >= 371 and region <= 420:
        print('Narva haigla')
    elif region >= 421 and region <= 470:
        print('Pärnu haigla')
    elif region >= 471 and region <= 490:
        print('Haapsalu haigla')
    elif region >= 491 and region <= 520:
        print('Järvamaa haigla (Paide)')
    elif region >= 521 and region <= 570:
        print('Rakvere haigla, Tapa haigla')
    elif region >= 571 and region <= 600:
        print('Valga haigla')
    elif region >= 601 and region <= 650:
        print('Viljandi haigla')
    elif region >= 651 and region <= 700:
        print('Lõuna-Eesti haigla (Võru), Põlva haigla')
    else:
        print('Wrong 7,8,9 numbers of ID')

def validation(id):
    modul_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    modul_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    i = 0
    sum = 0
    for num in modul_1:
        sum += num * int(id[i])
        i += 1
    if sum % 11 != 10:
        if sum % 11 == int(id[10]):
            print('Valid ID')
        else:
            print('Invalid ID')
    else:
        i = 0
        sum = 0
        for num in modul_2:
            sum += num * int(id[i])
            i += 1
        if sum % 11 != 10:
            if sum % 11 == int(id[10]):
                print('Valid ID')
            else:
                print('Invalid ID')

while True:
    while input_id() == True:
        while True:
            user_in()
            first_num = user_id[0]
            region_birth = user_id[7:10]
            if user_input == '1':
                gender(int(first_num))
                time.sleep(2)
                continue
            elif user_input == '2':
                birth(int(first_num))
                time.sleep(2)
                continue
            elif user_input == '3':
                region(int(region_birth))
                time.sleep(2)
                continue
            elif user_input == '4':
                validation(user_id)
                time.sleep(2)
                continue
            elif user_input == '5':
                break
    else:
        continue






