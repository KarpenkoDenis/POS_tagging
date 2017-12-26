import numpy as np
from read_data_from_db import read_files_from



'''

list = np.array(make_list_mans_and_womans())

'''
def make_list_mans_and_womans(word_count):
    womans = np.array(read_files_from("./resource/ЖЕН/", word_count))
    mans = np.array(read_files_from('./resource/МУЖ/', word_count))
    list = []
    #y = []
    size = len(womans) if len(womans) < len(mans) else len(mans)  # чтобы было рановное кол-во данных
    for woman in womans: # [:size]:
        list.append([woman, woman[-2:], woman[-3:], 0])
        #y.append(0)
    for man in mans: # [:size]:
        list.append([man, man[-2:], man[-3:], 1])
        #y.append(1)
    # print(list)
    return list    #[list, y]




# print(list)
# print(y)


