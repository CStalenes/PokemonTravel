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
        if self.vaincue:
            print(f"\n You have already defeated {self.name} !")
            print(f" You already have the {self.badge}")
            return False
        
        self.nb_attempts += 1
        
        print(f"\n{'='*60}")
        print(f"WELCOME TO {self.name.upper()}")
        print(f"{'='*60}")
        print(f"Type Arena: {self.type_arena}")
        print(f"Champion: {self.champion.name}")
        print(f"Reward: {self.badge}")
        print(f"Attempts: {self.nb_attempts}")
        print(f"{'='*60}\n")

        print(f"👑 {self.champion.name}: \"I am {self.champion.name}, ")
        print(f"    master of the {self.type_arena} ! Are you ready to challenge me ?\"")
        
        return True
    
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
    
    def display_info(self):
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
    
    def __str__(self):
        """Textual representation of the arena"""
        statut = "OK" if self.defeated else "KO"
        return f"{statut} {self.name} - Champion {self.champion.name} ({self.type_arena})"

    def __repr__(self):
        """Technical representation of the arena"""
        return f"Arena(name='{self.name}', type='{self.type_arena}', champion='{self.champion.name}', defeated={self.defeated})"