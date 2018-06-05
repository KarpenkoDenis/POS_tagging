from converter import Converter
from read_groups import make_list_gender, make_list_parts_of_speech, make_biargams_list_parts_of_speech
from CART_lib import check_data, get_X_y
from sklearn.tree import DecisionTreeClassifier
from HMM import HMM_class

print("df")


def make_mass_len14(mass):
    save = []
    last_p = 0
    for i in range(14):
        if i == 8 or i == 13:  # эти классы не встретились в тексте, поэтому анализатор выдаёт пустые места, которые нужно занулить
            save.append(0.0)
        else:
            save.append(mass[last_p])
            last_p += 1
    return save

def print_result(arr_equals_0, arr_equals_1):

    two_word_good = 0
    for i in range(len(arr_equals_0)):
        two_word_good += 1 if arr_equals_0[i] and arr_equals_1[i] else 0
    only_one_word_good = 0
    for i in range(len(arr_equals_0)):
        only_one_word_good += 1 if (not arr_equals_0[i] and arr_equals_1[i]) or (
                arr_equals_0[i] and not arr_equals_1[i]) else 0
    two_word_wrong = 0
    at_least_one_word_good = 0
    for i in range(len(arr_equals_0)):
        at_least_one_word_good += 1 if arr_equals_0[i] or arr_equals_1[i] else 0
    two_word_wrong = 0
    for i in range(len(arr_equals_0)):
        two_word_wrong += 1 if not arr_equals_0[i] and not arr_equals_1[i] else 0
    print("two_word_good: ", two_word_good / len(arr_equals_0))
    print("at_least_one_word_good: ", at_least_one_word_good/ len(arr_equals_0))
    print("only_one_word_good: ", only_one_word_good/ len(arr_equals_0))
    print("two_word_wrong: ", two_word_wrong/ len(arr_equals_0))


def check_data_biagram(testX_0, testY_0, testX_1, testY_1, model):  # testX, testY, data):
    # two_word_good =  sum(model.predict(testX_0) == testY_0)

    arr_equals_0 = model.predict(testX_0) == testY_0
    arr_equals_1 = model.predict(testX_1) == testY_1
    # print("                 CART results:")
    # print_result(arr_equals_0, arr_equals_1)
    # for i in range(14):
    #     arr_equals_2 = model.predict(testX_1) == i
    #     all_i = sum(arr_equals_2)
    #     print("all_i", all_i) # нет ни одного 8 и 13 в тексте

    # two_word_good = 0
    # for i in range(len(testX_0)):
    #     two_word_good += 1 if arr_equals_0[i] and arr_equals_1[i] else 0
    # only_one_word_good = 0
    # for i in range(len(testX_0)):
    #     only_one_word_good += 1 if (not arr_equals_0[i] and arr_equals_1[i]) or (
    #                 arr_equals_0[i] and not arr_equals_1[i]) else 0
    # two_word_wrong = 0
    # at_least_one_word_good = 0
    # for i in range(len(testX_0)):
    #     at_least_one_word_good += 1 if arr_equals_0[i] or arr_equals_1[i] else 0
    # two_word_wrong = 0
    # for i in range(len(testX_0)):
    #     two_word_wrong += 1 if not arr_equals_0[i] and not arr_equals_1[i] else 0
    #
    # print("two_word_good: ", two_word_good)
    # print("at_least_one_word_good: ", at_least_one_word_good)
    # print("only_one_word_good: ", only_one_word_good)
    # print("two_word_wrong: ", two_word_wrong)

    # тестирование c MHH
    arr_equals_biagrams_0 = []
    arr_equals_biagrams_1 = []
    HMM_model = HMM_class()
    for i in range(len(testY_0)):
        # print("testX_0[i]", testX_0[i])
        # print("testY_0[i]", testY_0[i])
        #
        # print("testX_1[i]", testX_1[i])
        # print("testY_1[i]", testY_1[i])
        #
        # print("predict ", model.predict([testX_0[i]]))
        # save2 = model.predict([testX_0[i]])
        # print("predict_proba testX_0 ", model.predict_proba([testX_0[i]]))
        # print("predict_proba testX_1 ", model.predict_proba([testX_1[i]]))
        predict_vector_0 = model.predict_proba([testX_0[i]])[0]
        predict_vector_1 = model.predict_proba([testX_1[i]])[0]

        predict_vector_0 = make_mass_len14(predict_vector_0)
        predict_vector_1 = make_mass_len14(predict_vector_1)

        # print("changed predict_proba testX_0 ", predict_vector_0)
        # print("changed predict_proba testX_1 ", predict_vector_1)

        class_of_words = HMM_model.parsing_biagram(predict_vector_0, predict_vector_1)

        # print("class_of_words ", class_of_words)
        # print("test_y ", testY_0[i])
        arr_equals_biagrams_0.append(class_of_words[0] == testY_0[i])
        arr_equals_biagrams_1.append(class_of_words[1] == testY_1[i])
        if class_of_words[0] != testY_0[i] or class_of_words[1] != testY_1[i]:
            true_value = [testY_0[i], testY_1[i]]
            predict_value = [model.predict([testX_0[i]]), model.predict([testX_1[i]])]

            # print(class_of_words[0] != testY_0[i])
            # print(class_of_words[1] != testY_1[i])
    print("             HMM + CART results:")
    print_result(arr_equals_biagrams_0, arr_equals_biagrams_1)

    # print(arr_equals_biagrams)
    # good_tests =  sum(model.predict(testX) == testY)
    # good_tests =  sum(model.predict(testX) == testY)

    # for i in range(len(testX_0)):
    #     {
    #         HMM.parsing_biagram()
    #     }
    # print("Получилось")
    #
    # for i in range(len(testY_0)):
    #     print("test_X[i]", testX_0[i])
    #     print("test_y[i]", testY_0[i])
    #     print("predict ", model.predict([testX_0[i]]))
    #     # save = model.predict_proba([testX_0[i]])
    #     # save2 = model.predict([testX_0[i]])
    #     print("predict_proba ", model.predict_proba([testX_0[i]]))
    #     print("predict_proba 1 ", model.predict_proba([testX_0[i]], 1))
    #     print("test_y ", testY_0[i])
    # print("Из ",  len(testX), " испытаний успешны : ",  good_tests)
    # print("В процентном соотношении:", good_tests / len(testX))
    # return good_tests / len(testX)


