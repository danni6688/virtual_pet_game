import json
import os
import random

class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 25
        self.cleanness = 30
        self.energy = 60
        self.age = 0
        self.chat = 0
        self.coins = 100
        self.signed = False
        self.played_game = False
    
    def feeding(self):
        if self.coins < 8:
            print("Not enough coins to feed!")
            return
        print("\nChoose what you want {self.name} to eat: ")
        print("1.Dog food (10 coins, +10 hunger)")
        print("2.Steak (15 coins, +20 hunger +5 pleasure)")
        print("3.Carrot (8 coins, +8 hunger)")
        food = input("choose 1-3: ")
        if food == "1" and self.coins >= 10:
            self.hunger = min(100, self.hunger + 10)
            self.coins -= 10
        elif food == "2" and self.coins >= 15:
            self.hunger = min(100, self.hunger + 15)
            self.happiness = min(60, self.happiness + 5)
            self.coins -= 15
        elif food == "3" and self.coins >= 8:
            self.hunger = min(100,self.hunger + 8)
            self.coins -= 8
        else:
            print("Invalid input or insufficient gold coins, feeding fails.")
        self.energy = max(0, self.energy - 5)

    def resting(self):
        print(f"\n{self.name} took a nap.")
        self.energy = min(100, self.energy + random.randint(15, 25))
        self.hunger = max(0, self.hunger - 5)

    def washing(self):
        if self.coins < 8:
            print("Not enough coins to take a bath!")
            return
        print(f"\n{self.name} is going to take a shower.")
        self.cleanness = min(100, self.cleanness + random.randint(20, 30))
        self.happiness = max(0, self.happiness - 5)
        self.coins -= 8

    def playing(self):
        print(f"\nWhat do you want to play with {self.name}?")
        print("1.Throw the ball ( +15 pleasure  -10 energy)")
        print("2.Walking ( +10 pleasure  -5 energy)")
        print("3.Watching TV ( +5 pleasure -2 energy)")
        play = input("choose 1-3: ")
        if play == "1":
            self.happiness = min(100, self.happiness + 15)
            self.energy = max(0, self.energy - 10)
        elif play == "2":
            self.happiness = min(100, self.happiness + 10)
            self.energy = max(0, self.energy - 5)
        elif play == "3":
            self.happiness = min(100, self.happiness + 5)
            self.energy = max(0, self.energy - 2)
        else:
            print("Input error, walk is selected by default.")
            self.happiness = min(100, self.happiness + 10)
            self.energy = max(0, self.energy - 5)
        self.cleanness = max(0, self.cleanness - 5)
    
    def talking(self):
        talk = [
            f"{self.name}: Woof woof! Did you forget to feed me again?",
            f"{self.name}: You smile so softly today~",
            f"{self.name}: Am I the cutest {self.species} in the world!",
            f"{self.name}: Where did that ball go yesterday? I still want to play!",
            f"{self.name}: You're my only friend."
        ]
        if self.chat >= 5:
            print(f"{self.name}: You talk a lot hahaha")
        else:
            print(random.choice(talk))
        self.chat += 1
        self.happiness = min(100, self.happiness + 2)

    def sign_daily(self):
        if self.signed:
            print("You've already checked in today. Come back tomorrow!")
        else:
            coin = 15
            print(f"Signed in successfully! Get {coin} coins!")
            self.coins += coin
            self.signed = True

    def event_random(self):
        event = random.randint(1, 10)
        if event == 1:
            print(f"Accident! {self.name} Accidentally stepped in a puddle and got soaked.")
            self.cleanness = max(0, self.cleanness - 15)
            self.happiness = max(0, self.happiness - 5)
        elif event == 2:
            print(f"Lucky moment! You picked up some gold coins!")
            gain = random.randint(5, 15)
            self.coins += gain
            print(f"Gain {gain} coins! Current coins: {self.coins}")

    def gaming(self):
        if self.played_game:
            print("You've played the game today, try again tomorrow!")
            return
        print("\nGuessing Game (Win coins)")
        number = random.randint(1, 5)
        guess_number = input("I've prepared a number between 1 and 5 for you to guess:")
        try:
            if int(guess_number) == number:
                print("Guess correctly! Reward 10 coins!")
                self.coins += 10
            else:
                print(f"Unfortunately, it's {number}, no guesses.")
        except:
            print("Please enter a valid number!")
        self.played_game = True

    def passed_time(self):
        self.age += 1
        self.signed = False
        self.played_game = False
        self.hunger = max(0, self.hunger - 5)
        self.energy = max(0, self.energy - 3)
        self.cleanness = max(0, self.cleanness - 4)
        self.happiness = max(0, self.happiness - 2)
        self.event_random()

    def gameover(self):
        if self.hunger <= 0 or self.energy <= 0 or self.cleanness <= 0 or self.happiness <= 0:
            print(f"Oops! {self.name}'s status is so bad, it's run away from home ...")
            return True
        return False

    def birthday(self):
        if self.age > 0 and self.age % 7 == 0:
            print(f"Today is {self.name}'s virtual birthday! You've been together for {self.age} for days!")
            self.coins += 20
            print(f"Birthday bonus: +20 coins! Current Coins: {self.coins}")

    def __str__(self):
        return(f"\nStatus Report - {self.name}\n"
               + "-" * 35 + "\n"
               + f"{'Species':15}: {self.species}\n"
               + f"{'Age (days)':15}: {self.age}\n"
               + f"{'Hunger':15}: {self.hunger}/100\n"
               + f"{'Energy':15}: {self.energy}/100\n"
               + f"{'Cleanliness':15}: {self.cleanness}/100\n"
               + f"{'Happiness':15}: {self.happiness}/100\n"
               + f"{'Coins':15}: {self.coins}\n"
               + "-" * 35)

