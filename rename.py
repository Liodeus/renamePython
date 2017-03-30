# -*- coding: utf-8 -*-

# Programme qui renomme tout les fichiers
# en un nom donner apres avoir donner le path
# Faire une sauvegarde de tout les anciens nom
# dans un fichier texte
# Bouton pour afficher que les fichiers, dossier ou tout
# Changer de couleur pour diferencier les dossiers et fichiers
# uname() -> os
# # Save le noms de tout les fichiers
# for element in liste_fichiers:
#     print(element)
# # Liste avec le nom de tout les files
# file = [f for f in liste_fichiers if isfile(f)]
# # Liste avec le nom de tout les Directories
# directory = [f for f in liste_fichiers if not isfile(f)]


from os import chdir, listdir, getcwd, rename
from os.path import isfile
from tkinter import *


class Interface(Frame):

    buttonState = {}  # State of the button
    fileList = list()  # List that contain the files name of the path
    buttonList = list()  # List that contain the checkButton

    def __init__(self, window, **kwargs):
        window.minsize(width=350, height=350)
        Frame.__init__(self, window, **kwargs)
        self.pack(fill=BOTH)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        #  Ajouter bouton pour trier par ordre alpha
        choice = StringVar()

        self.All = Radiobutton(window, text="All", variable=choice,
                               value="All", command=self.All)
        self.onlyFiles = Radiobutton(window, text="Files",
                                     variable=choice, value="Files",
                                     command=self.Files)
        self.onlyDirectories = Radiobutton(
            window, text="Directories", variable=choice, value="Directories",
            command=self.Directories)

        self.All.pack()
        self.onlyFiles.pack()
        self.onlyDirectories.pack()

        self.All.select()

        # Label with current path
        currentPath = "Current Path : " + getcwd()
        self.path = Label(self, text=currentPath)
        self.path.pack(pady=10)

        # Error message shown if an error occur
        self.errorMessage = Label(self, text="")
        self.errorMessage.pack(pady=10)

        # Textbox that let you input a path
        self.getPath = Entry(window, textvariable="", width=30)
        self.getPath.pack(pady=10)

        # Button to change path
        self.buttonPath = Button(
            window, text="Change path", command=self.clickButtonPath)
        self.buttonPath.pack(pady=10)

        # Button to rename
        self.buttonRename = Button(
            window, text="Rename", command=self.renameFiles)
        self.buttonRename.pack(pady=10)

        # Change the position
        # Label with new files name
        # self.newNameBox = Label(self, text="New name")
        # self.newNameBox.pack(side=TOP)

        # Textbox that let you input name to rename all the files
        self.renameBox = Entry(window, textvariable="", width=30)
        self.renameBox.pack(pady=10)

        self.showCheckButton("All")

    def All(self):
        self.removeCheckButton()
        self.showCheckButton("All")

    def Files(self):
        self.removeCheckButton()
        self.showCheckButton("Files")

    def Directories(self):
        self.removeCheckButton()
        self.showCheckButton("Directories")

    # Change the path and list the files on buttonPath click
    def clickButtonPath(self):

        # Remove the checkButton when you change path
        self.removeCheckButton()

        path = self.getPath.get()  # Get the new path

        try:
            chdir(path)  # Change path
        except FileNotFoundError:
            self.showCheckButton("All")
            error = "Unknown or non-existent path"
            self.errorMessage["text"] = error
        else:
            self.showCheckButton("All")

    # Method to remove checkButton
    def removeCheckButton(self):
        for file in self.buttonList:
            file.destroy()

    # Method to rename the files selected
    def renameFiles(self):
        i = 0
        for key, state in self.buttonState.items():
            currentPath = "./" + key
            name = self.renameBox.get() + str(i)
            newName = "./" + name
            if(state.get() == 1):
                if(name not in self.fileList):
                    rename(currentPath, newName)
                    i += 1
                else:
                    error = "Unknown or non-existent path"
                    self.errorMessage["text"] = error

        # Remove the checkButton when the files change names
        self.removeCheckButton()
        self.reset()
        # Refresh the checkButton
        self.showCheckButton("All")

    # Display the checkButton
    def showCheckButton(self, val):
        self.fileList = listdir()

        self.path["text"] = "Current path : " + getcwd()
        self.errorMessage["text"] = ""

        for file in self.fileList:
            # Change the color
            if(isfile(file)):
                color = 'blue'  # Is a file
            else:
                color = 'red'  # Is a directory

            if(val == "All"):
                self.buttonState[file] = IntVar(value=0)
                file = Checkbutton(self, text=file,
                                   variable=self.buttonState[file],
                                   fg=color, activeforeground=color)
                file.pack()
                self.buttonList.append(file)
            elif(val == "Files"):
                if(isfile(file)):
                    self.buttonState[file] = IntVar(value=0)
                    file = Checkbutton(self, text=file,
                                       variable=self.buttonState[file],
                                       fg=color, activeforeground=color)
                    file.pack()
                    self.buttonList.append(file)
            elif(val == "Directories"):
                if(not isfile(file)):
                    self.buttonState[file] = IntVar(value=0)
                    file = Checkbutton(self, text=file,
                                       variable=self.buttonState[file],
                                       fg=color, activeforeground=color)
                    file.pack()
                    self.buttonList.append(file)
            else:
                self.errorMessage["text"] = "Error"

    # Reset list and dict -> when you change path or rename
    def reset(self):
        self.buttonList = list()
        self.fileList = list()
        self.buttonState = {}


window = Tk()

interface = Interface(window)

interface.mainloop()
interface.destroy()
