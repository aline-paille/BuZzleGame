#!/usr/bin/python3.1
import string
from re import *
from Variables import *

LEAF = "_NULL_"

class Dictionary:
    def __init__(self, language):
        """ we use a lexicograpic tree = dicoList"""
        if language == FRENCH_LANGUAGE:
            self.dicoList = self.getDicoFromTXTFile("../dictionaries/dictionary_fr.txt")
        elif language == ENGLISH_LANGUAGE:
            self.dicoList = self.getDicoFromTXTFile("../dictionaries/dictionary_fr.txt")
        # if dictionary_fr.txt not presnet use:
        # self.dicoList = self.get_dico_correct("../dictionaries/dictionary_fr.txt", language)

        self.trie = self.createDicoAsTree(self.dicoList)

    def getDicoFromTXTFile(self, file):
        f = open(file, 'r')
        myList = f.read().split('\n')
        myList = myList[:-1]
        f.close()
        return myList

    def createDicoAsTree(self, words):
        tree = {}
        for word in words:
            currentTree = tree
            for j,letter in enumerate(word):
                currentTree = currentTree.setdefault(letter, {})
            currentTree = currentTree.setdefault(LEAF, LEAF)
        return tree
    
    def isInTree(self, word):
        currentTree = self.trie
        for letter in word :
            if letter in currentTree:
                currentTree = currentTree[letter]
            else :
                return False 
        else :
            if LEAF in currentTree :
                return True
            else :
                return False 
            
    def prefixIsInTree(self, prefix):
        currentTree = self.trie
        for letter in prefix :
            if letter in currentTree :
                currentTree = currentTree[letter]
            else : 
                return False
        return True



    def getDicoFromXMLFile(self, file):
        return findall(r'<lemma>(.*)</lemma>',open(file, 'r').read(), M|I)

    def lowerList(self, myList):
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
        fic = open(file, 'w')
        for i,e in enumerate(myList):
            fic.write(e)
            fic.write("\n")
        fic.close()
    
    def get_dico_correct(self, file, language):
        if language == FRENCH_LANGUAGE:
            L = self.getDicoFromXMLFile("../dictionaries/dela-fr-public-u8.dic.xml")
        elif language == ENGLISH_LANGUAGE :
            L = self.getDicoFromXMLFile("../dictionaries/dela-en-public-u8_2.dic.xml")
        else : 
            print("error : bad language asked")
        Lbis = self.lowerList(L)
        L1 = self.deleteAccentuation(Lbis)
        L2 = self.deleteWordsAccentuated(L1)
        L3 = self.deleteMultiplePartWords(L2)
        self.dico = L3
        self.writeInFile(L3, file)
        return L3