import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
# Un pokedex avec les fonctionnalités suivantes :
    # Afficher les pokemons
        # Nom
        # Type
        # Image
    # Créer un nouveau pokemon
        # Nom
        # Type
        # Image
    # Supprimer un pokemon
        # Message de sécurité avant suppression
    # Modifier un pokemon
        # Nom
        # Type
        # Image
    # Données persistantes (qui restent même après fermeture de l'app)
screen = tk.Tk()
screen.title("Pokedex")
screen.geometry("640x480")



# ----------------------------------------------------
# Pokemon class : data managment + persistence
# ----------------------------------------------------
class Pokemon:
    def __init__(self, name_pokemon, type_pokemon, image_pokemon):
        self.name_pokemon = name_pokemon
        self.type_pokemon = type_pokemon
        self.image_pokemon = image_pokemon

pokedex = []

file_path = 'pokedex.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    el = line.split(", ")
    name_pokemon = el[0]
    type_pokemon = el[1]
    image_pokemon = el[2]
    pokedex.append(Pokemon(name_pokemon, type_pokemon, image_pokemon))

# pokedex = [
#     Pokemon("Abo", "Poison", "./img/Abo.png"),
#     Pokemon("Abra", "Psy", "./img/Abra.png"),
#     Pokemon("Akwakwak", "Eau", "./img/Akwakwak.png"),
# ]

def show_details():
    index = list_pokemon.curselection()
    if index:
        pokemon = pokedex[index[0]]
        messagebox.showinfo(f"Détails du pokémon {pokemon.name_pokemon}", f"Nom : {pokemon.name_pokemon}\nType : {pokemon.type_pokemon}\n Image : {pokemon.image_pokemon}")
    else:
        messagebox.showwarning("Aucune sélection", "Aucun Pokemon sélectionné.")

def add_pokemon():
    pokemon_name = entry_name.get()
    pokemon_type = entry_type.get()
    pokemon_image = entry_image.get()
    # Récupérer le pokedex et ajouter un nouveau pokemon grâce à append
    pokedex.append(Pokemon(pokemon_name, pokemon_type, pokemon_image))
    # Mettre à jour la liste des pokemons dans la listbox
    list_pokemon.insert(tk.END, pokemon_name)
    # Ajout du pokemon dans le fichier
    file = open("pokedex.txt", "a", encoding="utf-8")
    file.write(f"{pokemon_name}, {pokemon_type}, {pokemon_image}\n")
    file.close()
    messagebox.showinfo("Pokemon ajouté", "Le Pokemon a été ajouté avec succès.")

def delete_pokemon():
    index = list_pokemon.curselection()
    if index:
        confirm = messagebox.askyesno("Confirmation", f"Es-tu sûr de vouloir supprimer le pokemon ?")

        if not confirm:
            return

        list_pokemon.delete(index)
        # Index de l'élément à supprimer dans le fichier texte
        index = index[0]
        # Supprimer directement depuis pokedex
        pokedex.pop(index)
        # On met à jour le fichier pokedex.txt en parcourant le tableau pokedex et en faisant un W
        with open("pokedex.txt", "w", encoding="utf-8") as file:
            for p in pokedex:
                file.write(f"{p.name_pokemon}, {p.type_pokemon}, {p.image_pokemon}")
        messagebox.showinfo("Suppression", "Pokemon supprimé avec succès")
    else:
        messagebox.showwarning("Aucune sélection", "Aucun Pokemon sélectionné.")


# ----------------------------------------------------
# Interface
# ----------------------------------------------------
list_pokemon = tk.Listbox(screen)
for pokemon in pokedex:
    list_pokemon.insert(tk.END, pokemon.name_pokemon)
list_pokemon.pack()

show_button = tk.Button(screen, text="Afficher les détails", command=show_details)
show_button.pack()

delete_button = tk.Button(screen, text="Supprimer le Pokemon", command=delete_pokemon)
delete_button.pack()

# Formulaire d'ajout de Pokemon
label_name = tk.Label(screen, text="Nom du Pokemon : ")
label_name.pack()
entry_name = tk.Entry(screen)
entry_name.pack()

label_type = tk.Label(screen, text="Type du Pokemon : ")
label_type.pack()
entry_type = tk.Entry(screen)
entry_type.pack()

label_image = tk.Label(screen, text="Lien vers l'image : ")
label_image.pack()
entry_image = tk.Entry(screen)
entry_image.pack()

add_button = tk.Button(screen, text="Ajouter le Pokemon", command=add_pokemon)
add_button.pack()

screen.mainloop()