def save_pet(pet, filename):
    with open(filename, "w") as f:
        json.dump(pet.__dict__, f)
    print("Saved!")

def load_pet(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    pet = Pet(data["name"], data["species"])
    pet.__dict__.update(data)
    print("Save loaded!")
    return pet

def game_starting():
    print("Welcome to Virtual Petting Zoo!")
    filename = input("Enter your save file name (e.g. coco.json): ")
    if os.path.exists(filename):
        already_resume = input(f"Found {filename} Continue? (yes/no): ")
        if already_resume.lower() == "yes":
            my_pet = load_pet(filename)
        else:
            pet_name = input("Please name your pet:")
            pet_species = input("What is your pet? (dog/cat/rabbit/customizable animals):")
            my_pet = Pet(pet_name, pet_species)
    else:
        pet_name = input("Please name your pet:")
        pet_species = input("What is your pet? (dog/cat/rabbit/customizable animals):")
        my_pet = Pet(pet_name, pet_species)
    
    count = 0
    threshold = random.randint(3, 6)

    while True:
        print(my_pet)
        print("\nWhat you want to do:")
        print("1. Feeding")
        print("2. Playing")
        print("3. Resting")
        print("4. Cleaning")
        print("5. Chatting")
        print("6. Signing")
        print("7. Small game")
        print("8. Exit the game")
        choice = input("Please enter choices (1-8):")

        if choice == "1":
            my_pet.feeding()
        elif choice == "2":
            my_pet.playing()
        elif choice == "3":
            my_pet.resting()
        elif choice == "4":
            my_pet.washing()
        elif choice == "5":
            my_pet.talking()
        elif choice == "6":
            my_pet.sign_daily()
        elif choice == "7":
            my_pet.gaming()
        elif choice == "8":
            save_pet(my_pet, filename)
            print(f"\nThank you for taking care of {my_pet.name}, bye-bye.")
            break
        else:
            print("Invalid entry")
            continue

        count += 1
        if count >= threshold:
            my_pet.passed_time()
            my_pet.birthday()
            count = 0
            threshold = random.randint(3, 6)
        
        if my_pet.gameover():
            break

if __name__ == "__main__":
    game_starting()


    





