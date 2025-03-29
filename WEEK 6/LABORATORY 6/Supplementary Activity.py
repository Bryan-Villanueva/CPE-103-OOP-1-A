import random
from abc import ABC


class Character(ABC):
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.max_hp = hp
        self.wins = 0

    def special_attack(self):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def add_win(self):
        self.wins += 1


class Novice(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=10)

    def special_attack(self):
        return self.attack * 1.2


class Swordsman(Character):
    def __init__(self, name):
        super().__init__(name, hp=120, attack=15)

    def special_attack(self):
        return self.attack * 1.5


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=90, attack=20)

    def special_attack(self):
        return self.attack * 1.8
        if random.random() < 0.2:
            return 0
        return self.attack * 1.8


class Magician(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, attack=25)

    def special_attack(self):
        return self.attack * 2.0

    def heal(self, amount):
        super().heal(amount * 1.5)


class Boss(Character):
    def __init__(self, name):
        super().__init__(name, hp=200, attack=20)

    def special_attack(self):
        return self.attack * 1.8


class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.game_mode = None

    def select_game_mode(self):
        print("Select Game Mode:")
        print("1. Single Player (vs Computer)")
        print("2. Player vs Player")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            self.game_mode = "single"
            player_name = input("Enter your name: ")
            self.player1 = Novice(player_name)
            self.player2 = Boss("Monster")
        elif choice == "2":
            self.game_mode = "pvp"
            self.setup_pvp_game()
        else:
            print("Invalid choice. Please try again.")
            self.select_game_mode()

    def setup_pvp_game(self):
        print("\nPlayer 1 Character Selection:")
        self.player1 = self.select_character(1)
        print("\nPlayer 2 Character Selection:")
        self.player2 = self.select_character(2)

    def select_character(self, player_num):
        name = input(f"Enter Player {player_num} name: ")
        print("Select your class:")
        print("1. Novice (HP: 100, Attack: 10)")
        print("2. Swordsman (HP: 120, Attack: 15)")
        print("3. Archer (HP: 90, Attack: 20)")
        print("4. Magician (HP: 80, Attack: 25)")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            return Novice(name)
        elif choice == "2":
            return Swordsman(name)
        elif choice == "3":
            return Archer(name)
        elif choice == "4":
            return Magician(name)
        else:
            print("Invalid choice. Defaulting to Novice.")
            return Novice(name)

    def determine_first_attacker(self):
        return random.choice([self.player1, self.player2])

    def play_match(self):
        attacker, defender = self.determine_first_attacker(), self.player2 if self.determine_first_attacker() == self.player1 else self.player1

        print(f"\n{attacker.name} goes first!")

        while self.player1.is_alive() and self.player2.is_alive():
            print(f"\n{attacker.name}'s turn (HP: {attacker.hp})")
            print(f"{defender.name}'s HP: {defender.hp}")

            print("1. Normal Attack")
            print("2. Special Attack")
            print("3. Heal (restores 20% of max HP)")

            choice = input("Choose your action (1-3): ")

            if choice == "1":
                damage = attacker.attack
                defender.take_damage(damage)
                print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
            elif choice == "2":
                damage = attacker.special_attack()
                defender.take_damage(damage)
                print(f"{attacker.name} uses special attack on {defender.name} for {damage} damage!")
            elif choice == "3":
                heal_amount = int(attacker.max_hp * 0.2)
                attacker.heal(heal_amount)
                print(f"{attacker.name} heals for {heal_amount} HP!")
            else:
                print("Invalid choice. Defaulting to normal attack.")
                damage = attacker.attack
                defender.take_damage(damage)
                print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

            if not defender.is_alive():
                break

            attacker, defender = defender, attacker

        self.declare_winner()

    def declare_winner(self):
        if self.player1.is_alive():
            winner = self.player1
            loser = self.player2
        else:
            winner = self.player2
            loser = self.player1

        print(f"\n{loser.name} has been defeated!")
        print(f"{winner.name} wins the match!")

        winner.add_win()
        print(f"{winner.name}'s total wins: {winner.wins}")

        if self.game_mode == "single" and winner == self.player1:
            if winner.wins >= 2 and isinstance(winner, Novice):
                self.promote_novice()

    def promote_novice(self):
        print("\nCongratulations! You've won 2 matches as a Novice.")
        print("You can now choose a new class:")
        print("1. Swordsman (HP: 120, Attack: 15)")
        print("2. Archer (HP: 90, Attack: 20)")
        print("3. Magician (HP: 80, Attack: 25)")

        choice = input("Enter your choice (1-3): ")
        name = self.player1.name

        if choice == "1":
            self.player1 = Swordsman(name)
        elif choice == "2":
            self.player1 = Archer(name)
        elif choice == "3":
            self.player1 = Magician(name)
        else:
            print("Invalid choice. Defaulting to Swordsman.")
            self.player1 = Swordsman(name)

        self.player1.wins = 2
        print(f"\n{self.player1.name} is now a {self.player1.__class__.__name__}!")

    def play_again(self):
        choice = input("\nDo you want to play again? (y/n): ").lower()
        return choice == 'y'

    def start(self):
        print("Welcome to the Battle Game!")

        while True:
            self.select_game_mode()
            self.play_match()

            if not self.play_again():
                print("\nThanks for playing!")
                break


if __name__ == "__main__":
    game = Game()
    game.start()