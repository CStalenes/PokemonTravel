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
        type_multiplier = self.EFFICIENCY.get(self.type, {}).get(target.type, 1.0)
        # 4.5 On fait cela pour calculer les degat du multiplier en fonction de la cible et de l'attaquant
        
        # 5. Random variability (between 0.85 and 1.0)
        variability = random.uniform(0.85, 1.0)


        # 6. Constructing the attack message
        main_message = f"{self.name} attacks {target.name}!"
        damage_message = f"-> {final_damage} damage points inflicted"

        if effectiveness_message:
            messages.append(f"   {effectiveness_message}")
        messages.append(damage_message)
        
        # 7. Return attack information
        return {
            'success': True,
            'message': '\n'.join(messages),
            'damage': final_damage,
            'type_multiplier': type_multiplier,
            'target_knocked_out': target.knocked_out
        }

    def receive_damage(self, damage):
        """
        Receives damage and updates HP.
        
        Args:
            damage (int): Number of damage points received
        """
        self.current_hp -= damage
        
        if self.current_hp <= 0:
            self.current_hp = 0
            self.knockout = True

    def is_knockout(self):
        """Checks if the Pokémon is knocked out"""
        return self.knockout

    def heal(self):
        """Restores all of the Pokémon's HP"""
        self.current_hp = self.max_hp
        self.knockout = False

    def __str__(self):
        status = "KO" if self.ko else f"  {self.current_hp}/{self.max_hp} HP"
        return f"{self.name} (Lvl.{self.level}) [{self.type}] - {status}"



class FirePokemon(Pokemon):
    """Pokemon fire type"""

    def __init__(self, name, level=5):
        super().__init__(name, 'Fire', level)
        self.attack += 1

class WaterPokemon(Pokemon):
    """Pokemon water type"""

    def__init__(self, name, level=5):
        super().__init__(name,'Water', level)
        self.defense += 1

class PlanPokemon(Pokemon):
    """Pokemon plant type """

    def__init__(self, name, level=5):
        super().__init__(name, "Plant", level)
        self.hp_max += 2
        self.hp_max = self.hp_max 

    