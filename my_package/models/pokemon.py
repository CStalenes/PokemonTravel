class Pokemon:
    def __init__(self, name, type_pokemon, hp, attack, defense, speed, level=1):
        self.name = name
        self.type_pokemon = type_pokemon
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        
    def __str__(self):
        return f"{self.name} ({self.type_pokemon}) - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}, Level: {self.level}"
    
    def __repr__(self):
        return f"Pokemon({self.name}, {self.type_pokemon}, {self.hp}, {self.attack}, {self.defense}, {self.speed}, {self.level})"