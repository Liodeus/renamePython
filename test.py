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
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    fichier = {}
    liste_fichiers = list()

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=500, height=500, **kwargs)
        self.pack(fill=BOTH)

        cheminActuel = "Chemin actuel : " + getcwd()
        self.chemin = Label(self, text=cheminActuel)
        self.chemin.pack()

        self.errorMessage = Label(self, text="")
        self.errorMessage.pack()

        self.entrer = Entry(fenetre, textvariable="", width=30)
        self.entrer.pack()

        self.bouton = Button(
            fenetre, text="Changer de dossier", command=self.cliquer)
        self.bouton.pack()

    def cliquer(self):
        self.remove_checkbox()
        path = self.entrer.get()
        try:
            chdir(path)  # Change le chemin ou l'on se trouve
        except FileNotFoundError:
            error = "Chemin inconnu ou innexistant"
            self.errorMessage["text"] = error
        else:
            self.liste_fichiers = listdir()
            print(self.liste_fichiers)

            self.chemin["text"] = "Chemin actuel : " + getcwd()
            self.errorMessage["text"] = ""

            for file in self.liste_fichiers:
                self.file = Label(self, text=file)
                self.file.pack()
            # for file in self.liste_fichiers:
            #     self.fichier[file] = IntVar(value=0)
            #     case = Checkbutton(self, text=file,
            #                        variable=self.fichier[file])
            #     case.pack()

    def remove_checkbox(self):
        for cle in self.fichier.keys():
            self.fichier[cle].destroy()


fenetre = Tk()

interface = Interface(fenetre)


interface.mainloop()

interface.destroy()


# # On crée une fenêtre, racine de notre interface
# fenetre = Tk()
# bouton = Checkbutton(fenetre, text="Nouveau?")
# bouton.pack()

# test = list()
# test.append(bouton)
# print(test)

# test[0].destroy()
# # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
# fenetre.mainloop()


# help("os")

# def choix():
#     print("Que voulez-vous renommer ? \n")
#     print("1. Les fichiers ")
#     print("2. Les dossiers ")
#     print("3. Les deux ")
#     choix = input("Choix : ")
#     return choix


# def choixPath():
#     pathCorrect = False

#     while not pathCorrect:
#         try:
#             path = input("Entrer le chemin du dossier : ")
#             chdir(path)  # Change le chemin ou l'on se trouve
#         except FileNotFoundError:
#             print("Chemin inconnu ou innexistant")
#         else:
#             pathCorrect = True
#             liste_fichiers = listdir()  # Liste avec les noms de fichiers
#     return liste_fichiers

# liste_fichiers = choixPath()
# choix = choix()


# # Save le noms de tout les fichiers
# for element in liste_fichiers:
#     print(element)

# # Liste avec le nom de tout les files
# file = [f for f in liste_fichiers if isfile(f)]
# # Liste avec le nom de tout les Directories
# directory = [f for f in liste_fichiers if not isfile(f)]


# print(file)
# print(directory)
