# This Python file uses the following encoding: utf-8
# program napisal Miro - 26.3.2017 - nalogi 7.2 in 7.3
# program naklju�no izbere �tevilo med 1 in 100, posku�amo ugotoviti �tevilo s pomo�jo komentarja
# ob tem �teje tudi �tevilo poskusov

import os, sys  # dolo�imo encoding = utf-8
import random  # omogo�imo, da ra�unalnik izbere naklju�no �tevilo v danem obsegu

comp_value = random.randint(1, 100)  # ra�unalnik izbere �tevilo med 1 in 100
print "IGRA - UGANI SKRITO �TEVILO !!!!"
print "Poskusi ugotoviti �tevilko med 1 in 100, ki si jo naklju�no izbral ra�unalnik."
stevec_poskusov = 1  # �tevec poskusov damo na 1
while True:
    moja_vrednost = raw_input("Vpi�i �tevilko med 1 in 100 : ")  # vnesemo �tevilo
    if int(moja_vrednost) == comp_value:  # preverimo pravilnost in izpi�emo �e je pogoj izpolnjen
        print "�estitam, pravilno si ugotovil/a, da gre za �tevilo " + str(comp_value) + "."
        print "Uspelo ti je v " + str(stevec_poskusov) + ". poskusu."
        print "**********************************"
        odgovor = raw_input("Si �eli� �e eno igro ? (1=Da/2=Ne)")  # vpra�amo, po novi igri
        if odgovor == "1":  # odgovor DA - pripravimo vse za za�etek nove igre
            comp_value = random.randint(1, 100)
            stevec_poskusov = 1
            print "NOVA IGRA - UGANI SKRITO �TEVILO !!!!"
            print "Poskusi ugotoviti �tevilko med 1 in 100, ki si jo naklju�no izbral ra�unalnik."
        elif odgovor != "1":  # odgovor NE - sko�imo ven iz zanke
            print ""
            print "Hvala za sodelovanje in lep dan �e naprej :-)"
            break
    elif int(moja_vrednost) < comp_value:  # preverimo �e je vne�eno �tevilo manj�e od ra�unalikove izbire
        stevec_poskusov += 1  # pove�amo �tevec poskusov za 1
        print "�tevilo je ve�je !!!"  # igralcu napi�emo komentar, da la�je nadaljuje z igro
    elif int(moja_vrednost) > comp_value:  # preverimo �e je vne�eno �tevilo ve�je od ra�unalikove izbire
        stevec_poskusov += 1  # pove�amo �tevec poskusov za 1
        print "�tevilo je manj�e !!!"  # igralcu napi�emo komentar, da la�je nadaljuje z igro

print ""
print "DODATEK - izpis �umnikov"  # primer izpisa �umnikov
znak = "���"
znak1 = "�ƊЎ"
print znak + " " + znak1
