#!/usr/bin/python3.2

from tkinter import *
from HelpWindow import *
from AboutWindow import *
from Form import *
from Game import *
from Variables import *
import gettext

en_GB = gettext.translation('Window', localedir='lang\locales', languages=['en_GB'])
fr_FR = gettext.translation('Window', localedir='lang\locales', languages=['fr_FR'])
en_GB.install()

class Window:
    
    def __init__(self):
        self.window = Tk()  
        self.window.title(_("BUZzLE"))
        self.window.resizable(False, False)

        menuBar = Menu(self.window)
        self.window.config(menu=menuBar)

        menuGame = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label=_("Game"), menu=menuGame)
        #menuGame.add_command(label=_("Home"), command=self.backToHome)
        menuGame.add_command(label=_("Exit"), command=self.quit)

        self.language = ENGLISH_LANGUAGE

        self.message = StringVar()
        self.depositLabel = Label(self.window, textvariable = self.message)
        self.depositLabel.pack()
        self.message.set('Click on the bee to validate your french word! :-)')

        # languagesMenu = Menu(menuBar, tearoff=False)
        # menuBar.add_cascade(label=_("Languages"), menu=languagesMenu)
        # languagesMenu.add_command(label=_("French"), command=lambda:self.switchLanguage(FRENCH_LANGUAGE))
        # languagesMenu.add_command(label=_("English"), command=lambda:self.switchLanguage(ENGLISH_LANGUAGE))

        # helpMenu = Menu(menuBar, tearoff=False)
        # menuBar.add_cascade(label=_("Help"), menu=helpMenu)
        # helpMenu.add_command(label=_("Help"), command=self.displayHelp)
        # helpMenu.add_command(label=_("About"), command=self.displayAbout)

        self.optionsSelection()

    def start(self):
        self.window.mainloop()
        
    def quit(self):
        self.window.destroy()

    def backToHome(self):
        self.languageSelectionWindow()

    def switchLanguage(self, selectedLanguage):
        """ TODO: save new language and restart the app + alerte the user OR go to a main window"""
        if selectedLanguage == FRENCH_LANGUAGE:
            fr_FR.install()
            self.message.set('français') 
        elif selectedLanguage == ENGLISH_LANGUAGE:        
            en_GB.install()
            self.message.set('english')
        else:
            self.message.set('error')

    def displayHelp(self):
        helpWindow = HelpWindow()

    def displayAbout(self):
        aboutWindow = AboutWindow()

    def createGame(self, event):
        self.getFormInfo()
        self.form.destroy() # destroy start Window       
        self.game = Game(self) # open Game window

    def getFormInfo(self):
        self.solver = self.form.solver.get()
        if self.solver != SOLVER_TYPE_0 and self.solver != SOLVER_TYPE_1:
            print("001","Solver get back error.")

        self.level = self.form.level.get()  #cases_boires
        if self.level != LEVEL_TYPE_0 and self.level != LEVEL_TYPE_1:     
            print("002","Level type get back error.")
        
        self.joker = self.form.joker.get()
        if  self.joker != JOKER_TYPE_0 and self.joker != JOKER_TYPE_1:
            print("003","Joker get back error")

    def optionsSelection(self):
        self.form = Form(self)
        self.game = None
        self.language = ENGLISH_LANGUAGE 
        self.solver = SOLVER_TYPE_0
        self.level = LEVEL_TYPE_0
        self.joker = JOKER_TYPE_0
        
    def updateMesasgeText(self, message):
        self.message.set(message)

