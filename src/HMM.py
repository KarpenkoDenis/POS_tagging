import HMM_lib



class HMM_class:
    # matr_is_created = False;
    # matr_after_w1 = []
    # matr_before_w2 = []
    def __init__(self):
        self.matr_is_created = False;
        self.matr_after_w1 = []
        self.matr_before_w2 = []
    def parsing_biagram(self, probability1, probability2, answers, answers_CART):
        all_classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if not self.matr_is_created:
            [self.matr_after_w1, self.matr_before_w2] = HMM_lib.make_matrixs_p()
            # print(matrix1)
            # print(matrix2)
            self.matr_after_w1 =HMM_lib.normalise(self.matr_after_w1)
            self.matr_before_w2 =HMM_lib.normalise(self.matr_before_w2)
            # print(HMM_lib.normalise(self.matr_before_w2))
            self.matr_is_created = True

        # вероятность что слово word1 принадлежит к какому-лбо класу
        # probability1 = {"1": 0.1, "2":0.3, "3":0.0, "4":0.6}
        # probability1 = [0.1, 0.3, 0.0, 0.6]
        # вероятность что слово word1 принадлежит к какому-лбо класу
        # probability2 = {"1": 0.3, "2":0.2, "3":0.3, "4":0.2}
        # probability2 = [0.3, 0.2, 0.3, 0.2]
        # # вероятность, что после слова word1 находится слово класса
        # probability_after_w1 = {"1": 0.1, "2":0.1, "3":0.5, "4":0.3}
        # # вероятность, что преед словом word2 находится слово класса
        # probability_before_w1 = {"1": 0.4, "2":0.3, "3":0.2, "4":0.1}

        # # матрица вероятностей, что после слова word1 относящемуся к классу i нахоидтся класс j
        # matr_after_w1 = [
        #     [ 0.4, 0.1, 0.2, 0.4],
        #     [ 0.2, 0.4, 0.3, 0.1],
        #     [ 0.1, 0.2, 0.5, 0.2],
        #     [ 0.1, 0.3, 0.3, 0.3]
        # ]
        # # матрица вероятностей, что перед словом word2 относящемуся к классу j нахоидтся класс i
        # matr_before_w2 = [
        #     [0.1, 0.1, 0.3, 0.5],
        #     [0.1, 0.3, 0.5, 0.1],
        #     [0.4, 0.2, 0.1, 0.3],
        #     [0.4, 0.3, 0.1, 0.2]
        # ]
        #print("probability1")
        max_i =0
        max_j=0
        max_prob=0
        # print("-------------------------------------------------------------------------------------------")
        for i in all_classes:
            #print(probability1[i])
            #print("probability2")

            for j  in all_classes:
                #print(probability2[j])
                # print("i:", i, "j:", j)
                # print(matr_after_w1[i][j])
                # print(matr_before_w2[j][i])
                # P(i) * P(j) * P(i|j) * P(j|i)
                # print("i", i)
                # print("j", j)
                # print("probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i] = ", probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i])
                # print("probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i] = ", probability1[max_i] * probability2[max_j] * self.matr_after_w1[max_i][max_j] * self.matr_before_w2[max_j][max_i])
                # if probability1[i]!=0 and probability2[j] !=0:
                #     print([i, j])
                #     print("P(1)", probability1[i])
                #     print("P(2)", probability2[j])
                #     print("P(2|1)", self.matr_after_w1[i][j])
                #     print("P(1|2)", self.matr_before_w2[j][i])
                #     print(probability1[i], " * ",  self.matr_after_w1[i][j], " = ", probability2[j])
                #     print(probability2[j], " * ",  self.matr_before_w2[i][j], " = ", probability1[i])
                if probability1[i] != 0 and probability2[j] != 0:
                    if probability1[i]  * self.matr_after_w1[i][j] > max_prob:
                        max_i = i
                        max_j = j
                        max_prob = probability1[i]  * self.matr_after_w1[i][j]
                # if  probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i] > \
                #     probability1[max_i] * probability2[max_j] * self.matr_after_w1[max_i][max_j] * self.matr_before_w2[max_j][max_i]:
                #     # print(probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i])
                #     max_i = i
                #     max_j = j

                # if probability1[i] * probability2[j] * self.matr_after_w1[i][j] > max_prob:
                #     max_i = i
                #     max_j = j
                #     max_prob = probability1[i] * probability2[j] * self.matr_after_w1[i][j]
                # else:
                #     if probability1[i] * probability2[j] * self.matr_before_w2[j][i] > max_prob:
                #         max_i = i
                #         max_j = j
                #         max_prob = probability1[i] * probability2[j] * self.matr_before_w2[j][i]


                # if  probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i] > \
                #     probability1[max_i] * probability2[max_j] * self.matr_after_w1[max_i][max_j] * self.matr_before_w2[max_j][max_i]:
                #     # print(probability1[i] * probability2[j] * self.matr_after_w1[i][j] * self.matr_before_w2[j][i])
                #     max_i = i
                #     max_j = j
                #     max_prob =
        # if max_prob >= max(probability1) and
        # print([max_i, max_j], " cart= ", answers_CART)
        # print("Correct = ", answers)
        # if answers_CART!=[max_i, max_j]:
        #     print("Wrong?")
        return [max_i, max_j]



# class_of_words = parsing_biagram( "1", "2")
# print(class_of_words)