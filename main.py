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