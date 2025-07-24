def count_words(file_contents: str):
    word_count = 0
    for word in file_contents.split():
        word_count += 1
    return word_count

def count_char(file_contents: str):
    letter_dict = {}

    for letter in list(file_contents):
        # Test if letter exists in dictionary
        lcase_letter = letter.lower()
        if lcase_letter in letter_dict:
            letter_dict[lcase_letter] += 1
        else:
            letter_dict[lcase_letter] = 1
    
    return letter_dict

def sort_on(items):
    return items["count"]

def list_dict_char(letter_dict: dict):
    letter_list = []

    for letter, count in letter_dict.items():
        if letter.isalpha() == True:
            letter_list.append({"char": letter, "count": count})
    
    letter_list.sort(reverse=True, key=sort_on)

    return letter_list

def char_report(file_contents: str):
    num_words = count_words(file_contents)
    dict_char = count_char(file_contents)
    list_char = list_dict_char(dict_char)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    
    for letter in list_char:
        for key in letter:
            print(f'{letter[key]}: {letter["count"]}')


    print('============= END ===============')