class Game:
    """Main class managing the game flow"""
    
    def __init__(self):
        self.player = None
        self.arenes = []
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
        
        # Choice of the starter
        self.choose_starter()
        
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
        fire_champion = Champion("Pierre", "Fire")
        fire_champion.add_pokemon(FirePokemon("Ponyta", level=8))
        fire_champion.add_pokemon(FirePokemon("Goupix", level=10))
        fire_arena = Arena("Fire Arena", "Fire", fire_champion, "Badge Volcan")

        # Water Arena  
        water_champion = Champion("Ondine", "Water")
        water_champion.add_pokemon(WaterPokemon("Stari", level=12))
        water_champion.add_pokemon(WaterPokemon("Psykokwak", level=14))
        water_arena = Arena("Water Arena", "Water", water_champion, "Badge Marine")

        # Plant Arena
        plant_champion = Champion("Erika", "Plant")
        plant_champion.add_pokemon(PlantPokemon("Mystherbe", level=16))
        plant_champion.add_pokemon(PlantPokemon("Chétiflor", level=18))
        plant_arena = Arena("Plant Arena", "Plant", plant_champion, "Badge Vert")

        self.arenas.extend([fire_arena, water_arena, plant_arena])

    # Challenge an arena
   def challenge_arena(self, arena):
        """Start a fight against the arena champion"""
        clear_screen()
        display_title(f"CHALLENGE: {arena.name.upper()}")
        
        print(f"\n{'='*60}")
        print(f"\n🎯 Champion {arena.champion.name} is waiting for you !")
        print(f"⚡ Specialité: Type {arena.type_arena}")
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
                "Train (random fight)",
                "View the arenas",
                "Quit the game"
            ]

            display_menu(options)
            
            choice = input("\nYour choice : ").strip()
            
            if choice == '1':
                self.display_team()
            elif choice == '2':
                self.challenge_arena()
            elif choice == '3':
                self.train_randomly()
            elif choice == '4':
                self.display_arenas()
            elif choice == '5':
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