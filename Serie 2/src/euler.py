# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
| Die Reihe Z_n = (1+1/n)^n, welche bekanntemassen gegen der Eulersche Zahl konvergiert, wird mit dieser Klasse
berechnet. Der Wert von n und die Mantisselaenge der Zahlen, mit dem die Methoden rechnen, koennen von der Benutzer
selbst bestimmt werden.

.. document private functions
.. automethod:: euler
.. automethod:: plotcontour
.. automethod:: plotnormal

"""
import decimal

import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def euler(exp, prec):
    """
    | Die zu e konvergierende Reihe Z_n = (1+1/n)^n wird bezueglich
    einer bestimmten n und Mantissenlaenge bestimmt

    :param exp: exp definiert die Groesse der Variable n in der Reihe Z_n, es gilt: "n = 3 + 3*exp" (Integer)
    :param prec: Die Laenge der Mantisse (Integer)
    :return ret_val: (1 + 1/(3+3*exp))^(3+3*exp))    bzgl. Mantisselaenge prec
    :rtype: Decimal

    """
    decimal.getcontext().prec = prec
    k = decimal.Decimal(3 + 3 * exp)
    n = 2 ** decimal.Decimal(k)

    z = 1 / n
    z += 1
    return z ** n


def plotcontour(exp, prec):
    """
    | Der relative Fehler zwischen dem Ergebnis der Methode euler mit den Variablen exp und prec und dem
    genauen Wert fuer e wird in Form eines Konturplotes dargestellt. In den X- Und Y-Achse stehen jeweils
    die Werte von exp und prec. Die Grosse des relativen Fehlers erkennt man anhand der Farbskala.

	 :param exp: exp definiert die Groesse der Variable n in der Reihe Z_n, es gilt: "n = 3 + 3*exp" (Integer)
    :param prec: Die Laenge der Mantisse (Integer)

    """

    a = exp
    b = prec

    # a, b = (300,400)
    X = np.arange(0, a)
    Y = np.arange(0, b)

    Z = np.ndarray(shape=(b, a))

    for x in range(0, a):
        for y in range(0, b):
            # if (abs(euler(x+1,y+1) - decimal.Decimal(2.71828182845904523536028747135266249775724709369995)) < 0.001):
            #   Z[x][y] = 100
            # else:
            #   Z[x][y] = 1
            Z[y][x] = abs(euler(x + 1, y + 1) - decimal.Decimal(
                2.71828182845904523536028747135266249775724709369995)) / decimal.Decimal(
                2.71828182845904523536028747135266249775724709369995)

    plt.figure(figsize=(15, 15))
    CS = plt.contour(X, Y, Z)
    im = plt.imshow(Z, origin='lower')
    plt.clabel(CS, inline=1, fontsize=10)
    CB = plt.colorbar(CS)
    CBI = plt.colorbar(im, orientation='horizontal', shrink=0.8)

    plt.title('Eulersche Zahl')

    plt.show()


def plotnormal(exp, prec):
    """
    | Der relative Fehler zwischen dem Ergebnis der Methode euler mit den Variablen exp und prec und dem
    genauen Wert fuer e wird in Form einer Grafik dargestellt. In den X- Und Y-Achse stehen jeweils
    die Werte von exp und der davon abhaengige relative Fehler.

    :param exp: exp definiert die Groesse der Variable n in der Reihe Z_n, es gilt: "n = 3 + 3*exp" (Integer)

    """

    X = np.arange(0, exp)
    plt.figure(figsize=(15, 15))

    Y = np.ndarray((exp,))

    for x in range(0, exp):
        Y[x] = abs(euler(x + 1, prec) - decimal.Decimal(
            2.71828182845904523536028747135266249775724709369995)) / decimal.Decimal(
            2.71828182845904523536028747135266249775724709369995)
        # Y[x] = euler (x,prec)

    print X
    print Y

    plt.plot(X, Y)
    plt.show()


# def euler_plot(value):
#   dif = value - 2.7182818284 5904523536 0287471352 6624977572 4709369995 9574966967 6277240766 3035354759 4571382178 5251664274
if __name__ == "__main__":
    # for i in range(16):
    #   for p in range(4):
    #        print "j={}, prec={}: {}".format(i+1,(p+1)*10, euler(i+1,(p+1)*10))
    #   print ""

    print ("!!!!!!!!!!!")
    print euler(7, 8)
    print euler(60, 10)
    print euler(39, 50)
    for i in range(52, 68, 1):
        print
        for p in range(52, 68, 1):
            # print decimal.Decimal(2.71828182845904523536028747135266249775724709369995)
            # if (abs(euler(i+1,p+1) - decimal.Decimal(2.71828182845904523536028747135266249775724709369995)) < 0.001):
            #   hs=100
            # else:
            #   hs = 0
            print "j={}, prec={}: {}".format(i + 1, p + 1, euler(i + 1, p + 1))


            # plotnormal()