#Task you have a string I like to learn Python! It seems like the easiest from the powerfull programming languages to learn
'''
task 1 -> print length of the string
task 2 -> print quantity of words in the phrase
task 3 -> split string to list and replace vowels to special symbols
task 4 -> list with substite symbol should be converted into list
'''

#Task1 -> print length of the string
phrase = 'I like to learn Python! It seems like the easiest from the powerful programming languages to learn'
print(len(phrase))

#Task2 -> print quantity of words in the phrase
phrase = 'I like to learn Python! It seems like the easiest from the powerful programming languages to learn'
countOfWords = (len(phrase.split()))
print(countOfWords)

#taks3 -> split string to list and replace vowels to special symbols
phrase = 'I like to learn Python! It seems like the easiest from the powerful programming languages to learn'
# convertTolist = list(phrase) #trying to do it with list method
# print(convertTolist) #I got each value in the string even a space as item of list, which is not a great solution
# convertion = phrase.split(' ')
# print(type(convertion))

def convertReplace(phrase, substitute):
    all_vowels = 'AEIOUaeiou'
    for characters in all_vowels:
        phrase = phrase.replace(characters, substitute)
        phrase_final = phrase.split(' ')
    return phrase_final

subsitute = '@'

print("I am printing the sentence where all vowels are substituted with symbol @ and converted to list", convertReplace(phrase, subsitute))
task4 = convertReplace(phrase,subsitute)
print(task4)

#Task4 list with substite symbol should be converted into list
result_of_task4 = ' '.join(task4)
print(result_of_task4)
