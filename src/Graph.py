#!/usr/bin/python3.1
from LettersGenerator import *

class Graph:
    def __init__(self, language):
        self.graph = self.makeGraphe()
        self.lettersList = LettersGenerator(language).lettersList #['P','A','T','R','U','I','P','J','O','E','T','E','H','U','N','Y','S','R','S','E','X','V','E','A']#LettersGenerator(language).letters_liste

    def makeGraphe(self):
        """ graph représenté par ses sommets et la liste de ses voisins
        associés"""
        graph = {
            0:[1,2,5,6,7,8],
            1:[0,2,3,6,7,8],
            2:[0,1,3,4,6,7,8,9,10],
            3:[1,2,4,8,9,10],
            4:[2,3,8,9,10,11],
            5:[0,6,7,12,13,14],
            6:[0,1,2,5,7,8,12,13,14],
            7:[0,1,2,5,6,8,9,12,13,14,15,16],
            8:[0,1,2,3,4,6,7,9,10,14,15,16],
            9:[2,3,4,7,8,10,11,14,15,16,17,18],
            10:[2,3,4,8,9,11,16,17,18],
            11:[4,9,10,16,17,18],
            12:[5,6,7,13,14,19],
            13:[5,6,7,12,14,15,19,20,21],
            14:[5,6,7,8,9,12,13,15,16,19,20,21],
            15:[7,8,9,13,14,16,17,19,20,21,22,23],
            16:[7,8,9,10,11,14,15,17,18,21,22,23],
            17:[9,10,11,15,16,18,21,22,23],
            18:[9,10,11,16,17,23],
            19:[12,13,14,15,20,21],
            20:[13,14,15,19,21,22],
            21:[13,14,15,16,17,19,20,22,23],
            22:[15,16,17,20,21,23],
            23:[15,16,17,18,21,22]
            }
        return graph

    def isNeighbour(self, case1, case2):
        """ fonction qui dit si case2 est un voisin de case1 """
        return case2 in self.graph[case1]

    def print_graph(self):
        [print(i," --> ",e) for i,e in self.graph.items()]

    def isInGraph(self, letter):
        """ fonction qui retourne la liste des position de cette letter dans le graph"""
        L = []
        for c,v in self.graph.items():
            if self.lettersList[c].lower()==letter.lower():
                L.append(c)
        return L
