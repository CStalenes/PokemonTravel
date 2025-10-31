from my_package.models.floor import Floor

class Arena:

    """
    Class representing a Pokemon arena
    
    An arena is defended by a champion specialized in a type.
    The player must beat the champion to obtain a badge.
    
    Attributes:
        name (str): Arena name
        type (str): Arena type ('Fire', 'Water', 'Plant')
        champion (Champion): Champion who defends the arena
        badge (str): Badge name obtained after victory
        defeated (bool): True if the player has already defeated this arena
    """

    def __init__(self, name, type_arena, champion, badge=None):
        self.name = name
        self.type_arena = type_arena
        self.champion = champion
        self.badge = badge or f"Badge of {self.type_arena} Arena"
        self.defeated = False

        #Arena stats
        self.nb_attempts = 0
        self.nb_victories = 0

        # Floors will be added with add_floors
        self.floors = []
        
        # The champion is always at the floor 3
        self.champion = champion
    
    def add_floors(self, trainer_floor1, trainer_floor2):
        """
        Configure the 3 floors of the arena
        
        Args:
            trainer_floor1 (Trainer): Trainer of the floor 1
            trainer_floor2 (Trainer): Trainer of the floor 2
        """
        # Floor 1: Beginner Trainer
        floor1 = Floor(1, trainer_floor1, f"{self.name} - Entrance Hall")

        # Floor 2: Intermediate Trainer
        floor2 = Floor(2, trainer_floor2, f"{self.name} - Training Room")
        
        # Floor 3: Champion
        floor3 = Floor(3, self.champion, f"{self.name} - Champion's Room")
        
        self.floors = [floor1, floor2, floor3]
        

    def is_available(self):
        """
        Check if the arena is available to challenge
        
        Returns:
            bool: True if the arena has not been defeated yet
        """
        return not self.defeated
    
    def challenge(self):
        """
        Start the arena challenge
        This method is called before starting the fight
        
        Returns:
            bool: True if the challenge can start, False otherwise
        """
        if self.defeated:
            print(f"\n You have already defeated {self.name} !")
            print(f" You already have the {self.badge}")
            return False
        
        self.nb_attempts += 1
        
        print(f"\n{'='*70}")
        print(f"WELCOME TO {self.name.upper()}")
        print(f"{'='*70}")
        print(f"Type Arena: {self.type_arena}")
        print(f"Champion: {self.champion.name}")
        print(f"Reward: {self.badge}")
        print(f"Attempts: {self.nb_attempts}")
        print(f"{'='*70}\n")

        print(f"📢 Announcement: \"Welcome to {self.name} !\"")
        print(f"   To challenge the Champion {self.champion.name},")
        print(f"   you must first defeat the trainers of the floors 1 and 2 !")
        print(f"\n    The arena has 3 floors:")
        print(f"   1. Entrance Hall - Beginner Trainer")
        print(f"   2. Training Room - Intermediate Trainer")
        print(f"   3. Champion's Room - {self.champion.name}")

        print(f"{self.champion.name}: \"I am {self.champion.name}, ")
        print(f"    master of the {self.type_arena} ! Are you ready to challenge me ?\"")

    def display_progression_floors(self):
        """Display the progression in the floors of the arena"""
        print(f"\n{'='*70}")
        print(f"PROGRESSION IN {self.name.upper()}")
        print(f"{'='*70}")
        
        for floor in self.floors:
            print(floor)
        
    def get_current_floor(self):
        """
        Return the current floor accessible
        
        Returns:
            Floor: Next floor to challenge, or None if all floors defeated
        """
        for floor in self.floors:
            if not floor.defeated:
                return floor
        return None
    
    def is_floor_accessible(self, floor_number):
        """
        Check if a floor is accessible
        
        Args:
            floor_number (int): Number of the floor (1-3)
            
        Returns:
            bool: True if accessible
        """
        if floor_number < 1 or floor_number > 3:
            return False
        
        floor = self.floors[floor_number - 1]
        
        # Floor 1 is always accessible
        if floor_number == 1:
            return not floor.defeated
        
        # Floors 2 and 3: check if the previous floor is defeated
        previous_floor = self.floors[floor_number - 2]
        return previous_floor.defeated and not floor.defeated

     def player_victory_floor(self, floor_number):
        """
        Mark a floor as defeated
        
        Args:
            floor_number (int): Number of the floor defeated
        """
        if floor_number < 1 or floor_number > 3:
            return
        
        floor = self.floors[floor_number - 1]
        floor.player_victory_floor()
        
        print(f"\n{'='*70}")
        print(f"FLOOR {floor_number} DEFEATED !")
        print(f"{'='*70}")
        print(f"You have defeated {floor.trainer.name} !")
        
        # If it's the champion (floor 3)
        if floor_number == 3:
            self.player_victory()
        else:
            # Unlock the next floor
            print(f"\nThe floor {floor_number + 1} is now accessible !")
            print(f"{'='*70}\n")
    
    def player_victory(self):
        """
        Called when the player beats the champion
        Marks the arena as defeated and rewards the player
        """
        if not self.defeated:
            self.defeated = True
            self.nb_victories += 1
            
            print(f"\n{'='*60}")
            print(f"CONGRATULATIONS !")
            print(f"{'='*60}")
            print(f"You have defeated {self.champion.name} of {self.name} !")
            print(f"You obtain the {self.badge} !")
            print(f"{'='*60}\n")
            
            print(f"{self.champion.name}: \"Bravo ! You have proven your value.")
            print(f"    Take this {self.badge}, you deserve it !\"")
    
    def player_defeat(self):
        """
        Called when the player loses to the champion
        """
        print(f"\n{'='*60}")
        print(f"DEFEAT...")
        print(f"{'='*60}")
        print(f"{self.champion.name} was too strong this time...")
        print(f"Train yourself and come back stronger !")
        print(f"{'='*60}\n")
        
        print(f"{self.champion.name}: \"You have potential, but you need to")
        print(f"    train yourself. Come back to me when you are ready !\"")
    
    def display_info_arena(self):
        """
        Display the detailed information of the arena
        """
        statut = "**DEFEATED**" if self.defeated else "**TO CHALLENGE**"
        
        print(f"\n{'='*60}")
        print(f"{self.name}")
        print(f"{'='*60}")
        print(f"Statut: {statut}")
        print(f"Type Arena: {self.type_arena}")
        print(f"Champion: {self.champion.name}")
        print(f"Badge: {self.badge}")
        print(f"Attempts: {self.nb_attempts}")
        
        if self.defeated:
            print(f"Victories: {self.nb_victories}")
        
        print(f"\n--- Champion Team ---")
        for i, pokemon in enumerate(self.champion.team, 1):
            print(f"  {i}. {pokemon.name} (Lvl.{pokemon.level}) - Type {pokemon.type}")
        
        print(f"{'='*60}")

    def reset_arena(self):
        """
        Reset the arena (for tests or replaying)
        """
        self.defeated = False
        self.nb_attempts = 0
        self.nb_victories = 0
        
        print(f"{self.name} has been reset")
    
    def __str__(self):
        """Textual representation of the arena"""
        statut = "OK" if self.defeated else "KO"
        return f"{statut} {self.name} - Champion {self.champion.name} ({self.type_arena})"

    def __repr__(self):
        """Technical representation of the arena"""
        return f"Arena(name='{self.name}', type='{self.type_arena}', champion='{self.champion.name}', defeated={self.defeated})"
