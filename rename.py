# -*- coding: utf-8 -*-

# Programme qui renomme tout les fichiers
# en un nom donner apres avoir donner le path
# Faire une sauvegarde de tout les anciens nom
# dans un fichier texte
# Bouton pour afficher que les fichiers, dossier ou tout

# uname() -> os


from os import chdir, listdir, getcwd, rename
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

        # Button to rename
        self.buttonRename = Button(
            window, text="Rename", command=self.renameFiles)
        self.buttonRename.pack()

        # Change the position 
        # Label with new files name
        # self.newNameBox = Label(self, text="New name")
        # self.newNameBox.pack(side=BOTTOM)

        # Textbox that let you input name to rename all the files
        self.renameBox = Entry(window, textvariable="", width=30)
        self.renameBox.pack()

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
            self.showCheckButton()

    # Method to remove checkButton
    def removeCheckButton(self):
        for file in self.buttonList:
            file.destroy()

    # Method to rename the files selected
    def renameFiles(self):
        i = 0
        for key, state in self.buttonState.items():
            print(key, " = ", state.get())
            currentPath = "./" + key
            newName = "./" + self.renameBox.get() + str(i)
            if(state.get() == 1):
                print(state.get())
                print(currentPath)
                print(newName)
                rename(currentPath, newName)
                i += 1

        # Remove the checkButton when the files change names
        self.removeCheckButton()
        self.buttonList = list()
        # Refresh the checkButton
        self.showCheckButton()

    # Display the checkButton
    def showCheckButton(self):
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


window = Tk()
interface = Interface(window)

interface.mainloop()
interface.destroy()


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
