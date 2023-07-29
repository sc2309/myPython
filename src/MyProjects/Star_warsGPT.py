import random

class Character:
    def __init__(self, name, health, saber_head, saber_hand, saber_body, saber_leg):
        self.name = name
        self.health = health
        self.saber_head = saber_head
        self.saber_hand = saber_hand
        self.saber_body = saber_body
        self.saber_leg = saber_leg

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        return f"{self.name}'s health: {self.health}"

class KyloRen(Character):
    def __init__(self):
        super().__init__("Kylo Ren", health=500, saber_head=50, saber_hand=26, saber_body=75, saber_leg=20)

class Malgus(Character):
    def __init__(self):
        super().__init__("Darth Malgus", health=550, saber_head=100, saber_hand=26, saber_body=120, saber_leg=20)

# Add other character classes in a similar way...

class StarJediFighters:
    def __init__(self):
        self.player1 = None
        self.player2 = None

    def character_selection(self):
        print("Welcome to Star Jedi Fighters!")
        name = input("Please enter a name: ")
        print("\nYour opponent will not be automatic")
        print("Choose your character as P1\nsometimes a character may undergo aggression and may cause more damage than normal")

        character_list = {
            "Kylo Ren": KyloRen(),
            "Darth Malgus": Malgus(),
        }

        print("\nHere you can select a character for yourself:")
        for character in character_list:
            print(f"{character} - Health: {character_list[character].health}")

        player1_choice = input().strip()
        while player1_choice not in character_list:
            print("Invalid character choice. Please select again.")
            player1_choice = input().strip()

        print("\nLet your opponent select their character as P2:")
        player2_choice = input().strip()
        while player2_choice not in character_list or player2_choice == player1_choice:
            if player2_choice == player1_choice:
                print("Character already chosen by P1. Please select another character.")
            else:
                print("Invalid character choice. Please select again.")
            player2_choice = input().strip()

        self.player1 = character_list[player1_choice]
        self.player2 = character_list[player2_choice]

        print("\nGame starting...")

    def fight(self):
        turn = 1
        while self.player1.is_alive() and self.player2.is_alive():
            if turn % 2 != 0:
                self.player1_attack(self.player1, self.player2)
            else:
                self.player2_attack(self.player2, self.player1)
            turn += 1

    def player1_attack(self, attacker, defender):
        move = input("\nSelect your move P1:\n"
                     "lightsaber strike on head(lsh)\n"
                     "lightsaber strike on hand(lshand)\n"
                     "lightsaber strike on leg(lsl)\n"
                     "lightsaber strike on body(lsb)\n").strip()

        if move == 'lsh':
            defender.take_damage(attacker.saber_head)
        elif move == 'lshand':
            defender.take_damage(attacker.saber_hand)
        elif move == 'lsl':
            defender.take_damage(attacker.saber_leg)
        elif move == 'lsb':
            defender.take_damage(attacker.saber_body)
        else:
            print('Invalid move. You missed.')

        print(defender)
        if not defender.is_alive():
            print(f"{defender.name} lost the game")
            self.exit_game()

    def player2_attack(self, attacker, defender):
        move = input("\nSelect your move P2:\n"
                     "lightsaber strike on head(lsh)\n"
                     "lightsaber strike on hand(lshand)\n"
                     "lightsaber strike on leg(lsl)\n"
                     "lightsaber strike on body(lsb)\n").strip()

        if move == 'lsh':
            defender.take_damage(attacker.saber_head)
        elif move == 'lshand':
            defender.take_damage(attacker.saber_hand)
        elif move == 'lsl':
            defender.take_damage(attacker.saber_leg)
        elif move == 'lsb':
            defender.take_damage(attacker.saber_body)
        else:
            print('Invalid move. You missed.')

        print(defender)
        if not defender.is_alive():
            print(f"{defender.name} lost the game")
            self.exit_game()

    @staticmethod
    def exit_game():
        print("\nThanks for playing! May the force be with you.")
        exit()

if __name__ == "__main__":
    game = StarJediFighters()
    game.character_selection()
    game.fight()
