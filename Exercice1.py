""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. """

import numpy as np


def multipleDeTroisEtCinq(limite, *facteurs):
    """
    Brief : Fonction qui permet de trouver les nombres multiples sous une limite avec une itération

    :param limite : limite des multiples
    :param facteurs : nombre de multiples désirées

    :return multiples : une liste contenant tous les multiples
    """
    multiples = list()
    liste_de_facteur = list(facteurs)

    for nombre in range(limite):
        for fact in liste_de_facteur:
            if nombre % fact == 0:
                multiples.append(nombre)
                break
    return multiples


def multipleAlternative(limite, *facteurs):
    """
    Brief : Fonction qui permet de trouver les nombres multiples sous un limite d'une meilleure façon
    :param limite: limite des multiples
    :param facteurs: nombre de multiples désirées
    :return: une liste contenant tous les multiples
    """
    data = np.array(list(range(limite)))
    liste_de_facteur = list(facteurs)

    multiples = list()
    for fact in liste_de_facteur:
        # mult = list(np.where(data % fact == 0))
        # multiples = list(set(multiples, mult))
        #
        # multiples = list(set((np.where(data % fact == 0))))

    return np.unique(multiples)


element_multiple = multipleAlternative(1000, 3, 5)
print(element_multiple)
print(np.where(element_multiple == 0))



# print(sum(multipleDeTroisEtCinq(1000, 3, 6)))
