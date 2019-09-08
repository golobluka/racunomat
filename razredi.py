
import random, math, time


STEVILO_KROGOV = 4
DATOTEKA_LESTVICE = 'lestvica\lestvica.txt'
DOLZINA_LESTVICE = 10

### Zbirka moznih nalog:

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
def koren(x):
    return x ** (1/2)
def sinus_hiperbolikus(x):
    return math.sinh(x)


seznam_formul = [[sinus,'sin', [x/2 for x in range(-8, 8)]], [ekspo, 'e^', [x for x in range(1, 6)]], [arctan, 'arctan' , [-6, -5, -3, -1, 1, 3, 5, 6]], [fakulteta, 'fakulteta', [ 5, 6, 7, 8]], [naravni_logaritem, 'ln', [x/10 for x in range(0, 400)]], [eksponent_2, '2^', [x/2 for x in range(9, 18)]], [koren, 'koren', [x for x in range(2, 19)]], [sinus_hiperbolikus, 'sinh', [x/5 for x in range(-15, 14)]]]

### Razredi:


class Racun:
    def __init__(self, seznam_formul):
        self.formule = seznam_formul
    
    def izberi_racun(self):
        formula = random.choice(range(len(self.formule)))
        
        self.x = random.choice(self.formule[formula][2])
        if self.x == int(self.x):
            self.x = int(self.x)

        self.zapis = str(self.formule[formula][1])
        self.racun = self.formule[formula][0]
        self.resitev = round(self.racun(self.x),3)

        self.cas = round(time.time(), 1)

        return round(self.resitev, 2)
    
    def je_stevilo(self, odgovor):
        return odgovor.replace('.', '', 1 ).replace('-', '', 1).isdigit()
        
    def relativna_napaka(self, priblizek):
        if self.resitev != 0:
            return round((self.resitev - priblizek) * 100 / self.resitev, 2)
        else:
            return 0



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
        self.igre[id_igre] = [igra, 0, 1]
        return id_igre
    
    def dodaj_tocke(self, id_igre, tocke):
        self.igre[id_igre][1] = round(tocke, 0) + self.igre[id_igre][1]
        return self.igre[id_igre][1]
    
    def konec_igre(self, id_igre):
        if self.igre[id_igre][2] >= STEVILO_KROGOV:
            return True
        else:
            return False

    def dodaj_krog(self, id_igre):
        self.igre[id_igre][2] = self.igre[id_igre][2] + 1

    def preveri_izkopicek(self, id_igre):
        with open(DATOTEKA_LESTVICE, 'r',encoding='utf-8') as dat:
            vrstice = dat.readlines()
            

            for mesto, vrstica in enumerate(vrstice):
                podatki  = vrstica[:-1].split(',', 2)
    
                if int(podatki[1]) >= self.igre[id_igre][1]:
                    pass
                else:
                    return (mesto + 1, vrstice)

            if len(vrstice) < DOLZINA_LESTVICE:
                return (len(vrstice) + 1, vrstice)
            return (False, vrstice)
    
    def spremeni_lestvico(self, mesto, ime, tocke ):
        with open(DATOTEKA_LESTVICE , 'r', encoding = 'utf-8') as dat:
            vrstice = dat.readlines()
        vrstice = vrstice[:mesto - 1] + [ime + ',' + str(tocke) + '\n'] + vrstice[mesto - 1:]

        if len(vrstice) > DOLZINA_LESTVICE:
            vrstice = vrstice[:DOLZINA_LESTVICE]
        text = ''.join(vrstice)

        with open(DATOTEKA_LESTVICE, 'w', encoding='utf-8' ) as dat:
            dat.write(text)

    def preberi_lestvico(self):
        seznam_rezultatov = []
        with open(DATOTEKA_LESTVICE, 'r', encoding='utf-8' ) as dot:     
            for vrstica in dot:
                seznam_rezultatov.append(vrstica[:-1].split(','))
            return seznam_rezultatov
                
        

############################################################
# Tu je funkcija za izračunavanje točk
############################################################


def tockar(odgovor, resitev, cas=10):
    absolutna = absolutna_napaka(odgovor, resitev)
    if resitev == 0:
        tocke = 100 * (odgovor + 1) ** (-4)
    else:
        relativna = relativna_napaka(odgovor, resitev)
        prilagojeno = (resitev + 1) ** (-1) + resitev
        tocke = 100 * (abs(absolutna/(prilagojeno)) + 1) ** (-3) + (100 *   (1 - 1 ** (-3)))
    
    koncne_tocke = round(tocke - 2 * math.log(cas + 1))
    if koncne_tocke < 0:
        return 0
    else:
        return koncne_tocke

def relativna_napaka(odgovor, resitev):
    return (odgovor - resitev)/ resitev
   
def izracun_odklona(odgovor, resitev):
    if resitev == 0:
        return 1
    return (resitev)/odgovor

def absolutna_napaka(odgovor, resitev):
    return odgovor - resitev


    
    
    
    
    
    


