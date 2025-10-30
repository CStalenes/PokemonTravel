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
        print("1. ⚔️  Attack")
        print("2. 🔄 Change Pokemon")
        print("3. 🏃 Flee (only against wild Pokemon)")
        
        choice = input("\n➤ Your choice (1-3) : ").strip()
        
        if choice == '1':
            return {'type': 'attack', 'trainer': player}
        
        elif choice == '2':
            return self._menu_changement_pokemon(player)
        
        elif choice == '3':
            return 'flee'
        
        else:
            print("Invalid choice, default attack")
            return {'type': 'attack', 'trainer': player}

    def _menu_change_pokemon(self, trainer):
        """
        Menu to change Pokemon
        
        Args:
            trainer (Trainer): Trainer who changes Pokemon
            
        Returns:
            dict: Change action
        """
        print(f"\n--- Team of {trainer.name} ---")
        
        # Display the team
        for i, pokemon in enumerate(trainer.team, 1):
            marker = "VS" if pokemon == trainer.active_pokemon else "  "
            state = "KO" if pokemon.ko else f"{pokemon.hp_actuals}/{pokemon.hp_max} HP"
            print(f"{marker} {i}. {pokemon.name} (Lvl.{pokemon.level}) - {state}")
        
        print(f"{len(trainer.team) + 1}. ← Cancel")
        
        choice = input(f"\n➤ Choose a Pokemon (1-{len(trainer.team)}) : ").strip()
        
        try:
            index = int(choice) - 1
            
            if index == len(trainer.team):
                # Cancel
                return {'type': 'attack', 'trainer': trainer}
            
            if 0 <= index < len(trainer.team):
                if trainer.choose_pokemon(index):
                    return {'type': 'change', 'trainer': trainer, 'index': index}
                else:
                    # Change failed, default attack
                    return {'type': 'attack', 'trainer': trainer}
        except ValueError:
            pass
        
        print("Invalid choice")
        return {'type': 'attack', 'trainer': trainer}

    def _phase_action_ia(self, adversary, player):
        """
        Phase where the IA decides its action
        
        Args:
            adversary (Champion): Adversary controlled by the IA
            player (Trainer): Player trainer
            
        Returns:
            dict: Action chosen by the IA
        """
        # Vérifier si l'adversaire a une méthode IA (Champion)
        if hasattr(adversary, 'choose_action_ia'):
            decision = adversary.choose_action_ia(player.active_pokemon)
            
            if decision['action'] == 'change':
                adversary.choose_pokemon(decision['index'])
                return {'type': 'change', 'adversary': adversary}
        
        # Default : attack
        return {'type': 'attack', 'adversary': adversary}
    
    def _resolve_actions(self, action1, action2):
        """
        Resolve the actions in order of priority
        
        Args:
            action1 (dict): Action of the first trainer
            action2 (dict): Action of the second trainer
        """
        # Priority 1 : The changes of Pokemon are made first
        actions = [action1, action2]
        
        # Sort : changes first, then attacks by speed order
        def priority_action(action):
            if action['type'] == 'change':
                return (0, 0)  # Maximum priority
            else:
                # Speed order for attacks
                speed = action['trainer'].active_pokemon.speed
                return (1, -speed)  # Negative for decreasing order
        
        actions.sort(key=priority_action)
        
        # Execute the actions
        for action in actions:
            if not self.ongoing:
                break
            
            trainer = action['trainer']
            adversary = self.trainer2 if trainer == self.trainer1 else self.trainer1
            
            if action['type'] == 'attack':
                self._execute_attack(trainer, adversary)
            
            # The changes have already been made in the previous phases


    def _execute_attack(self, attacker_trainer, defender_trainer):
        """
        Execute an attack
        
        Args:
            attacker_trainer (Trainer): Trainer who attacks
            defender_trainer (Trainer): Trainer who defends
        """
        attacker = attacker_trainer.active_pokemon
        defender = defender_trainer.active_pokemon
        
        if not attacker or attacker.ko:
            return
        
        if not defenseur or defenseur.ko:
            return
        
        # Execute the attack
        print()
        result = attacker.attack_pokemon(defender)
        
        if result['success']:
            print(resultat['message'])
            
            # Update the statistics
            if attacker_trainer == self.trainer1:
                    self.total_damage_trainer1 += result['damage']
            else:
                self.total_damage_trainer2 += result['damage']
            
            # Check if the defender is KO
            if result.get('target_knocked_out', False):
                print(f"\n{defender.name} is KO !")
                
                # Gain experience
                exp_gained = self._calculate_experience(defender)
                self._gain_experience(attacker, exp_gained)
                
                # The defender must change of Pokemon
                if not defender_trainer.team_ko():
                    self._force_change_pokemon(defender_trainer)
        else:
            print(result['message'])
        
        self._pause(1)
    
     def _force_change_pokemon(self, trainer):
        """
        Force a trainer to change of Pokemon (after a KO)
        
        Args:
            trainer (Trainer): Trainer who must change
        """
        print(f"\n{trainer.name} must send another Pokemon !")
        
        if trainer == self.trainer1:
            # The player chooses
            self._menu_change_pokemon(trainer)
        else:
            # The IA chooses automatically
            trainer.choose_available_pokemon()
            if trainer.active_pokemon:
                print(f" {trainer.name} sends {trainer.active_pokemon.name} !")
        
        self._pause(1)


    def _calculate_experience(self, defeated_pokemon):
        """
        Calculate the experience gained after defeating a Pokemon
        
        Args:
            defeated_pokemon (Pokemon): Defeated Pokemon
            
        Returns:
            int: Experience points gained after defeating a Pokemon
        """
        # Simple formula: level of the defeated Pokemon * 10
        return defeated_pokemon.level * 10
    
    def _gain_experience(self, pokemon, experience):
        """
        Gain experience to a Pokemon
        
        Args:
            pokemon (Pokemon): Pokemon who gains experience
            experience (int): Experience points gained
        """
        print(f"\n{pokemon.name} gains {experience} experience points !")


    def _end_fight(self, winner):
        """
        Manage the end of the fight
        
        Args:
            winner (Trainer): Winner of the fight
        """
        self.ongoing = False
        
        print(f"\n{'='*70}")
        print(f"END OF FIGHT")
        print(f"{'='*70}")
        
        if winner == self.trainer1:
            print(f"VICTORY !")
            print(f"{self.trainer1.name} has won the fight !")
        
        elif winner == self.trainer2:
            print(f"DEFEAT...")
            print(f"{self.trainer2.name} has lost the fight...")
        else:
            print(f"DRAW...")
            print(f"The fight is a draw...")
        
        # Display the statistics
        print(f"\n--- Fight statistics ---")
        print(f"Turns: {self.current_turn}")
        print(f"Damage inflicted by {self.trainer1.name}: {self.total_damage_trainer1}")
        print(f"Damage inflicted by {self.trainer2.name}: {self.total_damage_trainer2}")
        print(f"{'='*70}\n")

    def _pause(self, seconds=0.5):
        """
        Pause to make the fight more readable
        
        Args:
            seconds (float): Duration of the pause
        """
        time.sleep(seconds)