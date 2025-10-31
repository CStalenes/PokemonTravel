class Floor:
    """
    Class representing a floor of arena with a trainer
    
    Attributes:
        numero (int): Floor number (1, 2, 3)
        dresseur (Trainer): Trainer who defends this floor
        defeated (bool): True if the trainer has been defeated
        description (str): Description of the floor
    """
    
    def __init__(self, number, trainer, description=""):
        """
        Initialize a floor
        
        Args:
            number (int): Floor number
            trainer (Trainer): Trainer of this floor
            description (str): Description of the floor
        """
        self.number = number
        self.trainer = trainer
        self.defeated = False
        self.description = description or f"Floor {number}"

    def is_available(self, previous_floor=None):
        """
        Check if the floor is available to challenge
        
        Args:
            previous_floor (Floor): Previous floor
            
        Returns:
            bool: True if the floor has not been defeated yet
        """
        # The floor 1 is always accessible
        if self.number == 1:
            return True
        
        # The other floors require having defeated the previous floor
        if previous_floor and previous_floor.defeated:
            return True
        return False

        # this bloc equal return previous_floor is not None and previous_floor.defeated:


    def display_info_floor(self):
        """Display the information of the floor"""
        statut = "**DEFEATED**" if self.defeated else "**TO CHALLENGE**"
        
        print(f"\n{'='*60}")
        print(f"FLOOR {self.number} - {self.description}")
        print(f"{'='*60}")
        print(f"Status: {statut}")
        print(f"Trainer: {self.trainer.name}")
        print(f"\n--- Trainer Team ---")
        
        for i, pokemon in enumerate(self.trainer.team, 1):
            print(f"  {i}. {pokemon.name} (Lvl.{pokemon.level}) - Type {pokemon.type_pokemon}")
        
        print(f"{'='*60}")
    
    def player_victory_floor(self):
        """Mark the floor as defeated"""
        self.defeated = True
    
    def reset_floor(self):
        """Reset the floor"""
        self.defeated = False
        self.trainer.heal_team()
    
    def __str__(self):
        statut = "**DEFEATED**" if self.defeated else "**TO CHALLENGE**"
        return f"{statut} FLOOR {self.number}: {self.trainer.name}"