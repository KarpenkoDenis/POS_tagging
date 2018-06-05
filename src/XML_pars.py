import xml.dom.minidom as minidom
import numpy as np

def get_data(len=1000):
    my_doc = minidom.parse('./resource/MarkupInfo/MarkupResult.xml')
    my_doc.normalize()

    sentences = my_doc.getElementsByTagName("sentence")
    return sentences[:len]


def get_words_POS(len=1000, random =False):
    my_doc = minidom.parse('./resource/MarkupInfo/MarkupResult.xml')
    my_doc.normalize()
    if random:
        words = my_doc.getElementsByTagName("word")
        words = np.reshape(words)
    else:
        words = my_doc.getElementsByTagName("word")[: len]

    words_with_POS = []
    for word in words:
        dictitem = word.getElementsByTagName("dictitem")[0]
        original = str.lower(word.getAttribute("original"))
        # original = word.getAttribute("original")
        subpart_of_speech = dictitem.getAttribute("subpart_of_speech")
        words_with_POS.append([original, int(subpart_of_speech)])

    return words_with_POS

def get_words_biagram_POS(len=1000, random =False):
    my_doc = minidom.parse('./resource/MarkupInfo/MarkupResult.xml')
    my_doc.normalize()
    sentences = my_doc.getElementsByTagName("sentence")
    words_with_POS_biagrams = []
    for sen in sentences:
        # sen.
        words = sen.getElementsByTagName("word")
        last_word = [str.lower(words[0].getAttribute("original")),
                     int(words[0].getElementsByTagName("dictitem")[0].getAttribute("subpart_of_speech"))]
        for w in words[1:]:
            curr_words = [str.lower(w.getAttribute("original")),
                          int(w.getElementsByTagName("dictitem")[0].getAttribute("subpart_of_speech"))]
            words_with_POS_biagrams.append([last_word, curr_words])
            last_word = curr_words


    # if random:
    #     words = my_doc.getElementsByTagName("word")
    #     words = np.reshape(words)
    # else:
    #     words = my_doc.getElementsByTagName("word")[: len]

    # words_with_POS = []
    # last_word = [words[0]]
    # for word in words[1:]:
    #     dictitem = word.getElementsByTagName("dictitem")[0]
    #     original = str.lower(word.getAttribute("original"))
    #     # original = word.getAttribute("original")
    #     subpart_of_speech = dictitem.getAttribute("subpart_of_speech")
    #     words_with_POS.append([original, int(subpart_of_speech)])
    if random:
        return np.random.shuffle(words_with_POS_biagrams)[:len]
    else:

        return words_with_POS_biagrams[:len]

# print(get_words_POS())

# s = get_data()
# print(len(s))
