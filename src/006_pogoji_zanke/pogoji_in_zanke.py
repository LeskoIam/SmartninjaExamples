

import random

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

secret = random.randint(0, 100)
print secret

print "Ugani skrito stevilo med 0 in 100 vkljucno."

for stevec in range(5):
    ans = raw_input("Ugibaj: ")
    ans = int(ans)

    if ans == secret:
        print "Odgovor je pravilen!"
        break
    elif ans > secret:
        print "Stevilka je previsoka, poizkusi znova"
    elif ans < secret:
        print "Stevilka je prenizka, poizkusi znova"
    # else:
    #     print "Napacen odgovor, poskusi ponovno, imas se " + str(4 - stevec) + " poizkusov"


print "Napacen odgovor"