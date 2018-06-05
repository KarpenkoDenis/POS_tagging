import numpy as np
from read_groups import make_list_gender, make_list_parts_of_speech
from sklearn import metrics
# from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier


from sklearn.externals import joblib # для сохранения модели



def get_X_y(list, converter):
    np.random.shuffle(list)
    large_list = []
    for m in list:
        large_list = large_list + [[  # converter.convert(m[0]),
            converter.convert(m[1]),
            converter.convert(m[2]),
            m[3]]]

    X = []
    for el in large_list:
        X = X + [el[:-1]]
    # print("X ", X)
    y = []
    for el in large_list:
        y = y + [el[-1]]

    return [X, y]


def check_data(test_X, test_y, data):
    good_tests =  sum(data.predict(test_X) == test_y)
    # print("Получилось")
    #
    # for i in range(len(test_y)):
    #     print("test_X[i]", test_X[i])
    #     print("test_y[i]", test_y[i])
    #     print("predict ", data.predict([test_X[i]]))
    #     print("predict_proba ", data.predict_proba([test_X[i]]))
    #     print("test_y ", test_y[i])
    # print("Из ",  len(test_X), " испытаний успешны : ",  good_tests)
    # print("В процентном соотношении:", good_tests / len(test_X))
    print(good_tests / len(test_X))
    return good_tests / len(test_X)



def start_CART(train_len, test_len):

    list = make_list_parts_of_speech(train_len)
    from converter import Converter
    converter = Converter()
    [X, y] = get_X_y(list, converter)

    print("len train list", len(list))
    print("len converter", len(converter.mass))

    model = DecisionTreeClassifier(  )

    # print("clf.fit start")

    model.fit(X, y)

    # joblib.dump(model, 'CART.pkl')  # сохраняем данные
    # print("clf.fit finish ")



    # Проверка на новых данных

    test_list = make_list_parts_of_speech(test_len, True)
    print("len test_list", len(test_list))


    [test_X, test_y] = get_X_y(test_list, converter)

    return check_data(test_X, test_y, model )


# test_result = []
# for i in range(10000, 20000, 3000):
#     for j in range(10000, 20000, 3000):
#         print("start_naive_bayes(i=", i,", j=", j,")")
#         test_result.append([i, j, start_naive_bayes(i, j)])
#         print("------------------------")
# print(test_result)

def check(train_data, test_data):
    from converter import Converter
    converter = Converter()
    [X, y] = get_X_y(train_data, converter)

    # print("len train_data", len(train_data))
    # print("len converter", len(converter.mass))
    # print("len test_data", len(test_data))

    model = DecisionTreeClassifier(  )
    model.fit(X, y)
    [test_X, test_y] = get_X_y(test_data, converter)

    return check_data(test_X, test_y, model)

def checking(): # кросс валидация

    all_words = make_list_parts_of_speech(80000)
    parts = [all_words[:20000], all_words[20000:40000], all_words[40000:60000], all_words[60000:]]
    parts2 = [all_words[:10000], all_words[10000:20000], all_words[20000:30000], all_words[30000:40000], \
             all_words[50000:60000], all_words[60000:70000], all_words[70000:]]
    parts3 = [all_words[:5000], all_words[5000:10000], all_words[10000:15000],  all_words[15000:20000], \
             all_words[20000:25000], all_words[25000:30000]]

    for i in range(len(parts)):
        for j in range(len(parts)):
            if i!=j:
                check(parts[i], parts[j])
    for i in range(len(parts2)):
        for j in range(len(parts2)):
            if i != j:
                check(parts2[i], parts2[j])
    for i in range(len(parts3)):
        for j in range(len(parts3)):
            if i!=j:
                check(parts3[i], parts3[j])
from sklearn.svm import SVC
checking()



def save_new_CART_model(train_len):

    list = make_list_gender(train_len)
    from converter import Converter
    converter = Converter()
    [X, y] = get_X_y(list, converter)

    print("len train list", len(list))
    print("len converter", len(converter.mass))

    model = DecisionTreeClassifier(  )

    # print("clf.fit start")

    model.fit(X, y)

    joblib.dump(model, 'CART.pkl')  # сохраняем данные

def load_CART_model(train_len):
    model = joblib.load('filename.pkl')
    return model
