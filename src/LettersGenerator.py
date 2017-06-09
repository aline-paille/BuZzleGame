#!/usr/bin/python3.1
from random import *
from Variables import *

# TODO : variable pour choisir si on prend l'alpha Francais ou anglais 
VAR_LANGAGE = "Anglais"

class LettersGenerator:
    def __init__(self, language):
        self.lettersList = self.lettersHexagon(language)

    def couple_probability(self, file):
        """ fonction qui lit le fichier et retourne le couple dans lequel on a mit probas = valeur correspondant aux sommes des pourcentages associés a chaque lettre et alpha = lettre de l'alphabet """
        probas = []
        alpha = []
        fic = open(file, 'r')
        line = fic.readlines()
        for i,e in enumerate(line) :
            l1 = line[i].split()
            probas.append(int(l1[1])) 
            alpha.append(l1[0])
        fic.close()
        return (probas, alpha)

    def lettersHexagon(self, language):
        """fonction qui  créer la liste de lettres utiles pour l'hexagone en majuscules """
        if language == FRENCH_LANGUAGE:
            file = "../probas_Alphabets/PourcentAlphaF.txt"
        elif language == ENGLISH_LANGUAGE:
            file = "../probas_Alphabets/PourcentAlphaA.txt"
        else: 
            print("error : bad language")
            return
        res = self.couple_probability(file)
        list1 = res[0]
        list2 = res[1]
        return [self.letter_alea(list1, list2).upper() for e in range(0,24)]

    def letter_alea(self, probas, alphabet):
        """ fonction qui choisit une lettre aleatoirement parmi un alphabet et en fonction de la proba de chaque lettre """
        val = randint(0,probas[len(probas)-1]-1)
        for i in range(0, len(probas)-1):
            if val<=probas[i] and val<probas[i+1]:
                return alphabet[i]
        return "error"
