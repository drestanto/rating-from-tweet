class Rating(object):
    def __init__(self, kata_negatif=None, kata_positif=None):
        self.kata_negatif = []
        self.kata_positif = []

    def load_kata_negatif(self):
        file = open("../data/kata-negatif.txt","r")
        self.kata_negatif = file.read().splitlines()

    def load_kata_positif(self):
        file = open("../data/kata-positif.txt","r")
        self.kata_positif = file.read().splitlines()

r = Rating()
r.load_kata_negatif()
r.load_kata_positif()
print(r.kata_negatif[100])
print(r.kata_positif[100])