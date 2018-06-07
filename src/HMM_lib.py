import XML_pars



def make_matrixs_p(len=4000):
    sentences = XML_pars.get_data(len)
    # weight = 10 # вес( во сколько раз значения слова важнее
    # создаём пустые матрицы ,перед их наполнением
    matr_after_w1 = [[0.0 for y in range(14)] for x in range(14)]
    matr_before_w2 = [[0.0 for y in range(14)] for x in range(14)]

    for sen in sentences:
        dictitems = sen.getElementsByTagName("dictitem")
        first_word = None
        for dictitem in dictitems[1:]:
            if(first_word==None): #если предыдущее слово ещё не было установлено
                first_word = dictitem.getAttribute("subpart_of_speech")
                # print(dictitem.getAttribute("subpart_of_speech"))
            else:
                second_word = dictitem.getAttribute("subpart_of_speech")
                i = int(first_word)
                j = int(second_word)
                matr_after_w1[i][j] +=1
                matr_before_w2[j][i] +=1
                first_word = second_word
    return [matr_after_w1, matr_before_w2]



def normalise(matrix):
    # сглаживание ( убираем нулевые вероятности)
    # k = 0.01 # коэффициент на сколько сглаживаем
    for line in matrix:
        line_len = sum(line)
        for i in range(len(line)):
            # line[i]+=k*line_len
            line[i]+=1


    for line in matrix:
        sum_line = sum(line)
        for i in range(len(line)):
            if sum_line!=0:
                line[i] = line[i]/sum_line

    return matrix
# [matrix1, matrix2] = make_matrixs_p()
# print(matrix1)
# print(matrix2)
# print(normalise(matrix1))
# print(normalise(matrix2))

