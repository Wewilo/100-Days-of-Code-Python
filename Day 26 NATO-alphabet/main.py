
import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv") 

word = input("Enter a word : ").upper()

nato_alphabet = {value['letter']:value['code'] for key,value in nato_alpha.iterrows()}


result = [nato_alphabet[letter] for letter in word]

print(result)







