import tkinter as tk
fenetre = tk.Tk()

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
        print(f"Nom : {self.name}")
        print(f"Pokemon numéro  {self.number}")
        print(f"Type : {self.type}")
        print(f"Il mesure {self.height} et pèse {self.weight}")
        print(f"Statistiques : ")
        print(f"PV = {self.hp}")
        print(f"Attaque = {self.attack}")
        print(f"Defense = {self.defense}")
        print(f"Attaque spéciale = {self.spatt}")
        print(f"Defense spéciale = {self.spdef}")
        print(f"Vitesse = {self.speed}")


bublizarre = Pokemon("Bulbizarre", 1, ["plante", "poison"], 0.7, 6.9, 45, 49, 49, 65, 65, 45)
print(Pokemon.self.name)






fenetre.geometry("1024x768")
fenetre.mainloop()