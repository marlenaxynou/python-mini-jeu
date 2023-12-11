# Fonction pour afficher la carte
def display_map(m, d):
    for i in m:
        for j in i:
            print(d[j], end="")
        print()

# Exemple de la fonction display_map avec la carte et le dictionnaire donnés
map_data = [[0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0]]
dico = {0: ' ', 1: '#'}
# display_map(map_data, dico)

# Fonction pour créer un personnage
def create_perso(depart):
    return {"char": "🤠", "x": depart[0], "y": depart[1], "score": 0}

# Exemple de la fonction create_perso
personnage = create_perso((0, 0))
print(personnage)  # Vérifier si la clé "score" a été ajoutée

# Fonction pour mettre à jour la position du personnage
def update_p(letter, p, m):
    if letter == "z" and p["y"] > 0 and m[p["y"] - 1][p["x"]] != 1:  # Haut
        p["y"] -= 1
    elif letter == "s" and p["y"] < len(m) - 1 and m[p["y"] + 1][p["x"]] != 1:  # Bas
        p["y"] += 1
    elif letter == "q" and p["x"] > 0 and m[p["y"]][p["x"] - 1] != 1:  # Gauche
        p["x"] -= 1
    elif letter == "d" and p["x"] < len(m[0]) - 1 and m[p["y"]][p["x"] + 1] != 1:  # Droite
        p["x"] += 1
import random
# Fonction pour créer des objets
def create_objects(nb_objects, m, player_position):
    objects = set()

    for _ in range(nb_objects):
        while True:
            x = random.randint(0, len(m[0]) - 1)
            y = random.randint(0, len(m) - 1)

            # Vérifie que la position générée n'est pas occupée par le joueur ou un autre objet
            if (x, y) != player_position and m[y][x] == 0 and (x, y) not in objects:
                objects.add((x, y))
                break

    return objects

# Fonction pour mettre à jour les objets et le score du personnage
def update_objects(p, objects, m):
    position = (p["x"], p["y"])

    if position in objects:
        objects.remove(position)
        p["score"] += 1
        print("Objet ramassé! Score: {}".format(p["score"]))
    return objects

# Exemple de la fonction update_objects
objects_set = {(1, 1), (2, 2), (3, 3)}  # Exemple d'ensemble d'objets
update_objects(personnage, objects_set, map_data)
print(personnage)  # Vérifier si le score a été mis à jour

# Fonction pour afficher la carte, le personnage et les objets
def display_map_and_char(m, d, p, objects):
    print("Map:")
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i, j) == (p["y"], p["x"]):
                print(p["char"], end="")
            elif (j, i) in objects:
                print("🍬", end="")
            else:
                print(d[m[i][j]], end="")
        print()

    print("\nScore: {}".format(p["score"]))

# Exemple de la fonction display_map_and_char
map_size = (4, 5)
map_data = [[0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]
dico = {0: ' ', 1: '#'}
personnage = create_perso((0, 0))
objects_set = create_objects(3, map_data, (personnage["x"], personnage["y"]))

# Boucle principale du jeu
while True:
    display_map_and_char(map_data, dico, personnage, objects_set)

    direction = input("Quel déplacement ? (z: haut, q: gauche, s: bas, d: droite, stop: arrêter) ")

    if direction == "stop":
        break

    if direction in ["z", "q", "s", "d"]:
        update_p(direction, personnage, map_data)
        update_objects(personnage, objects_set, map_data)
        display_map_and_char(map_data, dico, personnage, objects_set)  
    else:
        print("Erreur : Entrée invalide. Utilisez z, q, s, ou d pour vous déplacer.")

    if not objects_set:
        print("Tous les objets ont été ramassés!")
        break
