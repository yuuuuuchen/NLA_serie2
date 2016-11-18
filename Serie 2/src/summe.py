# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

"""
| Die Summe ueber alle Eintraege eines Feldes werden zusammenaddiert auf drei verschiedene Weisen: 
Summation in der Reihenfolge der  Indizes, 
Summation  nach  Groesse  der  Eintraege (beginnend  mit  dem  kleinsten Eintrag), 
paarweise Summation (auch Kaskadensummation). 
Dafuer werden Methoden jeweils speziell fuer den Datentypen numpy.float16 und numpy.float32 definiert
   

.. document private functions
.. automethod:: rand_16
.. automethod:: rand_32
.. automethod:: sum_index16
.. automethod:: sum_index32
.. automethod:: sum_value16
.. automethod:: sum_value32
.. automethod:: sum_kas


"""

import numpy as np



def rand_16(size):
    """
    | Ein Feld der Laenge size mit gleichverteilten Zufallszahlen (vom Typ numpy.float16) 
     und  Werten  im  Intervall [0,10^-5] wird erzeugt
    
    :param size: Die Laenge des Feldes, das erzeugt werden soll (Integer)
    :return ret_val: ein Feld der Laenge size mit gleichverteilten Zufallszahlen (vom Typ numpy.float16) 
     und  Werten  im  Intervall [0,10^-5]

    :rtype: Liste mit Eintraege des Datentyps numpy.float16
    
    """
    
    return [np.float16(np.random.uniform(0,1e-5)) for i in range(size)]

def rand_32(size):
    """
    | Ein Feld der Laenge size mit gleichverteilten Zufallszahlen (vom Typ numpy.float32) 
     und  Werten  im  Intervall [0,10^-5] wird erzeugt
    
    :param size: Die Laenge des Feldes, das erzeugt werden soll (Integer)
    :return ret_val: Summe der Eintraege 
    :rtype: Liste mit Eintraege des Datentyps numpy.float16
    
    """
    return [np.float32(np.random.uniform(0,1e-5)) for i in range(size)]


def sum_index16(values):
    """
    | Die Summe ueber alle Eintraege eines Feldes bekommt 
    man in dieser Methode durch die Summation in der Reihenfolge der Indizes 
    
    :param values: Das Feld, wessen Eintraege summiert werden sollen (Liste mit Eintraege des Datentyps numpy.float16)
    :return ret_val: Summe der Eintraege 
    :rtype: numpy.float16
    """
    sum=np.float16(0)
    for i in range(len(values)):
        sum += values[i]
    return sum

def sum_index32(values):
    """
    | Die Summe ueber alle Eintraege eines Feldes bekommt 
    man in dieser Methode durch die Summation in der Reihenfolge der Indizes 
    
    :param values: Das Feld, wessen Eintraege summiert werden sollen (Liste mit Eintraege des Datentyps numpy.float32)
    :return ret_val: Summe der Eintraege 
    :rtype: numpy.float32
    """
    sum=np.float32(0)
    for i in range(len(values)):
        sum += values[i]
    return sum
    
def sum_value16(values):
    """
    | Die Summe ueber alle Eintraege eines Feldes bekommt 
    man in dieser Methode durch die Summation  nach  Groesse 
    der  Eintraege (beginnend  mit  dem  kleinsten Eintrag)
    
    :param values: Das Feld, wessen Eintraege summiert werden sollen (Liste mit Eintraege des Datentyps numpy.float16)
    :return ret_val: Summe der Eintraege 
    :rtype: numpy.float16
    
    """
    sum=np.float16(0)
    values.sort()
    for i in range(len(values)):
        sum+= values[i]
    return sum

def sum_value32(values):
    """
    | Die Summe ueber alle Eintraege eines Feldes bekommt 
    man in dieser Methode durch die Summation  nach  Groesse 
    der  Eintraege (beginnend  mit  dem  kleinsten Eintrag)
    
    :param values: Das Feld, wessen Eintraege summiert werden sollen (Liste mit Eintraege des Datentyps numpy.float32)
    :return ret_val: Summe der Eintraege 
    :rtype: numpy.float32
    """
    sum=np.float32(0)
    values.sort()
    for i in range(len(values)):
        sum+= values[i]
    return sum

def sum_kas(values):
    """
    | Die Summe ueber alle Eintraege eines Feldes bekommt 
    man in dieser Methode durch die Summation  nach  paarweise Summation (auch Kaskadensummation)
    
    :param values: Das Feld, wessen Eintraege summiert werden sollen (Liste mit Eintraege des Datentyps numpy.float16 (oder 32))
    :return ret_val: Summe der Eintraege 
    :rtype: numpy.float16 (oder 32)
    """
    return values[0] if len(values)<2 else (sum_kas(values[:len(values)/2])+sum_kas(values[len(values)/2:]))
    
    
    
    
    
if __name__ == "__main__":
    print rand_16(2**5)
    print "Hello World"


