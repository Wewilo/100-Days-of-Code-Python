

import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv") 

nato_alphabet = {value['letter']:value['code'] for key,value in nato_alpha.iterrows()}

while True:
    
    word = input("Enter a word : ").upper()

    try:
        result = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print('Only letters from alphabet')
    else:
        print(result)
        break









