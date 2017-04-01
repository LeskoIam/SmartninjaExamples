__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


# While zanka
n = 10
while n < 10:
    print n
    n += 1  # n = n + 1

# Enako kot zgoraj while zanka, le da uporabimo for zanko
n = 10
for lojze_slak in range(n):
    print lojze_slak

# Imena spremenljivk niso pomembna!
franc_kosir = 0
while franc_kosir < 10:
    print franc_kosir
    franc_kosir += 1

# Logicne operacije
n = 10
# Ce n ni enak 10
if n != 10:
    print "Ni 10"
elif n != 5:
    pass  # Ne naredi nic, najveckrat uporabljeno kot placeholder
elif n != 10 and n != 5:  # Oba pogoja morata biti izpolnjena da se stavek izvede
    print "Ni 10 in ni 5"
elif not n == 7:  # Negacija z kljucno besedo not
    print "Ni 7"


# Velika zacetnica
ime = "matevz"
print ime
ime = ime.capitalize()
print "Pozdravljen {0}".format(ime)

# Dolzino stringa dobimo s pomocjo funkcije len (length),
# kasneje jo bomo uporabili tudi za iskanje dolzine drugih podatkovnih struktur
print len(ime)

# Cel string v male crke
vnos = "SLO"
print vnos
vnos = vnos.lower()
print vnos

# Kot pravilen pritrdilni vnos tretiramo d, D, j, J, Y
vnos = "D"
vnos = vnos.lower()
if vnos in "dyj":  # Ali je string vnos v stringu "dyj"
    print "Pravilen vnos"

# Poiscemo index kjer se nahaja nas iskani string (substring)
a = "test je dobra stvar"
print a.find("t")  # V dokumentaciji preveri razliko med metodo find in metodo index in kaj pomeni drugi argument obema metodama

# Poiscimo vse indekse kjer se pojavi iskani string sub
main_string = "testni string da po njem iscemo"
sub = "e"
previous = 0
while True:
    this = main_string.find(sub, previous)
    previous = this + 1
    print this
    if this == -1:
        break

# if stavka ki prevrjata isto stvar a je drugi veliko krajsi in lazje razumljiv
a = 5
if a >= 2 and a <= 10:
    print "Med 2 in 10,... vkljucno"

if 2 <= a <= 10:
    print "Med 2 in 10,... vkljucno"
