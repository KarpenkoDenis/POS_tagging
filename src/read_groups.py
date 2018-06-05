import numpy as np
from read_data_from_db import read_files_from
import XML_pars


'''

list = np.array(make_list_mans_and_womans())

'''


def words_separator1(list):
    new_list=[]
    for w in list:  # [:size]:
        new_list.append([w[0], w[0][-2:], w[0][-3:], w[1]])
    return new_list
def word_separator1(word):
    # new_list=[]
    # for w in list:  # [:size]:
    #     new_list.append([w[0], w[0][-2:], w[0][-3:], w[1]])
    return [word[0], word[0][-2:], word[0][-3:], word[1]]

def words_separator2(list):  # разбивает слово на три последние буквы
    new_list=[]
    for w in list:  # [:size]:
        new_list.append([w[0][-3:-2], w[0][-2:-1], w[0][-1:], w[1]])
    return new_list


def make_list_gender(word_count, separator =None):
    if separator == None:
        separator=words_separator1
    womans = np.array(read_files_from("./resource/ЖЕН/", word_count))
    mans = np.array(read_files_from('./resource/МУЖ/', word_count))
    its = np.array(read_files_from('./resource/ОНО/', word_count))
    list = []
    for el in womans:
        list.append([el, 1])
    for el in mans:
        list.append([el, 2])
    for el in its:
        list.append([el, 3])

    return separator(list)



def make_list_parts_of_speech(word_count=1000, random = False, separator =None):
    if separator == None:
        separator=words_separator1
    words = XML_pars.get_words_POS(word_count)

    list = []

    for w in words:
        list.append([w[0], w[0][-2:], w[0][-3:], w[1]])

    return list

def make_biargams_list_parts_of_speech(word_count=1000, random = False, separator =None):
    biagrams = XML_pars.get_words_biagram_POS(word_count)

    # list = []
    converted_biagrams = []
    for b in biagrams:
        converted_biagrams.append([word_separator1(b[0]), word_separator1(b[1])])

        # list.append([w[0], w[0][-2:], w[0][-3:], w[1]])

    return converted_biagrams

# print(make_list_parts_of_speech())
# print(list)
# print(y)


