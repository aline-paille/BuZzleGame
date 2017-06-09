#!/usr/bin/python3.1
from tkinter import *
from Variables import *

class Form:
    """Fenetre du Form de Ruzzle :
    self.frame = fenetre,
    self.fond = imaage de fond du canvas,
    self.canvas = canvas qui contient les widgets,
    ... """

    def __init__(self, Parent):   
        self.background = PhotoImage(file = "../images/appli.gif")
        self.frame = Frame(Parent.window, height=self.background.height(), width = self.background.width())

        self.canvas = Canvas(self.frame, width = self.background.width(), height=self.background.height(), background="white")
        self.canvas.create_image(0,0, image = self.background, anchor = NW)
        
        # creation de textes d'indication
        self.text = ("helvetica neue", 14)
        self.texte2 = self.canvas.create_text(10, 50, text =_("Solver type: "), font = self.text, anchor="w")
        self.texte3 = self.canvas.create_text(10, 100, text =_("Level: "), font = self.text, anchor="w")
        self.texte4 = self.canvas.create_text(10, 150, text =_("Jokers: "), font = self.text, anchor="w")

        # RadioButton solveur
        self.solver = IntVar(value=0)
        self.R3 = Radiobutton(self.canvas, text=_("Graph"), variable=self.solver, value=0, bg=FORM_BUTTONS_COLOR, justify=LEFT)
        self.radiobout3 = self.canvas.create_window(180, 50, window = self.R3, width=80, height=30) 
        self.R4 = Radiobutton(self.canvas, text=_("Dico"), variable=self.solver, value=1, bg=FORM_BUTTONS_COLOR, justify=LEFT)
        self.radiobout4 = self.canvas.create_window(250, 50, window = self.R4, width=80, height=30) 

        # RadioBoutons cases noires
        self.level = IntVar(value = 0)
        self.R6 = Radiobutton(self.canvas, text=_("Easy"), variable=self.level, value=0, bg=FORM_BUTTONS_COLOR, justify=LEFT)
        self.radiobout6 = self.canvas.create_window(180, 100, window = self.R6, width=80, height=30) 
        self.R5 = Radiobutton(self.canvas, text=_("Hard"), variable=self.level, value=1, bg=FORM_BUTTONS_COLOR, justify=LEFT)
        self.radiobout5 = self.canvas.create_window(250, 100, window = self.R5, width=80, height=30) 

        # RadioBoutons cases joker
        self.joker = IntVar(value = 0)
        self.R8 = Radiobutton(self.canvas, text=_("No"), variable=self.joker, value=0, bg=FORM_BUTTONS_COLOR, justify=LEFT)
        self.radiobout8 = self.canvas.create_window(180, 150, window = self.R8, width=80, height=30)
        self.R7 = Radiobutton(self.canvas, text=_("Yes"), variable=self.joker, value=1, bg=FORM_BUTTONS_COLOR, justify=LEFT)
        self.radiobout7 = self.canvas.create_window(250, 150, window = self.R7, width=80, height=30)  

        # bouton "Jouer"
        self.image_play = PhotoImage(file = "../images/play.gif")
        self.bouton_play = self.canvas.create_image(150,400,image = self.image_play)
        self.canvas.tag_bind(self.bouton_play, '<ButtonPress-1>', Parent.createGame) 

        self.frame.pack()
        self.canvas.pack()

    def destroy(self):
        self.frame.destroy()

