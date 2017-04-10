__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

# ##### List ###########
# https://docs.python.org/2/tutorial/datastructures.html
# Syntax
lista = ["to je string", 1, 2.4, [1, 2, 3]]  # V en list lahko shranimo mesane time podatkov. Tudi drug list.
print lista

# List, tako kot string, lahko indeksiramo, iz list-u izbiramo elemente po indeksu
print "Prvi element lista je {}".format(lista[0])
# Neglede na dolzino lista, lahko zadji element izberemo z indexom -1
print "Zadnji element lista je", lista[-1]
# Izbiranje gnezdenega lista
# Najprej izberemo zadnji element 'lista' nato se drigi element podlista
print lista[-1][1]

# Elementu lista lahko priredimo novo vrednost
lista[0] = 6
print lista

# In tudi njegovemu gnezdenemu listu
lista[-1][2] = "test"
print lista

# Dolzino lista izvemo z built-in funkcijo len()
print len(lista)


# ##### TODO_program #########
task_list = []  # Prazen list v katerega bomo kasneje dodajali elemente
task_done = []
while "pigs" != "fly":  # Neskoncna zanka :)
    task = raw_input("Enter new task: ")
    print "Your new task is {new_task}".format(new_task=task)
    this_task_done = raw_input("Is this task done? [y/n]: ")  # Predvidevamo pravilen vnos

    # Z metodo append dodamo en elemt na konec lista
    task_list.append(task)

    if this_task_done == "y":
        task_done.append(True)
    else:
        task_done.append(False)

    # Inline pogojni stavek. Enako kot zgoraj if/else le da krajse
    # task_done.append(True if this_task_done == "y" else False)

    add_another = raw_input("Would you like to add another task [y/n]: ")  # Predvidevamo pravilen vnos
    if add_another == "n":
        break

# Z while zanko prikazimo vnesene taske
i = 0
while i < len(task_list):
    print task_list[i]
    i += 1  # i = i + 1


# Odkomentiraj spodnjo vrstico in zakomentiraj vnosno while zanko zgoraj, ce noces vsakic vnasati taskov
# task_list = ["t1", "t2", "t3", "t4"]

# Uporaba funkcije ENUMERATE da dobimo poleg elemnta se njegov index
# https://docs.python.org/2/library/functions.html#enumerate
print task_list
for i, task in enumerate(task_list):
    print i, task

# ZIP - s for zanko se sprehodimo cez dva (ali vec) listov hkrati.
# Pozor! Ce listi, ki jih 'zipamo' niso enakih dolzin na koncu dobimo stevilo elementov krajsega!
# https://docs.python.org/2/library/functions.html#zip
print task_list
for t, td in zip(task_list, task_done):
    print t, td


# ##### Dictionary ##########
# https://docs.python.org/2/tutorial/datastructures.html#dictionaries

# Syntax
d = {"kljuc": "vrednost",
     1: 5,
     2: "test"}
print d

# Indexiramo podobno kot list, le da ne uporabimo indexa ampak vrednost kljuca
print d["kljuc"]
print d[1]

# Dodajanje elementov v dict
d["kljuc2"] = 666
print d

# Stevilo elementov v dictionary-ju
print len(d)

# ##### TODO_program z uporabo dictionary-ja ##########
tasks = {}  # Definiramo prazen dictionary
while "pigs" != "fly":
    task = raw_input("Enter new task: ")
    print "Your new task is {new_task}".format(new_task=task)

    this_task_done = raw_input("Is this task done? [y/n]: ")

    # Dodamo nov vnos v dictionary tasks.
    # Kljucu 'task' priredimo vrednost True/False
    tasks[task] = True if this_task_done == "y" else False

    add_another = raw_input("Would you like to add another task [y/n]: ")

    if add_another == "n":
        break

print tasks

print "Narejeni taski"
# https://docs.python.org/2/tutorial/datastructures.html#looping-techniques
for key, value in tasks.iteritems():
    if value:  # if value == True
        print key

print "Nedokoncani taski"
# https://docs.python.org/2/tutorial/datastructures.html#looping-techniques
for key, value in tasks.iteritems():
    if not value:  # if value == True
        print key

# Ce moramo dictionary ustvariti na roke je, zaradi berljivosti,
# dobro da ga lepse formatiramo. Recimo:
a = {1: 23323,
     2: 4343,
     3: 4343}


# ######### Shranjevanje v file #####

# Star in "nevaren" nacin. Ce pozabimo .close() ali nam koda kresira pa imamo file odprt,
# nismo sigurni da so se v njega podatki res zapisali
f = open("test.txt", "w")
f.write("test string")
f.close()

# To je 'pravilen' nacin pisanja v file. Uporabimo context manager with
# Odpri file z imenom test1.txt v Write nacino in njegov objekt shrani v spremenljivko f
with open("test1.txt", "w") as f:
    f.write("test string\n")
    f.write("nova vrstica\n")
    f.write("pred mano ni nove vrstice")
