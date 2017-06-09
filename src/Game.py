#!/usr/bin/python3.1

from tkinter import *
from Plateau import *
from datetime import datetime, timedelta, time

class Game():
    def __init__(self, parent):
        self.parentWindow = parent
        self.background = PhotoImage(file = "../images/appli.gif")
        self.game_over = PhotoImage(file = "../images/gameOver.gif")
        self.frame = Frame(self.parentWindow.window, width = self.background.width(), height=self.background.height()) 

        parent.window.geometry("1104x640")


       # creation du canvas qui contient les widjets
        self.canvas = Canvas(self.frame, width = self.background.width(), height=self.background.height(), background="white")
        self.canvas.create_image(0,0, image = self.background, anchor = NW)

        self.time = datetime(2000, 1, 1, 0, 2, 0)
        self.timeLeft = None

        self.nbResults = 0

        self.score = 0
        self.scoreLabel =  self.canvas.create_text(898, 555, font=("Arial", 24, "bold"), text = "0")

        self.myListBox = Listbox(parent.window, bg = "white", width=15, height=self.background.height())
        self.myListBox.pack(side = RIGHT)

        self.updateTimeLeft()

        
        self.plateau = Plateau(self.parentWindow, self, self.canvas)
        self.canvas.bind("<Button-1>", lambda event, x = self.canvas : self.plateau.click_canvas(event, x)) #self.plateau.click_triangle)
        self.canvas.pack()
        self.frame.pack(side = RIGHT)

    def updateTimeLeft(self):
        self.time = self.time - timedelta(seconds=1)

        if self.time.strftime("%M:%S") == "00:00":
            self.plateau = None
            self.canvas.create_image(0,0, image = self.game_over, anchor = NW)
            self.canvas.create_text(898, 555, font=("Arial", 24, "bold"), text = self.score)
        else:
            if self.timeLeft is not None:
                self.canvas.delete(self.timeLeft)

            self.timeLeft = self.canvas.create_text(958, 450, font=("Arial", 18), text = self.time.time().strftime("%M:%S"))

            self.frame.after(1000, self.updateTimeLeft)

    def updateScore(self):
        lastWord = self.plateau.getWord(self.plateau.word)
        wordLength = len(self.plateau.word)
        self.score += wordLength

        message = "\"" + lastWord + "\" is a valid word! +" + str(wordLength) + " points."
        self.parentWindow.updateMesasgeText(message)
        print("valid word! +", wordLength, " points")

        self.canvas.delete(self.scoreLabel)
        self.scoreLabel = self.canvas.create_text(898, 555, font=("Arial", 24, "bold"), text = self.score)
        self.nbResults += 1
        self.canvas.create_text(10, 20 * self.nbResults, font=("Arial", 14), text=lastWord, anchor=W)
        
    def insertListBox(self,myListe):
        for item in myListe :
            self.myListBox.insert(0, item)
        self.myListBox.pack()

    def destroy(self):
        self.frame.destroy()


   

   
