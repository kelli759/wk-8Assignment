 # PLAYERS UNKNOWN BATTLE GROUND (PUBG)
class Player:
    """Player class"""

    def __init__(self, name, health, ammo):
        """
        Initializes a new player object.

        :param name: Player's name
        :param health: Player's health
        :param ammo: Player's ammo
        """
        self.name = name
        self.health = health
        self.ammo = ammo

    def display_info(self):
        """Displays the player's information."""
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Ammo: {self.ammo}")

    def shoot(self):
        """Shoots at an enemy."""
        print(f"{self.name} shot at an enemy.")

    def take_damage(self, damage):
        """Takes damage from an enemy."""
        self.health -= damage
        print(f"{self.name} took {damage} damage.")

    def heal(self, amount):
        """Heals the player by a specified amount."""
        self.health += amount
        print(f"{self.name} healed for {amount} health.")


# Example
player = Player("dominator", 100, 50)
player.display_info()
player.shoot()
player.take_damage(20)
player.heal(10)

# PLAYERS UNKNOWN BATTLE GROUND (PUBG) - ANIMALS AND VEHICLES 
# animals like horse and vehicles like cars
class Animal:
    """Animal class"""

    def __init__(self, name):
        """
        Initializes a new animal object.

        :param name: Animal's name
        """
        self.name = name

    def move(self):
        """Moves the animal."""
        print(f"{self.name} is walking.")


class Horse(Animal):
    """Horse class"""

    def __init__(self, name):
        super().__init__(name)

    def move(self):
        """Moves the horse."""
        print(f"{self.name} is running.")

class Vehicle:
    """Vehicle class"""

    def __init__(self, name):
        """
        Initializes a new vehicle object.

        :param name: Vehicle's name
        """
        self.name = name

    def move(self):
        """Moves the vehicle."""
        print(f"{self.name} is moving.")


class Car(Vehicle):
    """Car class"""

    def __init__(self, name):
        super().__init__(name)

    def move(self):
        """Moves the car."""
        print(f"{self.name} is driving.")

# Example 
horse= Horse("Buddy")
horse.move()

car = Car("Toyota")
car.move()
