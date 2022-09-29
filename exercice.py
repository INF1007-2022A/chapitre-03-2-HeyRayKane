#!/usr/bin/env python
import math
def dissipated_power(voltage, resistance):
    # TODO: Calculer la puissance dissipée par la résistance.
    puissance = (voltage ** 2)/resistance
    return puissance

def orthogonal(v1, v2): #v1 et v2 sont des vecteurs
    # TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
    #v1[0] Pour accéder au X.
    #v1[1] Pour accéder au Y.
    produit_scalaire = (v1[0]*v2[0])+(v1[1]*v2[1])
    return (produit_scalaire == 0) #Retourne vrai ou faux

def average(values):
    # TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
    nombre_element = 0
    somme=0
    for v in values:
        if v>=0:
            nombre_element+=1
            somme+=v
    moyenne = somme/nombre_element
    return moyenne # La variable v contient une valeur de la liste.

def bills(value):
    # TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
    twenties, tens, fives, twos, ones = 0,0,0,0,0
    while value != 0:
        if value >= 20:
            twenties = value//20
            value -= 20*twenties #on aurait pu utiliser aussi l'opérateur %
        elif value >= 10:
            tens = value//10
            value -= 10*tens
        elif value >= 5:
            fives = value//5
            value -= 5*fives
        elif value >= 2:
            twos = value//2
            value -= 2*twos
        elif value >= 1:
            ones = value

    return (twenties, tens, fives, twos, ones);

def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    abs_value = abs(value)
    x = abs_value % base
    abs_value = abs_value - x
    result = digit_letters[x]
    while abs_value >= base:
        abs_value //= base
        w = abs_value % base
        result = digit_letters[w] + result
    if value < 0:
        # TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        result = "-" + result
    return result

if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))

""" Brouillon:
x = value % base  # x=2
y = value - x  # y=9
new_value = digits_letters[x]  # new_value = "2"
while y >= base:
    y = y // base  # y=3
    w = y % base  # w=0
    if w < base:
        new_value = digits_letters[w] + new_value  # new_value = "02"
print(new_value)"""