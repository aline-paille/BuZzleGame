#!/usr/bin/python3.1
import string
from re import *
from Variables import *

class Dictionary:
    def __init__(self, language):
        self.dicoList = self.get_dico_correct("../dictionaries/dictionary_fr.txt", language)
        self._end = "_NULL_"
        self.dicoTree = self.make_arbre(self.dicoList)

    # def getDicoFromFile(self, file):
    #     """ recupere la liste de words contenus dans un file"""
    #     f = open(file, 'r')
    #     myList = f.read().split('\n')
    #     myList = l[:-1]
    #     f.close()
    #     return myList

    def getDicoFromXMLFile(self, file):
        return findall(r'<lemma>(.*)</lemma>',open(file, 'r').read(), M|I)

    def lowerList(self, myList):
        """ retourne la liste des words en minuscule"""
        return [e.lower() for i,e in enumerate(myList)]


    def deleteAccentuation(self, myList):
        return [e.translate(str.maketrans("àâäéèêëîïôöûü","aaaeeeeiioouu")) for e in myList] 

    def isAccentuated(self, word):
        for i,e in enumerate(word):
            if e in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                return True
        return False       

    def deleteWordsAccentuated(self, myList):
        return [e for i,e in enumerate(myList) if self.isAccentuated(e)==False]
    
    def deleteMultiplePartWords(self, myList):
        return [e for i,e in enumerate(myList) if not ' ' in e]

    def writeInFile(self, myList, file):
        """ ecrit la liste de word dans un file """
        fic = open(file, 'w')
        for i,e in enumerate(myList):
            fic.write(e)
            fic.write("\n")
        fic.close()
    
    def get_dico_correct(self, file, language):
        #TODO: create new function to use directly my .txt file of each language
        if language == FRENCH_LANGUAGE:
        	L = self.getDicoFromXMLFile("../dictionaries/dela-fr-public-u8.dic.xml")
        elif language == ENGLISH_LANGUAGE :
		#L = self.getDicoFromXMLFile("../dictionaries/dela-en-public-u8_2.dic.xml")
            L = self.getDicoFromXMLFile("../dictionaries/dela-fr-public-u8.dic.xml")
        else : 
            print("error : bad language askeds")
        Lbis = self.lowerList(L)
        L1 = self.deleteAccentuation(Lbis)
        L2 = self.deleteWordsAccentuated(L1)
        L3 = self.deleteMultiplePartWords(L2)
        self.dico = L3
        self.writeInFile(L3, file)
        return L3

    def make_arbre(self, words):
        """ fonction qui creer l'arbre dictionnaire """
        dicoFinal = {}
        for word in words:
            dico_current = dicoFinal
            for j,letter in enumerate(word):
                dico_current = dico_current.setdefault(letter, {})
            dico_current = dico_current.setdefault(self._end, self._end)
        return dicoFinal
    
    def isInTree(self, word):
        """ verifife si un word appartient au dictionnaire """
        dico_current = self.dicoTree
        for letter in word :
            if letter in dico_current:
                dico_current = dico_current[letter]
            else :
                return False 
        else :
            if self._end in dico_current :
                return True
            else :
                return False 
            
    def prefixIsInTree(self, prefix):
        """ fonction qui nous dit si le prefix peut etre un word du 
        dictionnaire ou non """
        dico_current = self.dicoTree
        for letter in prefix :
            if letter in dico_current :
                dico_current = dico_current[letter]
            else : 
                return False
        return True
