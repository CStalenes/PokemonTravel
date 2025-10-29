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

    def __str__(self):
        """ Trainer Profile"""
        nb_pokemon = len(self.equipe)
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
    
    def add_pokemon(self, pokemon):
        
