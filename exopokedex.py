import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()


label1 = tk.Label(fenetre, text="0")
label1.grid(row=1, column = 0)

imagebulbizarre = tk.PhotoImage(file="img/Bulbizarre.png")
image1 = imagebulbizarre.subsample(3, 3)

class Pokemon:
    def __init__(self, nom, numero, type, taille, poids, hp, attaque, defense, attaquespeciale, defensespeciale, vitesse):
        self.name = nom
        self.number = numero
        self.type = type
        self.height = taille
        self.weight = poids
        self.hp = hp
        self.attack = attaque
        self.defense = defense
        self.spatt = attaquespeciale
        self.spdef = defensespeciale
        self.speed = vitesse

    def afficher_infos(self):
        print(f"{self.name}")
        print(f"Pokemon numéro  {self.number}")
        print(f"Type : {self.type}")
        print(f"Il mesure {self.height}m et pèse {self.weight}Kg")
        print(f"Statistiques : ")
        print(f"PV = {self.hp}")
        print(f"Attaque = {self.attack}")
        print(f"Defense = {self.defense}")
        print(f"Attaque spéciale = {self.spatt}")
        print(f"Defense spéciale = {self.spdef}")
        print(f"Vitesse = {self.speed}")

        label1.config(text=f"{self.name} \n Pokemon numéro  {self.number} \n Il mesure {self.height}m et pèse {self.weight}Kg \n Il est de type {self.type} \n Statistiques : \n PV = {self.hp}  \n Attaque = {self.attack} \n Defense = {self.defense} \n Attaque spéciale = {self.spatt} \n Defense spéciale = {self.spdef} \n Vitesse = {self.speed} ")
        label2.config(image = image1)

    

    

def afficher_tout():
    
    bulbizarre.afficher_infos()


pokemonlist = [
    "bulbizarre", "herbizarre", "florizarre"
]


bulbizarre = Pokemon("Bulbizarre", 1, ["plante", "poison"], 0.7, 6.9, 45, 49, 49, 65, 65, 45)
herbizarre = Pokemon("Herbizarre", 2, ["plante", "poison"], 1, 13, 60, 62, 63, 80, 80, 60)

listbox = tk.Listbox(fenetre, width=40)
for pok in pokemonlist:
    listbox.insert(tk.END,pok)
listbox.grid(row=0, column = 0)

label1 = tk.Label(fenetre, text="0")
label1.grid(row=1, column = 0)
label2 = tk.Label(fenetre, text="0")
label2.grid(row=2, column = 0)


bouton = tk.Button(fenetre, text="infos", command=afficher_tout)
bouton.grid(row=3, column = 0)




fenetre.geometry("1024x768")
fenetre.mainloop()