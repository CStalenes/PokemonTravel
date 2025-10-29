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

    def start(self):
        """
        Start the fight and manage the main loop
        
        Returns:
            bool: True if trainer1 wins, False otherwise
        """
        self.ongoing = True
        self.current_turn = 0
        
        # Introduction message
        self._display_introduction()

        # Ensure each trainer has an active Pokemon
        if not self.trainer1.active_pokemon:
            self.trainer1.choose_available_pokemon()
        if not self.trainer2.active_pokemon:
            self.trainer2.choose_available_pokemon()
        
        # Main loop of the fight
        while self.ongoing:
            self.current_turn += 1
            self._execute_turn()
            
            # Check if the fight is over
            if self.trainer1.team_ko():
                self._end_fight(winner=self.trainer2)
                return False
            
            if self.trainer2.team_ko():
                self._end_fight(winner=self.trainer1)
                return True
        
        return False
    
    def _display_introduction(self):
        """Display the introduction of the fight"""
        print(f"\n{'='*70}")
        print(f"FIGHT POKEMON")
        print(f"{'='*70}")
        print(f"{self.trainer1.name} VS {self.trainer2.name}")
        print(f"{'='*70}\n")
        
        input("Press Enter to start the fight...")
        self._pause()
    
    def _execute_turn(self):
        """Execute a complete turn of the fight"""
        print(f"\n{'='*70}")
        print(f"TURN {self.current_turn}")
        print(f"{'='*70}")
        
        # Display the current state
        self._display_fight_state()
        
        # Phase 1 : Actions of trainer 1 (player)
        action1 = self._phase_action_player(self.trainer1)
        
        # Check if the player has fled
        if action1 == 'fuir':
            self._flee_fight()
            return
        
        # Phase 2 : Actions of trainer 2 (adversary/IA)
        action2 = self._phase_action_adversary(self.trainer2, self.trainer1)
        
        # Phase 3 : Resolution of actions (speed order)
        self._resolve_actions(action1, action2)
        
        # Pause between turns
        input("\nPress Enter to continue...")
    
    def _display_fight_state(self):
        """Display the current state of the fight"""
        print(f"\n--- Fight State ---")
        

        # Player's Pokemon
        p1 = self.trainer1.active_pokemon
        if p1:
            percentage = int((p1.hp_actuals / p1.hp_max) * 100)
            bar = self._display_hp_bar(percentage)
            print(f"👤 {self.trainer1.name}: {p1.name} (Lvl.{p1.level})")
            print(f"   {bar} {p1.hp_actuals}/{p1.hp_max} HP ({percentage}%)")
        
        print()
        
        # Adversary's Pokemon
        p2 = self.trainer2.active_pokemon
        if p2:
            percentage = int((p2.hp_actuals / p2.hp_max) * 100)
            bar = self._display_hp_bar(percentage)
            print(f"👤 {self.trainer2.name}: {p2.name} (Lvl.{p2.level})")
            print(f"   {bar} {p2.hp_actuals}/{p2.hp_max} HP ({percentage}%)")
        
        print(f"\n{'='*70}")

    def _display_hp_bar(self, percentage):
        """
        Create a visual HP bar
        
        Args:
            percentage (int): Percentage of HP (0-100)
            
        Returns:
            str: Formatted HP bar
        """
        length = 20
        filled = int((percentage / 100) * length)
        empty = length - filled
        
        # Color according to the HP
        if percentage > 50:
            symbol = "█"
        elif percentage > 20:
            symbol = "▓"
        else:
            symbol = "░"
        
        bar = symbol * filled + "·" * empty
        return f"[{bar}]"
    
    def _phase_action_player(self, player):
        """
        Phase where the player chooses his action
        
        Args:
            player (Trainer): The player trainer
            
        Returns:
            dict: Chosen action
        """
        print(f"\n--- Turn of {player.name} ---")
        print("What do you want to do?")
        print("1. ⚔️  Attaquer")
        print("2. 🔄 Change Pokemon")
        print("3. 🏃 Flee (only against wild Pokemon)")
        
        choice = input("\n➤ Your choice (1-3) : ").strip()
        
        if choice == '1':
            return {'type': 'attack', 'trainer': player}
        
        elif choice == '2':
            return self._menu_changement_pokemon(player)
        
        elif choice == '3':
            return 'fuir'
        
        else:
            print("❌ Invalid choice, default attack")
            return {'type': 'attack', 'trainer': player}