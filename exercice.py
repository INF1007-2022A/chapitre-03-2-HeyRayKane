#!/usr/bin/env python


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
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
