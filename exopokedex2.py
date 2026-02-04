import tkinter as tk
from tkinter import messagebox
import os
fenetre = tk.Tk()

fichier = open("sauvegardepokedex.txt", "a")

imagebulbizarre = tk.PhotoImage(file="img/Bulbizarre.png")
image1 = imagebulbizarre.subsample(3, 3)
imageherbizarre = tk.PhotoImage(file="img/Herbizarre.png")
image2 = imageherbizarre.subsample(3, 3)
imageflorizarre = tk.PhotoImage(file="img/Florizarre.png")
image3 = imageflorizarre.subsample(3, 3)
imagesalameche= tk.PhotoImage(file="img/Salamèche.png")
image4 = imagesalameche.subsample(3, 3)
imagereptincel= tk.PhotoImage(file="img/Reptincel.png")
image5 = imagereptincel.subsample(3, 3)
imagedracaufeu= tk.PhotoImage(file="img/Dracaufeu.png")
image6 = imagedracaufeu.subsample(3, 3)
imagecarapuce= tk.PhotoImage(file="img/Carapuce.png")
image7 = imagecarapuce.subsample(3, 3)
imagecarabaffe= tk.PhotoImage(file="img/Carabaffe.png")
image8 = imagecarabaffe.subsample(3, 3)
imagetortank= tk.PhotoImage(file="img/Tortank.png")
image9 = imagetortank.subsample(4, 4)
logo = tk.PhotoImage(file="img/pngwing.com (3).png")
logo1 = logo.subsample(3, 3)


class Pokemon:
    def __init__(self, nom, numero, type, taille, poids, hp, attaque, defense, attaquespeciale, defensespeciale, vitesse, image):
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
        self.img = image


bulbizarre = Pokemon("bulbizarre", 1, ["plante", "poison"], 0.7, 6.9, 45, 49, 49, 65, 65, 45, image1)
herbizarre = Pokemon("herbizarre", 2, ["plante", "poison"], 1, 13, 60, 62, 63, 80, 80, 60, image2)
florizarre = Pokemon("florizarre", 3, ["plante", "poison"], 2, 100, 80, 82, 83, 100, 100, 80, image3)
salameche = Pokemon("salameche", 4, ["feu"], 0.6, 8.5, 39, 52, 43, 60, 50, 65, image4)
reptincel = Pokemon("reptincel", 5, ["feu"], 1.1, 19, 54, 68, 54, 80, 65, 80, image5)
dracaufeu = Pokemon("dracaufeu", 6, ["feu", "vol"], 1.7, 90.5, 78, 84, 78, 109, 85, 100, image6)
carapuce = Pokemon("carapuce", 7, ["eau"], 0.5, 9, 44, 48, 65, 50, 64, 43, image7)
carabaffe = Pokemon("carabaffe", 8, ["eau"], 1, 22.5, 59, 63, 80, 65, 80, 58, image8)
tortank = Pokemon("tortank", 9, ["eau"], 1.6, 85.5, 79, 83, 100, 85, 105, 78, image9)

        
pokemonlist = [bulbizarre, herbizarre, florizarre, salameche, reptincel, dracaufeu, carapuce, carabaffe, tortank]


def add_all():
    index = listbox.curselection()
    selection = listbox.get(index)
    for pok in pokemonlist:
        if pok.name == selection:
            label1.config(text=f"{pok.name} \n Pokemon numéro  {pok.number} \n Il mesure {pok.height}m et pèse {pok.weight}Kg \n Il est de type {pok.type} \n Statistiques : \n PV = {pok.hp}  \n Attaque = {pok.attack} \n Defense = {pok.defense} \n Attaque spéciale = {pok.spatt} \n Defense spéciale = {pok.spdef} \n Vitesse = {pok.speed} ")
            label2.config(image = pok.img)


def addnew():
    newname = champ_saisie.get()
    newnb = champ_saisie1.get()
    newtype = champ_saisie2.get()
    newh = champ_saisie3.get()
    neww = champ_saisie4.get()
    newhp = champ_saisie5.get()
    newatt = champ_saisie6.get()
    newdef = champ_saisie7.get()
    newspeatt = champ_saisie8.get()
    newspedef = champ_saisie9.get()
    newspeed = champ_saisie10.get()
    imagezzz = newname.capitalize()
    
    # bon la j'ai essayé de gérer les erreurs, ça bug avec try except et la c pas fou non plus nvm ça marche avec None!

    file_path = f"img/{imagezzz}.png"
    if os.path.exists(file_path):
        imagey= tk.PhotoImage(file=f"img/{imagezzz}.png")
        imagex = imagey.subsample(4, 4)
    else:
        imagex = None

    newname = Pokemon(newname, newnb, newtype, newh, neww, newhp, newatt, newdef, newspeatt, newspedef, newspeed, imagex)
    pokemonlist.append(newname)
    listbox.insert(tk.END,newname.name)

    #essai de sauvegarde dans 1 fichier texte (zone de code en travaux): 
    with open("sauvegardepokedex.txt", "r", encoding="utf-8") as f:
        fichier = open("sauvegardepokedex.txt", "a") 
        fichier.write(f"{newname.name}, {newname.number}, {newname.type}, {newname.height}, {newname.weight}, {newname.hp}, {newname.attack}, {newname.defense}, {newname.spatt}, {newname.spdef}, {newname.speed}, {newname.name}\n")

        lines = f.readlines()
    
        for line in lines:

            liste = line.split(", ")
            newname = liste[0]
            newnb = liste[1]
            newtype = liste[2]
            newh = liste[3]
            neww = liste[4]
            newhp = liste[5]
            newatt = liste[6]
            newdef = liste[7]
            newspeatt = liste[8]
            newspedef = liste[9]
            newspeed = liste[10]
            newnewname = liste[0].capitalize()
            file_path = f"img/{newnewname}.png"
            if os.path.exists(file_path):
                imageyy= tk.PhotoImage(file=f"img/{newnewname}.png")
                imagexx = imageyy.subsample(4, 4)
            else:
                imagex = None
            newname = Pokemon(newname, newnb, newtype, newh, neww, newhp, newatt, newdef, newspeatt, newspedef, newspeed, imagexx)
            pokemonlist.append(newname)
            listbox.insert(tk.END,newname.name)