def check(trainData, testData):
    converter = Converter()
    trainData_0 = []
    for data in trainData:
        trainData_0.append(data[0])
    #  самы слова и так перечислены в первом столбике
    # trainData_1 = []
    # for data in trainData:
    #     trainData_1.append(data[1])

    [X_0, y_0] = get_X_y(trainData_0, converter)

    # [X_1, y_0] = get_X_y(trainData_1, converter)

    print("len train_data", len(trainData))
    print("len converter", len(converter.mass))
    print("len test_data", len(testData))

    model = DecisionTreeClassifier()
    add_all_classes = range(14)
    value_all_classes = [[-1000 - 10000] for i in range(14)]

    # x111 =[X_0, value_all_classes]
    # y111 = [y_0, add_all_classes]


    # model.fit(X_0, y_0)
    model.fit(X_0, y_0)
    testData_0 = []
    for data in testData:
        testData_0.append(data[0])
    testData_1 = []
    for data in testData:
        testData_1.append(data[1])

    [testX_0, testY_0] = get_X_y(testData_0, converter)
    [testX_1, testY_1] = get_X_y(testData_1, converter)

    check_data_biagram(testX_0, testY_0, testX_1, testY_1, model)


def kross_validation():  # кросс валидация

    all_words = make_biargams_list_parts_of_speech(60000)
    print(len(all_words))
    # parts = [all_words[:20000], all_words[20000:40000], all_words[40000:]]
    parts = [all_words[:20000], all_words[20000:40000], all_words[40000:60000], all_words[60000:]]
    parts2 = [all_words[:10000], all_words[10000:20000], all_words[20000:30000], all_words[30000:40000], \
              all_words[50000:60000], all_words[60000:70000], all_words[70000:]]
    parts3 = [all_words[:5000], all_words[5000:10000], all_words[10000:15000], all_words[15000:20000], \
              all_words[20000:25000], all_words[25000:30000]]
    # for i in range(len(parts)):
    #     for j in range(len(parts)):
    #         if i != j:
    #             print("--------------------------------------------------------------")
    #             print("check trainBlock = ", i, "testBlock = ", j)
    #             check(parts[i], parts[j])

    for i in range(len(parts)):
        for j in range(len(parts)):
            if i!=j:
                check(parts[i], parts[j])
    print("------------------------")
    for i in range(len(parts2)):
        for j in range(len(parts2)):
            if i != j:
                check(parts2[i], parts2[j])
    print("------------------------")

    for i in range(len(parts3)):
        for j in range(len(parts3)):
            if i!=j:
                check(parts3[i], parts3[j])

kross_validation()
