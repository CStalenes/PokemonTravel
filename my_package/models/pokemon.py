class Pokemon:

    """Basis class for Pokémon"""
    
    # Efficiency Table
    EFFICIENCY = {
        'Fire': {'Plant': 2.0, 'Water': 0.5, 'Fire': 1.0},
        'Eau': {'Fire': 2.0, 'Plant': 0.5, 'Water': 1.0},
        'Plant': {'Water': 2.0, 'Fire': 0.5, 'Plant': 1.0}
    }

    def __init__(self, name, type_pokemon,level=5):
        self.name = name
        self.type_pokemon = type_pokemon
        self.level = level
        
        self.hp_max     = 20 + (level *5)
        self.hp_actuals = self.hp_max
        self.attack     = 5 + (level *2)
        self.defense    = 3 + level
        self.speed      = 3 + level

        self.ko = False
      
        
    def __str__(self):
        return f"{self.name} ({self.type_pokemon}) - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}, Level: {self.level}"
    
    def __repr__(self):
        return f"Pokemon({self.name}, {self.type_pokemon}, {self.hp}, {self.attack}, {self.defense}, {self.speed}, {self.level})"