class Arena:
    def __init__(self, name, type, champion, badge):
        self.name = name
        self.type = type
        self.champion = champion
        self.badge = badge
    
    #def __repr__(self):
    #    return "" % (self.name,)
    
    def __str__(self):
        return f"Challenge in arena {self.name} from type ({self.type}) to defy champion {self.champion}, and fetch badge :\n {self.badge})"