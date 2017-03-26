# -*- coding: utf-8 -*-

# Programme qui renomme tout les fichiers
# en un nom donner apres avoir donner le path
# Et faire une interface graphique
# Faire une sauvegarde de tout les anciens nom
# dans un fichier texte
# Bouton pour afficher que les fichiers, dossier ou tout

# uname() -> os


from os import chdir, listdir, getcwd
from os.path import isfile
from tkinter import *


class Interface(Frame):

    buttonState = {}  # State of the button
    fileList = list()  # List that contain the files name of the path
    buttonList = list()  # List that contain the checkButton

    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, width=500, height=500, **kwargs)
        self.pack(fill=BOTH)

        # Label with current path
        currentPath = "Current Path : " + getcwd()
        self.path = Label(self, text=currentPath)
        self.path.pack()

        # Error message shown if an error occur
        self.errorMessage = Label(self, text="")
        self.errorMessage.pack()

        # Textbox that let you input a path
        self.getPath = Entry(window, textvariable="", width=30)
        self.getPath.pack()

        # Button to change path
        self.buttonPath = Button(
            window, text="Change path", command=self.clickButtonPath)
        self.buttonPath.pack()

        # Button to change path
        self.buttonRename = Button(
            window, text="Rename", command=self.rename)
        self.buttonRename.pack()

    # Change the path and list the files on buttonPath click 
    def clickButtonPath(self):

        # Remove the checkButton when you change path
        self.removeCheckButton()

        path = self.getPath.get()  # Get the new path

        try:
            chdir(path)  # Change path
        except FileNotFoundError:
            error = "Unknown or non-existent path"
            self.errorMessage["text"] = error
        else:
            self.fileList = listdir()
            print(self.fileList)

            self.path["text"] = "Current path : " + getcwd()
            self.errorMessage["text"] = ""

            for file in self.fileList:
                self.buttonState[file] = IntVar(value=0)
                file = Checkbutton(self, text=file,
                                   variable=self.buttonState[file])
                file.pack()
                self.buttonList.append(file)

    # Method to remove checkButton
    def removeCheckButton(self):
        for file in self.buttonList:
            file.destroy()

    # Method to rename the files selected
    def rename(self):
        for state in self.buttonState.values():
            print(state.get())


window = Tk()
interface = Interface(window)

interface.mainloop()
interface.destroy()


# help("os")

# def choix():
#     print("Que voulez-vous renommer ? \n")
#     print("1. Les fichiers ")
#     print("2. Les dossiers ")
#     print("3. Les deux ")
#     choix = input("Choix : ")
#     return choix

# # Save le noms de tout les fichiers
# for element in liste_fichiers:
#     print(element)

# # Liste avec le nom de tout les files
# file = [f for f in liste_fichiers if isfile(f)]
# # Liste avec le nom de tout les Directories
# directory = [f for f in liste_fichiers if not isfile(f)]


# print(file)
# print(directory)
