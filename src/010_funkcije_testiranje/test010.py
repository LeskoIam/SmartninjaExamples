__author__ = 'mpolensek'


# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# ######## Funkcije ###########
# Funkcijo definira kljucna beseda 'def' za njo sledi ime funkcije
# Po dogovoro se imena finkcij pisejo z malimi crkami, beseda pa so locene s podcrtajem
def ime_funkcije():
    print "moja prva funkcija"

# Funkcijo poklicemo po njenem imenu z dodanimi oklepaji (v oklepaje pisemo argumente, v tem primeru argumentov ni)
ime_funkcije()


# Funkcija lahko sprejme argument/e - spremeljivke, ki se dostopne le funkciji (zunaj nje niso 'vidne')
def druga_funkcija(ime):
    print "moje ime je: {}".format(ime)

# Pri klicu funkcije ji podamo argument
moje_ime = "Matevz"
druga_funkcija(moje_ime)


# Ce definiramo vec funkcij z istim imenom, tista, ki je definirana kasneje prepise tisto, definirano pred njo
def druga_funkcija(ime):
    print "Haha, zbrisal si originalno funkcijo! Tvoj input je: {}".format(ime)

druga_funkcija(moje_ime)


# Iz funkcije lahko vracamo vrednosti, za to uporabimo kljucno besedo 'return'. V tem primeru se vrednost, ki jo funkcije vrne ne izpise
# ampak se 'shrani v spomin'
# Dobro je vedeti, da tudi ce funkcija ne vraca nobene vrednosti (nima return), se iz nje vrne None
# (poseben tip podatka ki predstavlja 'nic' (Null, NA, N/A))
def vrni_vrednost(a):
    return a + 1

# Da kaj vidimo na zaslonu potrebujemo print, saj funkcija sama ne pise na zaslom ampak samo vraca vrednost
print vrni_vrednost(5)


# Funkcija lahko sprejme vec argumentov
def vec_inputov(a, b, c):
    return a + b + c


# ########### Naprednejsa definicija funkcij ###########
# Argument, ki ze ima definirano privzeto vrednost
def zakomplicirana_funkcija(test_input, loops=1):
    for x in range(loops):
        print test_input


# Arguments - pri klicu funkcije podamo poljubno stevilo argumentov.
# Njihove vrednosti, se v enakem zaporedju, kot so bile podane
# shranijo v list 'args'
def se_bolj_kompleksen_input(*args):
    print type(args)  # Prikazemo tip spremenljivke
    print args
    for x in args:
        print x

# Pa jo poklicimo s poljubnim stevilom argumentov
se_bolj_kompleksen_input(1, 2, 3, 4, 5, 6, 7)


# Primer uporabe args.
def zdruzi_str(*args):
    return " ".join(args)

zdruzi_str()


# Key Word Arguments - podobno kot pri args, le da se vrednosti shranijo v dictionary.
# Tudi argumente moramo podajati poimensko!
def zdruzi_str_2(**kwargs):
    print kwargs

zdruzi_str_2(prvi="test1", drugi="test3", kljuc=34)
