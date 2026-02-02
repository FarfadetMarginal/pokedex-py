import tkinter as tk
from tkinter import messagebox

# Liste des couleurs disponibles
couleurs = [
    "red",
    "green",
    "blue",
    "yellow",
    "#FF5733",
    "#3498DB",
    "#2ECC71"
]

def changer_couleur():
    try:
        # Récupérer l'index de la couleur sélectionnée
        index = listbox.curselection()
        if not index:
            raise ValueError("Aucune couleur sélectionnée")

        # Récupérer la couleur
        couleur = listbox.get(index)

        # Appliquer la couleur de fond
        fenetre.configure(bg=couleur)

    except Exception:
        messagebox.showerror(
            "Erreur",
            "Veuillez sélectionner une couleur valide."
        )

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Changer la couleur de fond")
fenetre.geometry("300x250")

# Listbox des couleurs
listbox = tk.Listbox(fenetre)
for c in couleurs:
    listbox.insert(tk.END, c)
listbox.pack(pady=10)

# Bouton pour changer la couleur
bouton = tk.Button(
    fenetre,
    text="Change Background",
    command=changer_couleur
)
bouton.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()