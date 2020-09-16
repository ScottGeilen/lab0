# string can be any length
# Take string
# 
# Write a function:
# Name: remove_words_in_str()
# Modify the string to remove all occurrances of words defined in list
# Parameters: 
#   str - String that needs to be modified
#   list - List of words that needs to be removed
# Return: modified str without the words in the list
# Ex
#   str: This is an example
#   list: ['an', 'is', 'a']
# Return: This is example
import regex as re

def remove_words_in_str(data, words):
    new_list = data.split(' ')
    for i in words:
        if i in new_list:
            new_list.remove(i)
    new_str = ' '.join(new_list)
    print(new_str)
    return new_str
remove_words_in_str('This is an example', ['an', 'is', 'a'])

def remove_words_in_str2(sentence, word_list):
    sentence_list = re.split(r'[\s,]+', sentence)
    return_stentence_as_list = []
    for word in sentence_list:
        if word not in word_list:
            return_stentence_as_list.append(word)
    return ' '.join(return_stentence_as_list)
print(remove_words_in_str2('This.is.an.example', ['an', 'is', 'a']))
# def get_delim(sentence):
#     delim = ''
#     for ch in sentence:
#         if ch in string.punctuation:
#             return ch
# get_delim('This.is.an.example')