import time
import random


class FightingSystem:
    """
    Class managing a Pokemon fight turn by turn
    
    Attributes:
        trainer1 (Trainer): First trainer (generally the player)
        trainer2 (Trainer): Second trainer (adversary/champion)
        current_turn (int): Number of the current turn
        ongoing (bool): State of the fight
    """
    
    def __init__(self, trainer1, trainer2):
        """
        Initialize a fight between two trainers
        
        Args:
            trainer1 (Trainer): First trainer (player)
            trainer2 (Trainer): Second trainer (adversary)
        """
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.current_turn = 0
        self.ongoing = False
        
        # Fight statistics
        self.total_damage_trainer1 = 0
        self.total_damage_trainer2 = 0