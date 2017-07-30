__author__ = 'mpolensek'


# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# ############ Classi in objekti ##############
# Sintakticna definicija. Vsak class, po dogovoru, podeduje od osnovnega Python objekta 'object'
class Zgradba(object):
    # Posebna metoda __init__ se izvede ko iz classa ustvarimo objekt (pri klicu)
    # http://stackoverflow.com/a/8609238
    def __init__(self, ime, st_oken, st_vrat):
        self.ime = ime  # Podatne, zunanj, argumente preipisemo notranjim spremenljivkam
        self.st_oken = st_oken  # Self predstavlja class sam
        self.st_vrat = st_vrat  # in se uporablja za sklicovanje na spremenljivke in metode v samem class-u
        # e.g.:
        self.pokazi_st_vrat()  # Poklicemo class metodo

    def pokazi_st_vrat(self):  # Metoda
        print "Zgradba {} ima vrat.".format(self.ime, self.st_vrat)


# Iz class-a ustvarimo objekt
zg = Zgradba("baraka", 1, 1)  # V "tej vrstici" se izvede __init__ metoda
zg.pokazi_st_vrat()  # Klic metode
print zg.st_oken  # Poglejmo se argument


# Dedovanje objektov
# Namesto da dedujemo od osnovnega objekta, lahko dedujemo od katerega koli drugegea objekta
class Hisa(Zgradba):
    def __init__(self, ime, st_oken, st_vrat):
        # Pri dedovanju se dedovana __init__ metoda ne izvede, zato moramo za to poskrbeti sami
        # in podati dobljene argumente
        super(Hisa, self).__init__(ime, st_oken, st_vrat)

    def pokazi_st_oken(self):  # Metoda
        print "Hisa '{}' ima {} vrat".format(self.ime, self.st_oken)


# Iz class-a ustvarimo objekt
hi = Hisa("topli dom", 6, 2)  # V "tej vrstici" se izvede __init__ metoda
hi.pokazi_st_vrat()  # Metoda podedovana iz class-a Zgradba
hi.pokazi_st_oken()
print hi.ime


# Se eno dedovanje
class Blok(Hisa):
    def __init__(self, ime, st_oken, st_vrat, st_dvigal):
        self.st_dvigal = st_dvigal  # Argument, ki ga dedovani objekt ne pozna definiramo posebej
        super(Blok, self).__init__(ime, st_oken, st_vrat)

    def pokazi_st_dvigal(self):  # Metoda
        print "Blok '{}' ima {} streh".format(self.ime, self.st_dvigal)


bl = Blok("zelena jama", 160, 70, 2)
bl.pokazi_st_dvigal()
bl.pokazi_st_vrat()  # Metoda podedovana iz class-a Zgradba
bl.pokazi_st_oken()  # Metoda podedovana iz class-a Hisa

# ############ Primeri uporabe objektov ##############

# Iz enega class-a naredinmo vec objektov
hisa_1 = Hisa("hisa_1", 1, 2)
hisa_2 = Hisa("hisa_2", 11, 21)
hisa_3 = Hisa("hisa_3", 121, 221)

# In jih dodamo v list
hise = [hisa_1, hisa_2, hisa_3]

# Nato se lahko, kot za kateri koli drug tip podatka, cez njih sprehodimo s for zanko
for vsaka_hisa in hise:
    vsaka_hisa.pokazi_st_oken()
    vsaka_hisa.pokazi_st_vrat()


# Dostikrat objekte uporabimo za prenos podatkov med processi (threadi)
# Naredimo "prazen" class
class PrenosPodatkov:
    pass


# Nato v objekt lahko poimensko shranimo podatke
a = PrenosPodatkov()
a.rezultat_1 = 5
a.error_code = "E000"
a.unit = "dBm"

print a.rezultat_1, a.error_code, a.unit


# Sedaj ko poznate classe in objekte....
# jih ne uporabljati za vsako ceno :)!
# Za definicijo ene spremenljivke NE potrebujemo class-a!
class A(object):
    def __init__(self):
        self.a = 1


a = A()
print a.a
