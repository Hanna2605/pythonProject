with open('trimushketera.txt', 'r', encoding='UTF8') as file:
    data = file.read()
    words = data.split()
    unique_words = list()
    counter_bad_words = 0
    for word in words:
        word = word.lower().strip(',.!?"()*-:;1234567890')
        if word == '':
            counter_bad_words += 1
        elif word not in unique_words:
            unique_words.append(word)
    unique_words.sort()
    len_all_words = len(words) - counter_bad_words
    len_unique = len(unique_words)
    outfile = open('outhomework.txt', 'w', encoding='UTF8')
    outfile.write(f'There are {len_all_words} words in trimushketera.txt\n')
    outfile.write(f'There are {len_unique} unique words in trimushketera.txt\n')
    outfile.write('\n'.join(unique_words))
    outfile.close()






