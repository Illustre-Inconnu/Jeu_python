import random

# Fonction pour gérer l'attaque du héros ou du monstre
def gestion_attaque(vie, attaque):
    if probabilite_attaquer():
        vie -= attaque
        print("Le monstre est touché !")
    else:
        print("Le monstre esquive l'attaque !")
    return vie

# Fonction pour gérer le soin du héros
def gestion_soin(vie, soin):
    vie += soin
    print("Vous vous soignez.")
    return vie

# Fonction pour déterminer la probabilité d'une attaque réussie
def probabilite_attaquer():
    probabilite_rater_hero = 0.2
    probabilite_rater_monstre = 0.3
    
    attaque_hero_reussie = random.random() > probabilite_rater_hero
    attaque_monstre_reussie = random.random() > probabilite_rater_monstre
    
    if attaque_hero_reussie:
        print("Attaque du héros réussie !")
    else:
        print("Attaque du héros a échoué !")
    
    if attaque_monstre_reussie:
        print("Attaque du monstre réussie !")
    else:
        print("Attaque du monstre a échoué !")

    return attaque_hero_reussie and attaque_monstre_reussie

# Fonction pour déterminer la probabilité d'une fuite réussie
def probabilite_fuite():
    probabilite_fuite_hero = 0.25
    fuite_hero_reussi = random.random() > probabilite_fuite_hero
    
    if fuite_hero_reussi:
        print("La fuite a réussi !")
    else:
        print("La fuite a échoué !")
    
    return fuite_hero_reussi

# Initialisation des variables
hero_nom = input("Nommer votre personnage : ")
hero_point_vie = 100
hero_point_attaque = 10
hero_point_soin = 5

monstre_nom = "Monstre"
monstre_point_vie = 100
monstre_point_attaque = 7.5

run = True
while run:
    MIN = 1
    MAX = 3

    print("Taper 1 : pour attaquer")
    print("Taper 2 : pour vous soigner")
    print("Taper 3 : pour prendre la fuite")
    
    choix_utilisateur = int(input("Quel est votre choix ? : "))

    if choix_utilisateur == 1:
        monstre_point_vie = gestion_attaque(monstre_point_vie, hero_point_attaque)
    elif choix_utilisateur == 2:
        hero_point_vie = gestion_soin(hero_point_vie, hero_point_soin)
    elif choix_utilisateur == 3:
        if probabilite_fuite():
            break  # Utilisez break pour sortir de la boucle
    else:
        print(f"Choix invalide. Veuillez taper un nombre compris entre {MIN} et {MAX}.")

    hero_point_vie = gestion_attaque(hero_point_vie, monstre_point_attaque)

    print(f"Vie du héros : {hero_point_vie}")
    print(f"Vie du monstre : {monstre_point_vie}")

    if hero_point_vie <= 0:
        print("Vous avez perdu ! Le monstre vous a vaincu.")
        run = False
    elif monstre_point_vie <= 0:
        print("Félicitations ! Vous avez vaincu le monstre.")
        run = False
