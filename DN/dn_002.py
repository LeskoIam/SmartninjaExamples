# -*- coding: utf-8 -*-
# python 2
#  program napisal Miro - 21.4.2017 - naloga 10.3 LOTO
# program naključno izbere LOTO števila (6 + 1) število med 1 in 39



import random   # omogočimo, da računalnik izbere naključno število v danem obsegu

def preveri_loto_stevilo():
    print ""
    print "IGRA - LOTO"
    print "Računalnik - žrebanje LOTO številk (7+1)."
    print ""
    lista_loto_stevil = []
    lista_loto_stevil_dodatna = []
    while True:
        loto_stevilo = random.randint(1, 39)  # računalnik izbere število med 1 in 39
        print lista_loto_stevil
        if loto_stevilo not in lista_loto_stevil:
            lista_loto_stevil.append(loto_stevilo)
            print "dodajam"


        if len(lista_loto_stevil) == 7:
            while True:
                loto_stevilo_dodatno = random.randint(1, 39)  # računalnik izbere dodatno število med 1 in 39
                if loto_stevilo_dodatno not in lista_loto_stevil:
                    lista_loto_stevil_dodatna.append(loto_stevilo_dodatno)
                    break
                else:
                    continue
        if len(lista_loto_stevil_dodatna) == 1:
            break


if __name__ == "__main__":
    preveri_loto_stevilo()