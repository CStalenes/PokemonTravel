class Trainer:
    def __init__(self, name, age, gender, pokemon_list):
        self.name = name
        self.age = age
        self.gender = gender
        self.pokemon = pokemon_list

    def __str__(self):
        return f" There is {self.name} to ({self.age}) year old - {self.gender}, with as teamn :\n {self.pokemon})"