#fin de zone en travaux
    champ_saisie.delete(0, tk.END)
    champ_saisie1.delete(0, tk.END)
    champ_saisie2.delete(0, tk.END)
    champ_saisie3.delete(0, tk.END)
    champ_saisie4.delete(0, tk.END)
    champ_saisie5.delete(0, tk.END)
    champ_saisie6.delete(0, tk.END)
    champ_saisie7.delete(0, tk.END)
    champ_saisie8.delete(0, tk.END)
    champ_saisie9.delete(0, tk.END)
    champ_saisie10.delete(0, tk.END)

def delete():
    selection = listbox.curselection()
    index = selection
    namedel = listbox.get(index)
    for pok in pokemonlist:
        if pok.name == namedel:
            pokemonlist.remove(pok)
            break
    listbox.delete(index)

listbox = tk.Listbox(fenetre, width=40)
for pok in pokemonlist:
    listbox.insert(tk.END,pok.name)
listbox.place(x=20, y=10)

label1 = tk.Label(fenetre)
label1.place(x=20, y=500)
label2 = tk.Label(fenetre)
label2.place(x=20, y=180)


bouton = tk.Button(fenetre, text="Afficher infos", command=add_all)
bouton.place(x=70, y=700)

labelname = tk.Label(fenetre, text="nom")
labelname.place(x=500, y=0)
champ_saisie = tk.Entry(fenetre)
champ_saisie.place(x=600, y=0)

labelnb = tk.Label(fenetre, text="numéro")
labelnb.place(x=500, y=30)
champ_saisie1 = tk.Entry(fenetre)
champ_saisie1.place(x=600, y=30)

labeltype = tk.Label(fenetre, text="type")
labeltype.place(x=500, y=60)
champ_saisie2 = tk.Entry(fenetre)
champ_saisie2.place(x=600, y=60)

labelheight = tk.Label(fenetre, text="taille")
labelheight.place(x=500, y=90)
champ_saisie3 = tk.Entry(fenetre)
champ_saisie3.place(x=600, y=90)

labelweight = tk.Label(fenetre, text="poids")
labelweight.place(x=500, y=120)
champ_saisie4 = tk.Entry(fenetre)
champ_saisie4.place(x=600, y=120)

labelhp = tk.Label(fenetre, text="pv")
labelhp.place(x=500, y=150)
champ_saisie5 = tk.Entry(fenetre)
champ_saisie5.place(x=600, y=150)

labelatt = tk.Label(fenetre, text="attaque")
labelatt.place(x=500, y=180)
champ_saisie6 = tk.Entry(fenetre)
champ_saisie6.place(x=600, y=180)

labeldef = tk.Label(fenetre, text="defense")
labeldef.place(x=500, y=210)
champ_saisie7 = tk.Entry(fenetre)
champ_saisie7.place(x=600, y=210)

labelspeatt = tk.Label(fenetre, text="attaque spéciale")
labelspeatt.place(x=500, y=240)
champ_saisie8 = tk.Entry(fenetre)
champ_saisie8.place(x=600, y=240)

labelspedef = tk.Label(fenetre, text="defense spéciale")
labelspedef.place(x=500, y=270)
champ_saisie9 = tk.Entry(fenetre)
champ_saisie9.place(x=600, y=270)

labelspeed = tk.Label(fenetre, text="vitesse")
labelspeed.place(x=500, y=300)
champ_saisie10 = tk.Entry(fenetre)
champ_saisie10.place(x=600, y=300)

bouton2 = tk.Button(fenetre, text="ajouter un nouveau pokemon", command = addnew)
bouton2.place(x=550, y=330)

labellogo = tk.Label(fenetre, image = logo1)
labellogo.place(x=450, y=430)

labeltrait = tk.Label(fenetre, text = "|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n")
labeltrait.place(x=402, y=0)

boutondel = tk.Button(fenetre, text="Supprimer pokemon", command=delete)
boutondel.place(x=570, y=360)


fenetre.geometry("804x768")
fenetre.mainloop()