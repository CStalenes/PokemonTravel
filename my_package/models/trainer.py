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
        
        self.team.append(pokemon)
        
        #  1st pokemon become active
        if len(self.team) == 1:
            self.active_pokemon = pokemon
        
        return True
        
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
        if pokemon_chosen == self.active_pokemon:
            print(f" !! {pokemon_chosen.name} is already in combat !")
            return False
        
        # change the Pokemon
        previous = self.active_pokemon.name if self.active_pokemon else "None"
        self.active_pokemon = pokemon_chosen
        print(f" {self.name} recall {previous} and send {pokemon_chosen.name} !")
        
        return True


    def choose_available_pokemon(self):
        """
        Choose automatically the first able to fight Pokemon (not KO)
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
            pokemon.heal()
        
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
            marker = "VS" if pokemon == self.active_pokemon else "   "
            print(f"{marker}{i}. {pokemon}")
        
        print(f"{'='*50}")

    def __str__(self):
        """ Trainer Profile"""
        nb_pokemon = len(self.team)
        nb_availability = self.count_available_pokemon()
        return f" {self.name} - {nb_availability}/{nb_pokemon} Pokemon able to fight"


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
        super().__init__(name)
        self.type_affinity = type_affinity

    def choose_action_ia(self, adversary_pokemon):
        """
        Simple IA for the champion : decide what action to make
        
        Args:
            adversary_pokemon (Pokemon): Adversary Pokemon currently in combat
            
        Returns:
            dict: Action to perform {'action': 'attack'/'change', 'index': int}
        """
        # Strategy 1 : If the active Pokemon is in bad shape, try to change
        if self.active_pokemon.current_hp < self.active_pokemon.hp_max * 0.3:
            # Search for a Pokemon in better shape
            best_pokemon = self._find_best_pokemon(adversary_pokemon)
            if best_pokemon and best_pokemon != self.active_pokemon:
                index = self.team.index(best_pokemon)
                return {'action': 'change', 'index': index}
        
        # Strategy 2 : If disadvantaged by the type, try to change
        if self._has_type_disadvantage(self.active_pokemon, adversary_pokemon):
            best_pokemon = self._find_best_pokemon(adversary_pokemon)
            if best_pokemon and best_pokemon != self.active_pokemon:
                index = self.team.index(best_pokemon)
                return {'action': 'change', 'index': index}
        
        # Default : Attack
        return {'action': 'attack'}

    def _find_best_pokemon(self, adversary_pokemon):
        """
        Find the best Pokemon to send against the adversary
        
        Args:
            adversary_pokemon (Pokemon): Adversary Pokemon
            
        Returns:
            Pokemon: Best Pokemon available or None
        """
        best = None
        best_score = -1
        
        for pokemon in self.team:
            if pokemon.ko:
                continue
            
            score = 0
            
            # Score based on remaining HP (0-100)
            score += (pokemon.current_hp / pokemon.hp_max) * 100
            
            # Bonus if type advantage (+200)
            if self._has_type_advantage(pokemon, adversary_pokemon):
                score += 200
            
            # Malus if type disadvantage (-100)
            if self._has_type_disadvantage(pokemon, adversary_pokemon):
                score -= 100
            
            if score > best_score:
                best_score = score
                best = pokemon
        
        return best
    

    def _has_type_advantage(self, attacker, defender):
        """
        Check if the attacker has a type advantage
        
        Args:
            attacker (Pokemon): Attacking Pokemon
            defender (Pokemon): Defending Pokemon
            
        Returns:
            bool: True if the attacker has a type advantage
        """
        from my_package.models.pokemon import Pokemon
        
        effectiveness = Pokemon.EFFICIENCY.get(attacker.type, {}).get(defender.type, 1.0)
        return effectiveness > 1.0
    
    def _has_type_disadvantage(self, attacker, defender):
        """
        Check if the attacker has a type disadvantage
        
        Args:
            attacker (Pokemon): Attacking Pokemon
            defender (Pokemon): Defending Pokemon
            
        Returns:
            bool: True if the attacker has a type disadvantage
        """
        from my_package.models.pokemon import Pokemon
        
        effectiveness = Pokemon.EFFICIENCY.get(attacker.type, {}).get(defender.type, 1.0)
        return effectiveness < 1.0