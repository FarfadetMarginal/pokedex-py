import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()


label1 = tk.Label(fenetre, text="0")
label1.grid(row=1, column = 0)

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

def afficher_tout():
    index = listbox.curselection()
    selection = listbox.get(index)
    for pok in pokemonlist:
        if pok.name == selection:
            label1.config(text=f"{pok.name} \n Pokemon numéro  {pok.number} \n Il mesure {pok.height}m et pèse {pok.weight}Kg \n Il est de type {pok.type} \n Statistiques : \n PV = {pok.hp}  \n Attaque = {pok.attack} \n Defense = {pok.defense} \n Attaque spéciale = {pok.spatt} \n Defense spéciale = {pok.spdef} \n Vitesse = {pok.speed} ")
            label2.config(image = pok.img)


def ajout():
    newname = champ_saisie.get()
    newnb = champ_saisie1.get()
    newtype = champ_saisie2.get()
    newh = champ_saisie3.get()
    neww = champ_saisie4.get()
    newhp = champ_saisie5.get
    newatt = champ_saisie6.get()
    newdef = champ_saisie7.get()
    newspeatt = champ_saisie8.get()
    newspedef = champ_saisie9.get()
    newspeed = champ_saisie10.get()
    imagex = 0

    pokemonlist.append(newname)
    newname = Pokemon(newname, newnb, newtype, newh, neww, newhp, newatt, newdef, newspeatt, newspedef, newspeed, imagex)
    listbox.insert(tk.END,newname.name)
    print(pokemonlist)
    print(newname.name)
    print(newname.attack)



listbox = tk.Listbox(fenetre, width=40)
for pok in pokemonlist:
    listbox.insert(tk.END,pok.name)
listbox.grid(row=0, column = 0)

label1 = tk.Label(fenetre)
label1.grid(row=1, column = 0)
label2 = tk.Label(fenetre)
label2.grid(row=2, column = 0)


bouton = tk.Button(fenetre, text="infos", command=afficher_tout)
bouton.grid(row=3, column = 0)

labelname = tk.Label(fenetre, text="nom")
labelname.grid(row=0, column = 1)
champ_saisie = tk.Entry(fenetre)
champ_saisie.grid(row=1, column = 1)

labelnb = tk.Label(fenetre, text="numéro")
labelnb.grid(row=2, column = 1)
champ_saisie1 = tk.Entry(fenetre)
champ_saisie1.grid(row=3, column = 1)

labeltype = tk.Label(fenetre, text="type")
labeltype.grid(row=4, column = 1)
champ_saisie2 = tk.Entry(fenetre)
champ_saisie2.grid(row=5, column = 1)

labelheight = tk.Label(fenetre, text="taille")
labelheight.grid(row=6, column = 1)
champ_saisie3 = tk.Entry(fenetre)
champ_saisie3.grid(row=7, column = 1)

labelweight = tk.Label(fenetre, text="poids")
labelweight.grid(row=8, column = 1)
champ_saisie4 = tk.Entry(fenetre)
champ_saisie4.grid(row=9, column = 1)

labelhp = tk.Label(fenetre, text="pv")
labelhp.grid(row=10, column = 1)
champ_saisie5 = tk.Entry(fenetre)
champ_saisie5.grid(row=11, column = 1)

labelatt = tk.Label(fenetre, text="attaque")
labelatt.grid(row=12, column = 1)
champ_saisie6 = tk.Entry(fenetre)
champ_saisie6.grid(row=13, column = 1)

labeldef = tk.Label(fenetre, text="defense")
labeldef.grid(row=14, column = 1)
champ_saisie7 = tk.Entry(fenetre)
champ_saisie7.grid(row=15, column = 1)

labelspeatt = tk.Label(fenetre, text="attaque spéciale")
labelspeatt.grid(row=16, column = 1)
champ_saisie8 = tk.Entry(fenetre)
champ_saisie8.grid(row=17, column = 1)

labelspedef = tk.Label(fenetre, text="defense spéciale")
labelspedef.grid(row=18, column = 1)
champ_saisie9 = tk.Entry(fenetre)
champ_saisie9.grid(row=19, column = 1)

labelspeed = tk.Label(fenetre, text="vitesse")
labelspeed.grid(row=20, column = 1)
champ_saisie10 = tk.Entry(fenetre)
champ_saisie10.grid(row=21, column = 1)

bouton2 = tk.Button(fenetre, text="ajouter un nouveau pokemon", command = ajout)
bouton2.grid(row=22, column = 1)


fenetre.geometry("524x768")
fenetre.mainloop()