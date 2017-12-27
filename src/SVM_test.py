import numpy as np
from read_groups import make_list_gender
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import  grid_search

from sklearn.svm import SVC



def get_X_y(list, converter):
    np.random.shuffle(list)
    large_list = []
    for m in list:
        large_list = large_list + [[  # converter.convert(m[0]),
            converter.convert(m[1]),
            converter.convert(m[2]),
            m[3]]]
        # print(m)
        # for el in m:
        #     # print(el)
        #     large_list = large_list + [el]
        # print("1")

    # print("large_list", large_list)

    X = []
    for el in large_list:
        X = X + [el[:-1]]
    # print("X ", X)
    y = []
    for el in large_list:
        y = y + [el[-1]]

    return [X, y]


def test(test_X, test_y, clf_test):
    good_tests =  sum(clf_test.predict(test_X) == test_y)
    print("Из ",  len(test_X), " испытаний успешны : ",  good_tests)
    print("В процентном соотношении:", good_tests / len(test_X))
    return good_tests / len(test_X)



def start_test_SVM(train_len, test_len):

    list = make_list_gender(train_len)
    from converter import Converter
    converter = Converter()
    [X, y] = get_X_y(list, converter)
    print("len list", len(list))
    print("len converter", len(converter.mass))

    clf = SVC(  )

    # print("clf.fit start")

    problem = clf.fit(X, y)


    # print("clf.fit finish ")



    # Проверка на новых данных

    test_list = make_list_gender(-test_len)
    print("len test_list", len(test_list))


    [test_X, test_y] = get_X_y(test_list, converter)

    return test(test_X, test_y, clf)





'''
test_result = []
for i in range(1, 15, 2):
    for j in range(20, 90, 20):
        print("start_test_SVM(i=", i,", j=", j,")")
        test_result.append( [i, j, start_test_SVM(i, j)])
        print("------------------------")
print(test_result)

'''
# def gender(word):
#     new_word = [word, word[-2:], word[-3:]]
#     nX = [[ # converter.convert(new_word[0]),
#             converter.convert(new_word[1]),
#             converter.convert(new_word[2])]]
#     print(word, "- ", "муж" if clf.predict(nX) == 1 else "жен")
#     print("Номера: ", nX[0][0], ", ", nX[0][1])
#     print("---------------------------")

# gender("мама")
# gender("папа")
# gender("полрубля")
# gender("владыками")
# gender("электропередачи")
# gender("зануда")
# gender("зануда")
# gender("зануда")
# gender("зануда")
# gender("зануда")
# gender("боец")
# gender("служащий")
# gender("вековой")
# gender("ждущий")
# gender("налог")
# gender("терзаемый")
# gender("гнетущий")
# gender("лвоышдамый")
# gender("авытнашол")
# gender("вавшдыпашв")
# gender("пришла")
# gender("живая")
# gender("любимая")
# gender("летняя")
# gender("монтажнице")
# gender("миллионерша")

