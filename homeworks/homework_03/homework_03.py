while True:
    try:
        user_id = input('Please enter you ID (type exit to quit): ')
        if user_id.lower() == 'exit':
            break
        if len(user_id) != 11:
            if len(user_id) > 11:
                print('ID is too long!')
            else:
                print('ID is too short!')
            raise UserWarning
    except ValueError:
        print('ID you entered is not numeric!')
        continue
    except UserWarning:
        print('ID you entered is not 11 digits long')
    else:
        while True:
            user_input = input("Please choose what do you want to know:\
            \n1. owner\'s gender\n2. owner\'s date of birth\n3. owner\'s region of birth\
            \n4. is the ID valid?\n5. exit the program\n")
            gender = int(user_id[0])
            if user_input == '1':
                if gender > 0 and gender < 7:
                    if gender % 2 == 1:
                        print('He is male')
                    else:
                        print('She is female')
                else:
                    print('Wrong 1 number of ID')
                continue
            elif user_input == '2':
                day = user_id[5:7]
                month = user_id[3:5]
                year = user_id[1:3]
                if int(month) >= 1 and int(month) <= 12:
                # needs to be checked 'day' same way, but it's hard :)
                    print(day + '.' + month + '.', end="")
                    if gender == 1 or gender == 2:
                        print('18' + year)
                    elif gender == 3 or gender == 4:
                        print('19' + year)
                    elif gender == 5 or gender == 6:
                        print('20' + year)
                else:
                    print('Wrong 3 and 4 numbers of ID')
                continue
            elif user_input == '3':
                region = int(user_id[7:10])
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
                continue
            elif user_input == '4':
                modul_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                modul_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                user_id = list(user_id)
                i = 0
                sum = 0
                j = 0
                sum2 = 0
                for num in modul_1:
                    mult = int(user_id[i]) * modul_1[i]
                    sum = sum + mult
                    i += 1
                check_1 = int(sum % 11)
                if check_1 >= 10:
                    for num in modul_2:
                        mult = int(user_id[j]) * modul_2[j]
                        sum2 = sum2 + mult
                        j += 1
                    check_2 = int(sum2 % 11)
                    if check_2 >= 10:
                        print('Invalid ID')
                    elif check_2 == int(user_id[10]):
                        print('Valid ID')
                    else:
                        print('Invalid ID')
                elif check_1 == int(user_id[10]):
                    print('Valid ID')
                else:
                    print('Invalid ID')
                continue
            elif user_input == '5':
                break