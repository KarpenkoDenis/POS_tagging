


class Converter:
    mass =[]

    def convert(self, word):
        for w in self.mass:
            if w == word:
                return self.mass.index(w)

        self.mass = self.mass+[word]
        return self.mass.index(word)


# l = Converter()
# l.convert("qwe")
# print("Test: ", l.convert("djklsf"))
# print("Test: ", l.convert("djklsf"))
# print("Test: ", l.convert("hgf"))
# print("Test: ", l.convert("df"))
# print("Test: ", l.convert("dsf"))
# print("Test: ", l.convert("djklsf"))
# print("Test: ", l.convert("df"))
