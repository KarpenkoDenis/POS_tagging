from os import listdir





'''
word_count - если меньше 0, то все слова
иначе то кол-во, которое указано
'''


def add_ends_to_word(word, ends):
    fin_words = []
    # print("words_ending", words_ending)
    ends = ends_parser(ends)
    for end in ends:
        fin_words.append(word + (end if end != '#' else ""))
    return fin_words

def ends_parser(words_ending):
    start = 0
    end =0
    save_ending = []
    curr_end = ""
    inline = False
    for i in range(0, len(words_ending)):
        if inline:
            if words_ending[i] == ',' and words_ending[i-1] == '}':
                inline = False
            continue
        elif words_ending[i] ==',':
            save_ending = save_ending + [curr_end]
            curr_end = ""
        elif words_ending[i] == '{':
            if start !=0:
                # ends = ends_parser(words_ending[start:])
                save_ending = save_ending + add_ends_to_word(curr_end, words_ending[i:])
                inline = True
                curr_end = ""
            start = i + 1
        elif words_ending[i] == '}':
            save_ending = save_ending + [curr_end]
            end = i
            break
        else:
            curr_end = curr_end + words_ending[i]
    return save_ending

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
    words_ending = strings[0]

    ends_mass= ends_parser(words_ending)

    fin_words = []
    # print("words_ending", ends_mass)
    for word in strings[1:word_count+1]:
         for end in ends_mass:
             fin_words.append(word[:-1] + (end if end != '#' else ""))
    print("Final words:", fin_words)
    return fin_words


def read_files_from(path, word_count):
    all_words = []
    # print(listdir("./resource/ЖЕН/"))
    i=0
    for file in listdir(path):
        print(i)
        all_words = all_words + read_from(path + file, word_count)
        i+=1

    # print("all_words:", all_words)
    return all_words

def read_files_from_name(path, name):
    all_words =  read_from(path + name, -1)

    # print("all_words:", all_words)
    return all_words

'''

# пример

ends_parser("{ел,л{а,у},в{щл{1,2,3},jiodf,ji,о,ш},шо,оа}")

print("-------------")

ends_parser("{ел,л{а,у},в{щл,jiodf,ji,о,ш},шо,оа}")
add_ends_to_word("123", "{ел,л{а,у},в{щл,jiodf,ji,о,ш},шо,оа}")


'''

'''
read_files_from_name("./resource/ЖЕН/", "lexgroup.031")
read_files_from('./resource/МУЖ/')

'''