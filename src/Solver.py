#!/usr/bin/python3.1
from Graph import *
from LettersGenerator import *
from Dictionary import *

class Solver:
    """ classe qui résoud le jeu : 
    self.graph = le graph qui represente toutes les cases du plateau,
    self.d = objet Dictionnary,
    self.dico = l'arbre dictionnaire
    self.lettersList = la liste des letters du plateau,
    self.solution = la liste des solutions du solver"""

    def __init__(self, graphParent, dicoParent, lettersList, solver):
        self.g = graphParent
        self.graph = self.g.graph
        self.d = dicoParent
        self.dico = dicoParent.trie
        self.lettersList = lettersList
        self.solver = solver
        self.solution = self.setSolverType(solver)
        print(self.wordsCounter(self.solution), "words found.")

    def setSolverType(self, solver):
        if solver == 0:
            return self.solver_init()
        elif self.solver == 1:
            return self.solver2_init()
        else :
            print("xxx","solver execution error.")
        
    def solver_init(self):
        wordsFound = []
        colors = ["white" for e in self.lettersList]
        positions = [(i,e) for i,e in enumerate(self.lettersList)]
        for e in positions:
            self.solver_rec([], e, wordsFound, colors)
        res = set(wordsFound)
        res = self.decreasingList(res)
        return res

    def solver_rec(self, parcours, position, ensWordsFound, colors):
        """ ensMotTrouves = ensemble des words trouves, selections = une liste de selection de letters, colors nous permet de savoir si l'etat à déja ete visité ou non"""
        wordPotentiel = self.getWord(parcours + [position])
        if self.d.isInTree( wordPotentiel) :
            ensWordsFound.append(wordPotentiel)
        if not self.d.prefixIsInTree(wordPotentiel):
            return
        else :
            numCase = position[0]
            newParcours = list(parcours)
            newParcours.append((numCase, self.lettersList[numCase]))
            newColors = list(colors)
            newColors[numCase] = "black"
            for neighbour in self.graph[numCase]:
                if newColors[neighbour]=="white":
                    newPosition = (neighbour, self.lettersList[neighbour]);
                    self.solver_rec(newParcours, newPosition, ensWordsFound, newColors) 

    def solver2_init(self):
        """ solver qui recherche dans le dictionnaire """
        result = []
        colors = ["white" for e in self.lettersList]
        for letter in self.dico:
            #print(letter)
            self.solver2_rec([], letter, result, colors, self.dico)
        res = set(result)
        res = self.decreasingList(res)
        return res

    def solver2_rec(self, prefix, letter, result, colors, dico_current):
        emplacements = self.g.isInGraph(letter)
        #print(emplacements)
        if emplacements==[]:
            #print("-> emplacement VIDE")
            return 
        else :
            for emplacement in emplacements :
                #print("->", emplacement)
                if prefix ==[] or self.g.isNeighbour(emplacement, prefix[-1][0]):
                    #print("-> est neighbour de precedent")
                    if colors[emplacement] == "white":
                        #print(colors[emplacement])
                        wordPotentiel = self.getWord(prefix + [(emplacement,letter)])
                        if '_NULL_' in dico_current[letter]:
                            result.append(wordPotentiel)
                        if dico_current[letter] != {'_NULL_':'_NULL_'}:
                            new_dico_current = dico_current[letter]
                            newColors = list(colors)
                            newColors[emplacement] = "black"
                            for newLetter in new_dico_current:
                                self.solver2_rec(prefix + [(emplacement, letter)], newLetter, result, newColors, new_dico_current)

    def getWord(self, list_couple):
        """recupere un string correspondant à la suite de cases séléctionnées """
        if list_couple == []:
            return ""
        return ''.join([e[1].lower() for e in list_couple])

    def decreasingList(self, words):
        """ retourne les words d'une liste en ordre decroissant de longueur"""
        dic = {}
        words = self.d.lowerList(words)
        for word in words:
            if not len(word) in dic:
                dic[len(word)] = []
            dic[len(word)].append(word)
        dic = dic.items()
        dic = sorted(dic)
        #dic.reverse() 
        return [f for e in dic for f in e[1]] 

    def wordsCounter(self, myList):
        res = 0
        if myList != None: 
            for e in myList:
                res +=1
        return res
