import time
import random
import os

# Fonctions utilitaires
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Définition du personnage
class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.alive = True

    def take_damage(self, amount):
        self.hp -= amount
        delay_print(f"{self.name} a perdu {amount} PV.")
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            delay_print(f"{self.name} est vaincu...")

# Esquive simple avec obstacles
def dodge_phase():
    delay_print("ATTENTION ! Esquive les projectiles (o) !")
    bar = ["-", "-", "-", "-", "-"]
    for _ in range(10):
        pos = random.randint(0, 4)
        bar = ["-" for _ in range(5)]
        bar[pos] = "o"
        print("".join(bar))
        time.sleep(0.3)
    delay_print("Tu as survécu à l'attaque !\n")

# Système de combat
def fight_loop():
    player_hp = 20
    enemy = Enemy("Sans", 15)

    while enemy.alive:
        delay_print(f"\nHP Joueur : {player_hp} | {enemy.name} : {enemy.hp} PV")
        print("1. Attaquer")
        print("2. Épargner")
        print("3. Parler")
        choice = input("> ")

        if choice == "1":
            dmg = random.randint(3, 6)
            enemy.take_damage(dmg)
        elif choice == "2":
            delay_print(f"Tu essaies d'épargner {enemy.name}...")
            if enemy.hp < 5:
                delay_print(f"{enemy.name} accepte ton pardon.")
                enemy.alive = False
            else:
                delay_print(f"{enemy.name} n'est pas prêt à être épargné.")
        elif choice == "3":
            delay_print(f"Tu parles à {enemy.name}. Il ne répond pas.")
        else:
            delay_print("Commande invalide.")

        if enemy.alive:
            dodge_phase()
            hit = random.randint(1, 3)
            player_hp -= hit
            delay_print(f"{enemy.name} t'a infligé {hit} dégâts.")
            if player_hp <= 0:
                delay_print("Tu es mort...")
                return

    delay_print("Combat terminé. Tu as gagné ou fait preuve de miséricorde.")

if __name__ == "__main__":
    clear()
    delay_print("Un ennemi approche...\n")
    fight_loop()
