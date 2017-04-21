# Iz modula matematika (ime datoteke kjer je definirana funkcija sestej) uvozi funkcijo sestej
from matematika import sestej

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


def test_sestevanja():
    # Assert (predpostavi) - preveri ce je sledeci logicni izraz pravilen, ce izraz ni pravilen
    # se program ustavi in javi napako (AssertionError), drugace tece naprej neprekinjeno
    assert sestej(1, 2) == 4
    print "Test uspesen"

test_sestevanja()
