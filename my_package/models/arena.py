class Arena:
    def __init__(self, name, type, champion, badge):
        self.name = name
        self.type = type
        self.champion = champion
        self.badge = badge
    
    #def __repr__(self):
    #    return "" % (self.name,)
    
    def __str__(self):
        return f"Duel dans l'arene {self.name} de type ({self.type}) pour affronter le champion {self.champion}, pour recuperer le badge :\n {self.badge})"