class Circle:
    def __init__(self, radius, color):
        self.radius = radius 
        self._color = color  
        self._pi = 3.14159 


    def getColor(self):
        return self._color


    def getCircum(self):
        return 2 * self._pi * self.radius


class Player:
    def __init__(self, name):
        self.name = name  
        self.inventory = {}  
        self.money = 0 
        self.health = 100  


    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"Added {quantity} of {item} to inventory.")


    def remove_item(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            print(f"Removed {quantity} of {item} from inventory.")
            if self.inventory[item] == 0:
                del self.inventory[item]
        else:
            print(f"Cannot remove {quantity} of {item}. Not enough in inventory.")


    def add_money(self, amount):
        self.money += amount
        print(f"Added {amount} money. Current balance: {self.money}")


    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"Spent {amount} money. Current balance: {self.money}")
        else:
            print("Not enough money.")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("Player is dead.")
        else:
            print(f"Player took {damage} damage. Health: {self.health}")


    def heal(self, amount):
        if self.health > 0:
            self.health += amount
            if self.health > 100:
                self.health = 100
            print(f"Player healed by {amount}. Health: {self.health}")
        else:
            print("Player is dead. Cannot heal.")


class Patrick:
    def __init__(self, name):
        self.name = name 
        self.skillset = []  
        self.energy = 100  
        self.performance_score = 0  
        self.mood = 'neutral'  


    def learn_skill(self, skill):
        self.skillset.append(skill)
        print(f"{self.name} learned {skill}. Skills: {self.skillset}")


    def perform_task(self, task):
        if self.energy > 10:
            self.energy -= 10
            self.performance_score += 10
            print(f"{self.name} performed {task}. Energy left: {self.energy}. Score: {self.performance_score}")
        else:
            print(f"{self.name} is too tired to perform {task}.")


    def recharge(self):
        self.energy = 100
        print(f"{self.name} is fully recharged.")


    def adjust_mood(self):
        if self.performance_score > 50:
            self.mood = 'happy'
        elif self.performance_score < 20:
            self.mood = 'sad'
        else:
            self.mood = 'neutral'
        print(f"{self.name}'s mood is now {self.mood}.")


    def display_status(self):
        print(f"Me: {self.name}, Skills: {self.skillset}, Energy: {self.energy}, Performance Score: {self.performance_score}, Mood: {self.mood}")
