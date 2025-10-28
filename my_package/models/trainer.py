class Trainer:
    def __init__(self, name, age, gender, pokemon_list):
        self.name = name
        self.age = age
        self.gender = gender
        self.pokemon = pokemon_list

    def __str__(self):
        return f" Voici {self.name} de ({self.age}) ans - {self.gender}, avec sa teamn :\n {self.pokemon})"
