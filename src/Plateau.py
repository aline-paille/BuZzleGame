#!/usr/bin/python3.1
from Dictionary import *
from Variables import *
from Solver import *
from tkinter import *
from Graph import *
from math import *

class Plateau: 
    """ classe du plateau de jeu :
    self.word = word formé par le joueur,
    self.items = dico qui associe un boolean à chaqui item pour savoir si les element du canvas sont selectionnés ou non,
    self.lettersList = liste des lettres qui constitues le plateau ruzzle,
    self.dico = objet Dictionnary,
    self.graph = objet Graph,
    self.solver = objet Solver"""

    def __init__(self, parentWindow, parentGame, parentCanvas): 
        self.parentWindow = parentWindow
        self.parentGame = parentGame
        self.parentCanvas = parentCanvas
        self.items = {}
        self.wordsFound = []
        self.language = parentWindow.language
        self.solver = parentWindow.solver
        self.graph = Graph(self.language)
        self.lettersList = self.graph.lettersList
        self.draw_hexagon(parentCanvas, 340, 95, 140)
        self.word = []
        self.dico = Dictionary(self.language)
        self.solver = Solver(self.graph, self.dico, self.lettersList,self.solver)
        self.solutionSolver = self.solver.solution
        self.parentGame.insertListBox(self.solutionSolver)

        self.validationPolygon = parentCanvas.create_polygon(820, 0, 1030, 0, 1030, 180, 820, 180, fill='')

    def draw_hexagon(self,parent, X ,Y, l):
        """ fonction qui dessine l'hexagone, ses tirangles et ses lettres """
        h = sin((pi)/3)* l
        X1 = X + l/2
        X2 = X+l
        X3 = X + 3*l/2
        X4 = X + 2*l
        X5 = X + 5*l/2
        X6 = X + 3*l
    
        Y1 = Y + h
        Y2 = Y + 2 * h
        Y3 = Y + 3 * h
        
        trianglesList = [
            (X1,Y,True),(X2, Y,False),(X3,Y, True),(X4,Y,False),(X5,Y,True),
            (X,Y1,True),(X1,Y1,False),(X2,Y1,True),(X3,Y1,False),(X4,Y1,True),
            (X5,Y1,False),(X6,Y1,True),(X,Y2,False),(X1,Y2,True),(X2,Y2,False),
            (X3,Y2,True),(X4,Y2,False),(X5,Y2,True),(X6,Y2,False),(X1,Y3,False),
            (X2, Y3,True),(X3,Y3, False),(X4,Y3,True),(X5,Y3,False)]
        for i,e in enumerate(trianglesList):
            self.drawTriangle(parent, i, e[0],e[1], l, e[2])
        for i,e in enumerate(trianglesList):
            self.drawLetter(parent, i, e[0],e[1], e[2])

    def drawTriangle(self, parentCanvas, item, x, y, l, haut):
        """ fonction qui dessine les triangles, chacun d'eux aura un item compris entre 4 et 28"""
        h = sin((pi)/3)* l
        if haut== True:
            it = parentCanvas.create_polygon(x, y+h , x+l, y+h, x+l//2, y, outline=TRANSPARENCE, width=2, fill=TRANSPARENCE)
            self.items[item] = False
        else: 
            it = parentCanvas.create_polygon(x, y , x+l, y, x+l//2, y+h, outline=TRANSPARENCE, width=2, fill=TRANSPARENCE)
            self.items[item] = False

    def drawLetter(self, parentCanvas, item, x, y, haut):
        """ fonction qui dessine les lettres chaque lettre aura un item compris entre 28 et 52 """
        if haut== True:
            parentCanvas.create_text(x+55, y+75,font = ("leelawadee", 40, 'bold'), text=self.lettersList[item],anchor = W)
        else: 
            parentCanvas.create_text(x+50, y+45,font = ("leelawadee", 40, 'bold'), text=self.lettersList[item],anchor = W)
                
    def click_canvas(self, parent, event):
        """ fct qui récupere le dernier item sur lequel on a clické ie l'item du triangle clické et modifie la couleur du triangle (décalage des item de 4 car l existe surement déja des items associés au canvas ou a la frame)"""
        item = event.find_withtag(CURRENT)
        print(item)
        if item[0] < 28 and item[0] >= 4 :
            self.click_triangle(event, item)
        elif item[0] < 52 and item[0] >= 28 :
            it = event.find_withtag(item[0] - 24)
            self.click_triangle(event, it)
        elif item[0] == 52:
            self.click_valid_button()

    def click_triangle(self, event, item):
        """ action lors de l'evenement clique sur un triangle """
        # verifier que le triangle courrant est bien voisin du dernier selectionné
        if self.word==[] or self.graph.isNeighbour(self.word[-1][0], item[0]-4) or self.word[-1][0] == item[0]-4:
            if self.items[item[0]-4]==False:
                self.addLetter(event, item)
            # impossible de supprimer une autre lettre que la derniere du mot
            elif self.items[item[0]-4]==True and self.lettersList[item[0]-4]==self.word[-1][1] and item[0]-4==self.word[-1][0]: 
                self.deleteLetter(event, item)
        # impression du mot
        # self.getWord(self.word)


    def deleteLetter(self, event, item):
        """ fonction qui supprime la lettre correspondant a l'item du triangle cliqué lors de l'event, rend transparent ce triangle et remet le booleen associe à False """
        event.itemconfig(item, fill = TRANSPARENCE)
        self.word = self.word[0:-1]
        self.items[item[0]-4] = False

    def addLetter(self, event, item):
        """ fonction qui ajoute la lettre correspondant a l'item du triangle cliqué lors de l'event, rend ce triangle rouge et met le 
        booleen associe à True """
        event.itemconfig(item, fill = "red")
        event.itemconfig(item, stipple = 'gray50')
        self.word.append((item[0]-4, self.lettersList[item[0]-4]))  
        self.items[item[0]-4] = True

    def getWord(self, selections):
        res = ''.join([e[1].lower() for i,e in enumerate(selections)])
        print(res)
        return res

    def click_valid_button(self):
        tempMot = self.getWord(self.word)
        if(self.dico.isInTree(tempMot)):
            self.wordsFound.append(tempMot)
            self.parentGame.updateScore()
            print(self.wordsFound)
            #self.word =[]
            #for i in self.items:
                #self.parentCanvas.itemconfig(i, fill = TRANSPARENCE)
                #self.items[i[0]-4] = False

                
        else :
            print(tempMot, "doesn't exist in the dictionary.")
            message = "\"" + tempMot + "\" is not in the dictionary."
            self.parentWindow.updateMesasgeText(message)