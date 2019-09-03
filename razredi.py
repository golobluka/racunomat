
import random, math, time


def sinus(x):
    return math.sin(x)
def ekspo(x):
    return math.exp(x)
def arctan(x):
    return math.atan(x)
def fakulteta(x):
    return math.factorial(x)
def naravni_logaritem(x):
    return math.log(x)
def eksponent_2(x):
    return 2 ** x

seznam_formul = [[sinus,'sin', [1, 2, 3, 4]], [ekspo, 'e^', [2, 3, 4, 5]], [arctan, 'arctan' , [-6, -5, -3, -1, 1, 3, 5, 6]], [fakulteta, 'fakulteta', [ 7, 8, 9, 10, 11, 12, 13, 14, 16]], [naravni_logaritem, 'ln', [0.1, 0.25, 0.6, 2, 5, 10, 15, 20, 25, 30]], [eksponent_2, '2^', [5, 6, 7, 8, 9]]]

class Racun:
    def __init__(self, seznam_formul):
        self.formule = seznam_formul
    
    def izberi_racun(self):
        formula = random.choice(range(len(self.formule)))
        
        self.x = random.choice(self.formule[formula][2])
        self.zapis = str(self.formule[formula][1])
        self.racun = self.formule[formula][0]
        self.resitev = round(self.racun(self.x),3)

        self.cas = round(time.time(), 1)

        return round(self.resitev, 2)
        
    def relativna_napaka(self, priblizek):
        return round((self.resitev - priblizek) * 100 / self.resitev, 2)



class Racunomat:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = Racun(seznam_formul)
        self.igre[id_igre] = (igra, 0)
        return id_igre
    
    def dodaj_tocke(self):
        pass













