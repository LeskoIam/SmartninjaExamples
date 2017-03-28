__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# Spremenljivke
a = 3
b = 2 + a  # definiramo se eno spremenljivko, njena vrednost je 2 + 3

# Prikazemo vrednost na zaslon
print a
print b

# Racunamo s spremenljivkami, enako kot da bi operirali s stevilkami
print a + b + b

# Escape karakter \. Uporabimo kadar zelimo uporbiti nek poseben znak ali vsiliti dobesedno pisanje znaka,
# ki ima tudi pomen v python sintaxi
# Tukaj se vrednost a prepise z novo vrednostjo, ki je sedaj tipa string
a = "it'\"s"
print a

# Bool oz. logicne vrednosti
a = True   # 1, Da, ...
b = False  # 0, Ne, ...

print a
print b

# Kako od uporabnika vzeti vnos. Kar je uporabnik vnesel se shrani v spremenljivko "starost"
starost = raw_input("Vnesi svojo starost: ")

# Ker raw_input vrne string (neglede na to ali je uporabnik vnesel recimo stevilko),
#  lahko sedaj stringe lepimo z znakom +
print "Dragi uporabnik, tvoja starost je " + starost + " let."

# Se ena moznost je uporaba "format" metode na samem stringu
print "Dragi uporabnik star si {0} let {1}. {0} {1}".format(starost, 3)


###############################################
###############################################
# Flow control (pogojni stavki)

# Glede na ime uporabnika pokazemo odziv
# Dvojni enacaj!!

name = "Matevz"

if name == "Matevz":
    print "Pozdravljen Matevz"
elif name == "Tina":
    print "Pozdravljena Tina"
elif name == "Matevz":
    print "matevz 2"
else:
    print "nic ni res"

print name

# Uporaba bool vrednosti v pogojnih stavkih.
paid = False
if paid:
    print "Placano"
else:
    print "Ni placano"


###############################################
###############################################
# While zanka

n = 0

# Toliko casa kolikor je pogoj izpolnjen bo zanka tekla
while n <= 10:
    print n
    n += 1  # n = n + 1
print "Konec kode"


# Se en primer while zanke
skrito_stevilo = 5
pogoj = True
while pogoj:
    n = int(raw_input("stevilka: "))  # s funkcijo int spremenimo string v integer (ce je to mogoce, drugace dobimo error)
    if n == skrito_stevilo:
        pogoj = False


# Enako kot prejsnja, le da za izhod iz zanke uporabimo break
skrito_stevilo = 5
while True:
    n = int(raw_input("stevilka: "))  # s funkcijo int spremenimo string v integer (ce je to mogoce, drugace dobimo error)
    if n == skrito_stevilo:
        break

