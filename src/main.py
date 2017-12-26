import numpy as np
from read_groups import make_list_mans_and_womans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import  grid_search

from sklearn.svm import SVC




vectorizer = TfidfVectorizer()

corpus = [
    "dfgdfg",
    "ac",
]

list = make_list_mans_and_womans(10)

new_list =[]
large_list =[]
from converter import Converter

converter = Converter()
# new_list = list[:10] + list[-10:]

# list = list[:50000] + list[-50000:]  #слишком много в листе, уменьшим
np.random.shuffle(list)
# print("list", list)


for m in list:
    large_list = large_list + []
    large_list = large_list + [[#converter.convert(m[0]),
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
# print("y ", y)
print("len y ", len(y ))
# print("list[:10]", list[:10])
# X = vectorizer.fit(large_list)
# print("X " , X)
print("len X", len(X))
print("len converter", len(converter.mass))
# X = vectorizer.fit_transform(large_list)






clf = SVC( cache_size= 50000 )

# problem = clf.fit(X, y)  # создаем задачу
print("clf.fit start")

problem = clf.fit(X, y)  # создаем задачу


print("clf.fit finish ")
def gender(word):
    new_word = [word, word[-2:], word[-3:]]
    nX = [[ # converter.convert(new_word[0]),
            converter.convert(new_word[1]),
            converter.convert(new_word[2])]]
    print(word, "- ", "муж" if clf.predict(nX) == 1 else "жен")
    print("Номера: ", nX[0][0], ", ", nX[0][1])
    print("---------------------------")
gender("мама")
gender("папа")
gender("полрубля")
gender("владыками")
gender("электропередачи")
gender("зануда")
gender("зануда")
gender("зануда")
gender("зануда")
gender("зануда")
gender("боец")
gender("служащий")
gender("вековой")
gender("ждущий")
gender("налог")
gender("терзаемый")
gender("гнетущий")
gender("лвоышдамый")
gender("авытнашол")
gender("вавшдыпашв")
gender("пришла")
gender("живая")
gender("любимая")
gender("летняя")
gender("монтажнице")
gender("миллионерша")
gender("миллионерша")
