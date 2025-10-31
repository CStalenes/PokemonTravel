import json
import os
from datetime import datetime


class SaveSystem:
    """System for saving and loading game progress"""
    
    SAVE_DIR = "saves"
    SAVE_FILE = os.path.join(SAVE_DIR, "game_save.json")
    
    @staticmethod
    def ensure_save_directory():
        """Create the save directory if it doesn't exist"""
        if not os.path.exists(SaveSystem.SAVE_DIR):
            os.makedirs(SaveSystem.SAVE_DIR)
    
    @staticmethod
    def save_game(player, defeated_arenas):
        """
        Save the game progress to JSON
        
        Args:
            player (Trainer): The player trainer
            defeated_arenas (list): List of defeated arenas
        """
        SaveSystem.ensure_save_directory()
        
        # Prepare data to save
        save_data = {
            'player_name': player.name,
            'badges_count': len(defeated_arenas),
            'defeated_arenas': [arena.name for arena in defeated_arenas],
            'team': [],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save team data
        for pokemon in player.team:
            pokemon_data = {
                'name': pokemon.name,
                'type': pokemon.type_pokemon,
                'level': pokemon.level,
                'hp_max': pokemon.hp_max,
                'hp_actuals': pokemon.hp_actuals,
                'attack': pokemon.attack,
                'defense': pokemon.defense,
                'speed': pokemon.speed,
                'ko': pokemon.ko
            }
            save_data['team'].append(pokemon_data)
        
        # Write to JSON file
        try:
            with open(SaveSystem.SAVE_FILE, 'w') as f:
                json.dump(save_data, f, indent=4)
            print(f"\n✓ Game saved successfully!")
            print(f"  Location: {SaveSystem.SAVE_FILE}")
            print(f"  Badges: {save_data['badges_count']}/3")
            return True
        except Exception as e:
            print(f"\n✗ Error saving game: {e}")
            return False
    
    @staticmethod
    def load_game():
        """
        Load game progress from JSON
        
        Returns:
            dict: Game data or None if no save found
        """
        if not os.path.exists(SaveSystem.SAVE_FILE):
            print("No save file found.")
            return None
        
        try:
            with open(SaveSystem.SAVE_FILE, 'r') as f:
                save_data = json.load(f)
            print(f"\n✓ Save found!")
            print(f"  Player: {save_data['player_name']}")
            print(f"  Badges: {save_data['badges_count']}/3")
            print(f"  Saved: {save_data['timestamp']}")
            return save_data
        except Exception as e:
            print(f"\n✗ Error loading game: {e}")
            return None
    
    @staticmethod
    def display_save_info():
        """Display information about the current save"""
        if not os.path.exists(SaveSystem.SAVE_FILE):
            print("\nNo save file found.")
            return False
        
        try:
            with open(SaveSystem.SAVE_FILE, 'r') as f:
                save_data = json.load(f)
            
            print(f"\n{'='*60}")
            print(f"SAVE FILE INFORMATION")
            print(f"{'='*60}")
            print(f"Player: {save_data['player_name']}")
            print(f"Badges: {save_data['badges_count']}/3")
            print(f"Team Size: {len(save_data['team'])}")
            print(f"Last Saved: {save_data['timestamp']}")
            print(f"\nTeam:")
            for i, pokemon in enumerate(save_data['team'], 1):
                status = "KO" if pokemon['ko'] else f"{pokemon['hp_actuals']}/{pokemon['hp_max']} HP"
                print(f"  {i}. {pokemon['name']} ({pokemon['type']}) Lvl.{pokemon['level']} - {status}")
            print(f"{'='*60}\n")
            return True
        except Exception as e:
            print(f"\n✗ Error: {e}")
            return False
    
    @staticmethod
    def delete_save():
        """Delete the save file"""
        if os.path.exists(SaveSystem.SAVE_FILE):
            try:
                os.remove(SaveSystem.SAVE_FILE)
                print("\n✓ Save file deleted.")
                return True
            except Exception as e:
                print(f"\n✗ Error deleting save: {e}")
                return False
        else:
            print("\nNo save file to delete.")
            return False
