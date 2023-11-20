import tkinter as tk
from tkinter import messagebox
import json

class ListeCoursesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Liste de courses")

        # Charger la liste de courses depuis le fichier
        self.liste_courses = self.charger_liste()

        # Créer les widgets
        self.label = tk.Label(root, text="Liste de courses")
        self.listbox = tk.Listbox(root)
        self.ajouter_button = tk.Button(root, text="Ajouter", command=self.ajouter_article)
        self.supprimer_button = tk.Button(root, text="Supprimer", command=self.supprimer_article)
        self.sauvegarder_button = tk.Button(root, text="Sauvegarder", command=self.sauvegarder_liste)
        self.quitter_button = tk.Button(root, text="Quitter", command=self.root.destroy)

        # Placer les widgets dans la fenêtre
        self.label.pack(pady=10)
        self.listbox.pack(pady=10)
        self.ajouter_button.pack(pady=5)
        self.supprimer_button.pack(pady=5)
        self.sauvegarder_button.pack(pady=5)
        self.quitter_button.pack(pady=5)

        # Afficher la liste de courses
        self.afficher_liste()

    def charger_liste(self):
        try:
            with open("liste_courses.json", "r") as fichier:
                return json.load(fichier)
        except FileNotFoundError:
            return []

    def sauvegarder_liste(self):
        with open("liste_courses.json", "w") as fichier:
            json.dump(self.liste_courses, fichier)
        messagebox.showinfo("Sauvegarde", "Liste sauvegardée avec succès.")

    def afficher_liste(self):
        self.listbox.delete(0, tk.END)
        for article in self.liste_courses:
            self.listbox.insert(tk.END, article)

    def ajouter_article(self):
        article = simpledialog.askstring("Ajouter un article", "Entrez l'article à ajouter :")
        if article:
            self.liste_courses.append(article)
            self.afficher_liste()

    def supprimer_article(self):
        selected
