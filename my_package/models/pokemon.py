import random

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
        return f"{self.name} ({self.type_pokemon}) - HP: {self.hp_actuals}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}, Level: {self.level}"
    
    def __repr__(self):
        return f"Pokemon({self.name}, {self.type_pokemon}, {self.hp_actuals}, {self.attack}, {self.defense}, {self.speed}, {self.level})"


    def attack_pokemon(self, target):

        """
        Attacks a target Pokémon and calculates the damage inflicted.
        
        Args:
            target (Pokemon): The Pokémon receiving the attack
            
        Returns:
            dict: Information about the attack (damage, effectiveness)
        """

       # 1. Check if the attacker is KO
        if self.ko:
            return {
                'success': False,
                'message': f"{self.name} is KO and cannot attack!"
            }
        
        # 2. Check if the target is KO
        if target.ko:
            return {
                'success': False,
                'message': f"{target.name} is already KO!"
            }
        
        # 3. Calculate accuracy (95% chance of hitting)
        if random.random() > 0.95:
            return {
                'success': False,
                'message': f"{self.name} missed their attack!",
                'damage': 0
            }

        base_damage = (self.attack * self.level / 5) - (target.defense / 2)
        base_damage = max(1, base_damage)  # Minimum 1 damage
        
        # 4. Type multiplier (efficiency)
        type_multiplier = self.EFFICIENCY.get(self.type_pokemon, {}).get(target.type_pokemon, 1.0)
        # 4.5 On fait cela pour calculer les degat du multiplier en fonction de la cible et de l'attaquant
        
        # 5. Random variability (between 0.85 and 1.0)
        variability = random.uniform(0.85, 1.0)
        
        # Calculate final damage
        final_damage = int(base_damage * type_multiplier * variability)
        final_damage = max(1, final_damage)  # Minimum 1 damage
        
        # Apply damage to target
        target.hp_actuals -= final_damage
        target_knocked_out = False
        
        if target.hp_actuals <= 0:
            target.hp_actuals = 0
            target.ko = True
            target_knocked_out = True

        # 6. Constructing the attack message
        messages = []
        main_message = f"{self.name} attacks {target.name}!"
        messages.append(main_message)
        
        # Determine effectiveness message
        if type_multiplier > 1.0:
            effectiveness_message = "It's super effective!"
        elif type_multiplier < 1.0:
            effectiveness_message = "It's not very effective..."
        else:
            effectiveness_message = ""
        
        damage_message = f"→ {final_damage} damage points inflicted"
        
        if effectiveness_message:
            messages.append(f"   {effectiveness_message}")
        messages.append(damage_message)
        
        # 7. Return attack information
        return {
            'success': True,
            'message': '\n'.join(messages),
            'damage': final_damage,
            'type_multiplier': type_multiplier,
            'target_knocked_out': target_knocked_out
        }

    def receive_damage(self, damage):
        """
        Receives damage and updates HP.
        
        Args:
            damage (int): Number of damage points received
        """
        self.hp_actuals -= damage
        
        if self.hp_actuals <= 0:
            self.hp_actuals = 0
            self.ko = True

    def is_knockout(self):
        """Checks if the Pokémon is knocked out"""
        return self.ko

    def heal(self):
        """Restores all of the Pokémon's HP"""
        self.hp_actuals = self.hp_max
        self.ko = False

    def __str__(self):
        status = "KO" if self.ko else f"  {self.hp_actuals}/{self.hp_max} HP"
        return f"{self.name} (Lvl.{self.level}) [{self.type_pokemon}] - {status}"



class FirePokemon(Pokemon):
    """Pokemon fire type"""

    def __init__(self, name, level=5):
        super().__init__(name, 'Fire', level)
        self.attack += 1

class WaterPokemon(Pokemon):
    """Pokemon water type"""

    def __init__(self, name, level=5):
        super().__init__(name,'Water', level)
        self.defense += 1

class PlantPokemon(Pokemon):
    """Pokemon plant type """

    def __init__(self, name, level=5):
        super().__init__(name, "Plant", level)
        self.hp_max += 2
        self.hp_max = self.hp_max


class PokemonFactory:
    """Factory to create Pokémon according to their type"""
    
    POKEMON_TYPES = {
        'Fire': FirePokemon,
        'Water': WaterPokemon,
        'Plant': PlantPokemon
    }
    
    @staticmethod
    def create_pokemon(name, type_pokemon, level=5):
        """
        Create a Pokemon of the specified type
        
        Args:
            name (str): Name of the Pokemon
            type_pokemon (str): 'Fire', 'Water', or 'Plant'
            level (int): Level of the Pokemon
            
        Returns:
            Pokemon: Instance of the created Pokemon
        """
        pokemon_class = PokemonFactory.POKEMON_TYPES.get(type_pokemon)
        
        if pokemon_class is None:
            raise ValueError(f"Type '{type_pokemon}' unknown")
        
        return pokemon_class(name, level)
    
    @staticmethod
    def create_team(list_pokemon):
        """
        Create a complete team of Pokémon
        
        Args:
            list_pokemon: List of tuples (name, type, level)
            
        Returns:
            list: List of created Pokémon
        """
        team = []
        for name, type_pokemon, level in list_pokemon:
            pokemon = PokemonFactory.create_pokemon(name, type_pokemon, level)
            team.append(pokemon)
        return team

class PokemonGenerator:
    """Generator of random Pokémon"""
    
    NAMES_BY_TYPE = {
        'Fire': ["Ponyta", "Goupix", "Caninos", "Magmar"],
        'Water': ["Psykokwak", "Poissirène", "Tentacool", "Krabby"],
        'Plant': ["Mystherbe", "Chétiflor", "Saquedeneu", "Boustiflor"]
    }
    
    @staticmethod
    def generate_wild_pokemon(player_level):
        """
        Generate a random wild Pokemon
        
        Args:
            player_level (int): Level of the player
            
        Returns:
            Pokemon: Instance of the generated Pokemon
        """
        type_pokemon = random.choice(['Fire', 'Water', 'Plant'])
        name = random.choice(PokemonGenerator.NAMES_BY_TYPE[type_pokemon])
        level = max(1, player_level - random.randint(1, 3))
        
        return PokemonFactory.create_pokemon(name, type_pokemon, level)