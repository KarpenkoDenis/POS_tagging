from os import listdir





'''
word_count - если меньше 0, то все слова
иначе то кол-во, которое указано
'''
def read_from(path, word_count):

    words = open(path)
    # print(words)

    strings = []
    i=0

    for line in words:
        i += 1
        strings.append(line)
    if word_count < 0 or word_count > len(strings) -1:
        word_count = len(strings) -1
    # print(strings)
    words_ending = strings[0]
    # print(words_ending)
    start =0
    end =0

    for i in range(0, len(words_ending)):
        if words_ending[i] == '{':
            start = i+1
        if words_ending[i] == '}':
            end = i
            break
    words_ending = words_ending[start:end]
    words_ending = words_ending.split(",")
    fin_words = []
    # print("words_ending", words_ending)
    for word in strings[1:word_count+1]:
         for end in words_ending:
             fin_words.append(word[:-1] + (end if end != '#' else ""))
    #print("Final words:", fin_words)
    return fin_words


def read_files_from(path, word_count):
    all_words = []
    # print(listdir("./resource/ЖЕН/"))
    for file in listdir(path):
        all_words = all_words + read_from(path + file, word_count)

    # print("all_words:", all_words)
    return all_words


read_files_from("./resource/ЖЕН/", -1)
# read_files_from('./resource/МУЖ/')

