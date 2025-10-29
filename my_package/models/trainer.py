class Trainer:
    def __init__(self, name):
        
        """
        trainer initiate
        Args:
            name (str) : Trainer name
        """
        self.name = name
        self.team = []
        self.active_pokemon = None


    def add_pokemon(self, pokemon):
        # limited to 6 Pokemon max
        if len(self.team) >= 6:
            print(f"NOPE {self.name} team are fully complete with 6 Pokemon !")
            return False
        
        self.equipe.append(pokemon)
        
        #  1st pokemon become active
        if len(self.equipe) == 1:
            self.pokemon_actif = pokemon
        
        return 
        
    def choose_pokemon(self, index):
        """
        Choose a Pokemon for the fight
        
        Args:
            index (int): Index of the Pokemon in the team (0-5)
            
        Returns:
            bool: True if change is successful, False otherwise
        """
        # check if the index is valid
        if index < 0 or index >= len(self.team):
            print(f"Pokemon #{index + 1} doesn't exist !")
            return False
        
        pokemon_chosen = self.team[index]
        
        # check if the Pokemon is not KO
        if pokemon_chosen.ko:
            print(f"{pokemon_chosen.name} is KO and can't fight !")
            return False
        
        # check if the Pokemon is not already active
        if pokemon_chosen == self.pokemon_actif:
            print(f" !! {pokemon_chosen.name} is already in combat !")
            return False
        
        # change the Pokemon
        previous = self.pokemon_actif.name if self.pokemon_actif else "None"
        self.pokemon_actif = pokemon_chosen
        print(f" {self.name} recall {previous} and send {pokemon_chosen.name} !")
        
        return True


    def choose_available_pokemon(self):
        """
        Choose automatically the first available Pokemon (not KO)
        Useful when the active Pokemon is KO
        
        Returns:
            bool: True if a Pokemon has been found, False if all are KO
        """
        for pokemon in self.team:
            if not pokemon.ko:
                self.active_pokemon = pokemon
                return True
        
        return False
    
    def team_ko(self):
        """
        Check if the team is KO
        
        Returns:
            bool: True if all the Pokemon are KO
        """
        return all(pokemon.ko for pokemon in self.team)
    
    def count_available_pokemon(self):
        """
        Count the number of Pokemon still able to fight
        
        Returns:
            int: Number of Pokemon not KO
        """
        return sum(1 for pokemon in self.team if not pokemon.ko)
    
    def heal_team(self):
        """
        Heal all the Pokemon of the team
        Used after a victory or in a Pokemon center
        """
        for pokemon in self.team:
            pokemon.soigner()
        
        print(f"All the Pokemon of {self.name} have been healed !")
    
    def display_team(self):
        """
        Display the complete team of the trainer
        """
        print(f"\n{'='*50}")
        print(f"Team of {self.name}")
        print(f"{'='*50}")
        
        if not self.team:
            print("No Pokemon in the team")
            return
        
        for i, pokemon in enumerate(self.team, 1):
            marker = "VS" if pokemon == self.pokemon_actif else "   "
            print(f"{marker}{i}. {pokemon}")
        
        print(f"{'='*50}")

    def __str__(self):
        """ Trainer Profile"""
        nb_pokemon = len(self.team)
        nb_availability = self.count_available_pokemon()
        return f" {self.name} - {nb_availability}/{nb_pokemon} Pokemon available"


class Champion(Trainer):
    """
    Class representing an arena champion
    Inherits from Trainer with specific behaviors
    
    Attributes:
        specialty_type (str): Champion's elemental type
    """

    def __init__(self, name, type_affinity):

        """
        Initiate a champion
        Args:
            name (str): champion name
            type_affinity (str): champion elemental type
        """
        super.()__init__(name)
        self.type_affinity = type_affinity
    
    
