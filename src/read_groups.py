import numpy as np
from read_data_from_db import read_files_from



'''

list = np.array(make_list_mans_and_womans())

'''


def words_separator1(list):
    new_list=[]
    for w in list:  # [:size]:
        new_list.append([w[0], w[0][-2:], w[0][-3:], w[1]])
    return new_list


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






# print(list)
# print(y)


