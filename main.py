#henrique vera
#exercise poo
#2023-01-17



import random


def dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice_rolls = [dice1, dice2, dice3, dice4]
    highest_3 = sum(sorted(dice_rolls, reverse = True)[:3])
    return highest_3

class NPC:
    def __init__(self):
        self.force = dice()
        self.agilite = dice()
        self.constitution = dice()
        self.inteligence = dice()
        self.sagesse = dice()
        self.charisme = dice()
        self.class_darmure = random.randint(1, 12)
        self.nom = str
        self.race = str
        self.espece = str
        self.point_de_vie = random.randint(1, 20)
        self.profession = str

    def afficher_caracteristique(self):
        print(self.force, self.agilite, self.constitution, self.intelligence, self.self.inteligence, self.self.sagesse, self.charisme, self.class_darmure, self.nom, self.race, self.espece, self.point_de_vie, self.profession)


class KOBALD(NPC):
    def __init__(self):
        super().__init__ ()
    def attaque(self, cible):
        return
    def subir_dommage(self, dommage):
        return

class hero(NPC):
    def __init__(self):
        super().__init__ ()
    def attaque(self, cible):
        return
    def subir_dommage(self, dommage):
        return
