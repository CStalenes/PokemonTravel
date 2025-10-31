from my_package.models.pokemon import FirePokemon, WaterPokemon, PlantPokemon
from my_package.models.trainer import Trainer, Champion
from my_package.models.arena import Arena
from fighting.fighting_system import FightingSystem
from utils.display import display_title, display_menu, clear_screen, display_separator
from my_package.models.pokemon import PokemonGenerator, PokemonFactory
import random
random.seed(42)


class Game:
    """Main class managing the game flow"""
    
    def __init__(self):
        self.player = None
        self.arenas = []
        self.defeated_arenas = []
        self.ongoing = True
        
    def initialize_game(self):
        """Initialize the player and the arenas"""
        clear_screen()
        display_title("WELCOME TO THE THREE ARENAS CHALLENGE")
        
        # Creation of the player
        player_name = input("\nEnter your name, young trainer : ").strip()
        if not player_name:
            player_name = "Sacha"
        
        self.player = Trainer(player_name)
        
        # Choose starter first (required)
        self.choose_starter()
        
        # Then choose how to complete the team
        self.choose_team_mode()
        
        # Creation of the arenas
        self.create_arenas()
        
        print(f"\nGood luck, {self.player.name} !")
        input("\nPress Enter to continue...")
    
    def choose_starter(self):
        """Allow the player to choose his starter Pokemon"""
        clear_screen()
        display_title("CHOOSE YOUR STARTING POKEMON")
        
        print("\n1. Salamèche (Fire) - Strong against Plant, Weak against Water")
        print("2. Carapuce (Water) - Strong against Fire, Weak against Plant")
        print("3. Bulbizarre (Plant) - Strong against Water, Weak against Fire")
        
        choice = input("\nYour choice (1-3) : ").strip()
        
        starters = {
            '1': FirePokemon("Salamèche", level=5),
            '2': WaterPokemon("Carapuce", level=5),
            '3': PlantPokemon("Bulbizarre", level=5)
        }
        
        starter = starters.get(choice, FirePokemon("Salamèche", level=5))
        self.player.add_pokemon(starter)
        
        print(f"\nYou have chosen {starter.name} !")
        print(f"   Type: {starter.type_pokemon} | Level: {starter.level}")
        print(f"   HP: {starter.hp_max} | Attack: {starter.attack}")

    def choose_team_mode(self):
        """Allow player to choose how to build their team after selecting starter"""
        while True:
            clear_screen()
            display_title("COMPLETE YOUR TEAM")
            
            starter = self.player.team[0]
            print(f"\nYour starter {starter.name} is in your team (1/6)")
            print("\nHow do you want to complete your team of 6?")
            print("1. Let random Pokemon be added automatically")
            print("2. Choose 5 more Pokemon yourself")
            
            choice = input("\nYour choice (1-2): ").strip()
            
            if choice == '1':
                self.fill_team_randomly()
                break
            elif choice == '2':
                self.build_custom_team_with_starter()
                break
            else:
                print("\nInvalid choice!")
                input("\nPress Enter to try again...")

    def fill_team_randomly(self):
        """Fill the remaining team slots with random Pokemon (up to 6 total)"""
        print("\nFilling your team with random Pokemon...")
        while len(self.player.team) < 6:
            pokemon = PokemonGenerator.generate_wild_pokemon(5)
            self.player.add_pokemon(pokemon)
            print(f"   ✓ {pokemon.name} joined your team!")
        
        print("\nYour team is now complete!")
        input("\nPress Enter to continue...")

    def build_custom_team_with_starter(self):
        """Allow the player to choose 5 more Pokemon to complete their team (starter already added)"""
        remaining_slots = 6 - len(self.player.team)  # Should be 5
        
        while len(self.player.team) < 6:
            clear_screen()
            slots_filled = len(self.player.team)
            display_title(f"CHOOSE POKEMON {slots_filled}/6")
            
            starter = self.player.team[0]
            print(f"Your starter: {starter.name}")
            print(f"Current team: {slots_filled}/6 Pokemon\n")
            
            # Generate 3 random Pokemon options
            options = []
            for _ in range(3):
                pokemon = PokemonGenerator.generate_wild_pokemon(5)
                options.append(pokemon)
            
            print(f"Choose one of these Pokemon:")
            for i, pokemon in enumerate(options, 1):
                print(f"{i}. {pokemon.name} ({pokemon.type_pokemon}) - Lvl.{pokemon.level}")
                print(f"   HP: {pokemon.hp_max} | Attack: {pokemon.attack} | Defense: {pokemon.defense}")
            
            choice = input("\nYour choice (1-3): ").strip()
            
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < 3:
                    selected_pokemon = options[choice_index]
                    self.player.add_pokemon(selected_pokemon)
                    print(f"\n✓ {selected_pokemon.name} added to your team!")
                    input("\nPress Enter to continue...")
                else:
                    print("\nInvalid choice! Choose between 1 and 3")
                    input("\nPress Enter to try again...")
            except ValueError:
                print("\nPlease enter a valid number!")
                input("\nPress Enter to try again...")
        
        clear_screen()
        display_title("TEAM COMPLETE!")
        print(f"\nYour team of 6 Pokemon is ready!")
        self.player.display_team()
        input("\nPress Enter to continue...")

    def build_custom_team(self):
        """Allow the player to build a custom team of 6 random Pokemon"""
        clear_screen()
        display_title("BUILD YOUR TEAM OF 6 POKEMON")
        
        print("\nYou will be offered random Pokemon to build your team of 6!")
        input("\nPress Enter to start...")
        
        pokemon_count = 0
        max_pokemon = 6
        
        while pokemon_count < max_pokemon:
            clear_screen()
            display_title(f"POKEMON {pokemon_count + 1}/6")
            
            # Generate 3 random Pokemon options
            options = []
            for _ in range(3):
                pokemon = PokemonGenerator.generate_wild_pokemon(5)
                options.append(pokemon)
            
            print(f"\nChoose one of these Pokemon:")
            for i, pokemon in enumerate(options, 1):
                print(f"{i}. {pokemon.name} ({pokemon.type_pokemon}) - Lvl.{pokemon.level}")
                print(f"   HP: {pokemon.hp_max} | Attack: {pokemon.attack} | Defense: {pokemon.defense}")
            
            choice = input("\nYour choice (1-3): ").strip()
            
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < 3:
                    selected_pokemon = options[choice_index]
                    self.player.add_pokemon(selected_pokemon)
                    print(f"\n✓ {selected_pokemon.name} added to your team!")
                    pokemon_count += 1
                    input("\nPress Enter to continue...")
                else:
                    print("\nInvalid choice! Choose between 1 and 3")
                    input("\nPress Enter to try again...")
            except ValueError:
                print("\nPlease enter a valid number!")
                input("\nPress Enter to try again...")
        
        clear_screen()
        display_title("TEAM COMPLETE!")
        print(f"\nYour team of 6 Pokemon is ready!")
        self.player.display_team()
        input("\nPress Enter to continue...")

    def display_team(self):
        """Display the player's team"""
        clear_screen()
        display_title("MY TEAM")
        
        if not self.player.team:
            print("\nYou don't have any Pokemon yet !")
        else:
            for i, pokemon in enumerate(self.player.team, 1):
                print(f"\n{i}. {pokemon}")
        
        input("\nPress Enter to return...")

    def quit_game(self):
        """Quit the game"""
        clear_screen()
        display_title("GOODBYE !")
        
        print(f"\nSee you soon, {self.player.name} !")
        print(f"Badges obtained: {len(self.defeated_arenas)}/3")
        
        self.ongoing = False

    def create_arenas(self):
        """Create the three arenas with their champions"""

        # Fire Arena

        # Floor 1: Beginner Trainer
        beginner_trainer = Trainer("Sam")
        beginner_trainer.add_pokemon(FirePokemon("Goupix", level=8))
        
        # Floor 2: Intermediate Trainer
        intermediate_trainer = Trainer("Robert")
        intermediate_trainer.add_pokemon(FirePokemon("Ponyta", level=8))
        intermediate_trainer.add_pokemon(FirePokemon("Caninos", level=8))
    
        # Floor 3: Champion
        fire_champion = Champion("Pierre", "Fire")
        fire_champion.add_pokemon(FirePokemon("Ponyta", level=8))
        fire_champion.add_pokemon(FirePokemon("Goupix", level=10))
        fire_arena = Arena("Fire Arena", "Fire", fire_champion, "Badge Volcan")

        # Water Arena


        # Floor 1: Beginner Trainer
        beginner_trainer = Trainer("Sandy")
        beginner_trainer.add_pokemon(WaterPokemon("Stari", level=8))
        
        # Floor 2: Intermediate Trainer
        intermediate_trainer = Trainer("Gerald")
        intermediate_trainer.add_pokemon(WaterPokemon("Poissirène", level=10))
        intermediate_trainer.add_pokemon(WaterPokemon("Tentacool", level=11))
    
        # Floor 3: Champion
        water_champion = Champion("Ondine", "Water")
        water_champion.add_pokemon(WaterPokemon("Stari", level=12))
        water_champion.add_pokemon(WaterPokemon("Psykokwak", level=14))
        water_arena = Arena("Water Arena", "Water", water_champion, "Badge Marine")

        # Plant Arena

        # Floor 1: Beginner Trainer
        beginner_trainer = Trainer("John")
        beginner_trainer.add_pokemon(PlantPokemon("Mystherbe", level=12))
        
        # Floor 2: Intermediate Trainer
        intermediate_trainer = Trainer("Bill")
        intermediate_trainer.add_pokemon(PlantPokemon("Chétiflor", level=13))
        
        plant_champion = Champion("Erika", "Plant")
        plant_champion.add_pokemon(PlantPokemon("Saquedeneu", level=14))
        plant_champion.add_pokemon(PlantPokemon("Boustiflor", level=16))
        plant_arena = Arena("Plant Arena", "Plant", plant_champion, "Badge Vert")

        self.arenas.extend([fire_arena, water_arena, plant_arena])

    # Challenge an arena
    def choose_and_challenge_arena(self):
        """Let the player choose an arena to challenge"""
        clear_screen()
        display_title("CHOOSE AN ARENA TO CHALLENGE")
        
        available_arenas = [arena for arena in self.arenas if arena not in self.defeated_arenas]
        
        if not available_arenas:
            print("\nAll arenas have been defeated! You are a true champion!")
            input("\nPress Enter to continue...")
            return
        
        for i, arena in enumerate(available_arenas, 1):
            print(f"\n{i}. {arena.name}")
            print(f"   Type: {arena.type_arena}")
            print(f"   Champion: {arena.champion.name}")
        
        choice = input("\nChoose an arena (number) : ").strip()
        
        try:
            arena_index = int(choice) - 1
            if 0 <= arena_index < len(available_arenas):
                self.challenge_arena(available_arenas[arena_index])
            else:
                print("\nInvalid choice!")
                input("\nPress Enter...")
        except ValueError:
            print("\nPlease enter a valid number!")
            input("\nPress Enter...")
    
    def challenge_arena(self, arena):
        """Start a fight against the arena champion"""
        clear_screen()
        display_title(f"CHALLENGE: {arena.name.upper()}")
        
        print(f"\n{'='*60}")
        print(f"\nChampion {arena.champion.name} is waiting for you !")
        print(f"Specialité: Type {arena.type_arena}")
        print(f"{'='*60}")
        
        input("\nPress Enter to start the fight...")
        
        # Start the fight
        fight = FightingSystem(self.player, arena.champion)
        victory = fight.start()
        
        if victory:
            self.defeated_arenas.append(arena)
            # print(f"\n🏆 VICTORY ! You have obtained the Badge {arena.badge} !")
            arena.player_victory()
            
            # Check if all arenas are defeated
            # if len(self.defeated_arenas) == 3:
            #    self.final_victory()
        else:
            print("\nDEFEAT... Train yourself and come back stronger !")
        
        input("\nPress Enter to continue...")

    def catch_new_pokemon(self):
        """Allow the player to catch new Pokemon to add to their team (up to 6)"""
        clear_screen()
        display_title("CATCH NEW POKEMON")
        
        if len(self.player.team) >= 6:
            print("\nYour team is full (6/6 Pokemon)!")
            print("You cannot catch any more Pokemon.")
            input("\nPress Enter to continue...")
            return
        
        slots_available = 6 - len(self.player.team)
        print(f"\nYou can catch {slots_available} more Pokemon to complete your team.")
        
        while len(self.player.team) < 6:
            clear_screen()
            display_title(f"CATCH POKEMON - {len(self.player.team)}/6")
            
            # Generate 3 random Pokemon options
            options = []
            for _ in range(3):
                pokemon = PokemonGenerator.generate_wild_pokemon(5)
                options.append(pokemon)
            
            print(f"\nWild Pokemon appeared! Choose one to catch:")
            for i, pokemon in enumerate(options, 1):
                print(f"{i}. {pokemon.name} ({pokemon.type_pokemon}) - Lvl.{pokemon.level}")
                print(f"   HP: {pokemon.hp_max} | Attack: {pokemon.attack} | Defense: {pokemon.defense}")
            
            print(f"{len(options) + 1}. Skip (don't catch)")
            
            choice = input("\nYour choice: ").strip()
            
            try:
                choice_index = int(choice) - 1
                if choice_index == len(options):  # Skip option
                    print("\nYou left the Pokemon alone.")
                    input("\nPress Enter to continue...")
                    break
                elif 0 <= choice_index < 3:
                    selected_pokemon = options[choice_index]
                    if self.player.add_pokemon(selected_pokemon):
                        print(f"\n✓ You caught {selected_pokemon.name}!")
                        print(f"   {selected_pokemon.name} was added to your team!")
                        
                        if len(self.player.team) < 6:
                            continue_catching = input("\nCatch another Pokemon? (y/n): ").strip().lower()
                            if continue_catching != 'y':
                                break
                        else:
                            print("\nYour team is now full (6/6)!")
                            input("\nPress Enter to continue...")
                            break
                    else:
                        print("\nYour team is full!")
                        break
                else:
                    print("\nInvalid choice!")
                    input("\nPress Enter to try again...")
            except ValueError:
                print("\nPlease enter a valid number!")
                input("\nPress Enter to try again...")

    def display_arenas(self):
        """Display the status of all arenas"""
        clear_screen()
        display_title("ARENAS STATUS")
        
        for arena in self.arenas:
            status = "**DEFEATED**" if arena in self.defeated_arenas else "**TO CHALLENGE**"
            print(f"\n{status} - {arena.name}")
            print(f"   Type: {arena.type_arena}")
            print(f"   Champion: {arena.champion.name}")
        input("\nPress Enter to return...")

    def main_menu(self):
        """Display the main menu and manage the choices"""

        while self.ongoing:
            clear_screen()
            display_title("MAIN MENU")
            
            print(f"\nTrainer: {self.player.name}")
            print(f"Badges obtained: {len(self.defeated_arenas)}/3")
            
            display_separator()
            
            options = [
                "View my team",
                "Challenge an arena",
                "Catch new Pokemon",
                "Train (random fight)",
                "View the arenas",
                "Quit the game"
            ]

            display_menu(options)
            
            choice = input("\nYour choice : ").strip()
            
            if choice == '1':
                self.display_team()
            elif choice == '2':
                self.choose_and_challenge_arena()
            elif choice == '3':
                self.catch_new_pokemon()
            elif choice == '4':
                self.train_randomly()
            elif choice == '5':
                self.display_arenas()
            elif choice == '6':
                self.quit_game()
            else:
                print("\nInvalid choice !")
                input("\nPress Enter...")
    
    
    
def main():
    """Main function"""
    game = Game()
    game.initialize_game()
    game.main_menu()


if __name__ == "__main__":
    main()