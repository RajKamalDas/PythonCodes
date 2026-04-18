class Player:
    def __init__(self):
        # First default:
        self.level = 1
        self.name = "Player"
        self.petID = -1
        self.tool = -1
        self.stats = [50, (1, 3), 5, 10, 10, 0] # HP, Dmg, Sanity, crit, dodge, armour
        self.effects = [0, (0, 0), 0, 0, 0, 0] # For in game changes
        self.curHP = 40
        self.curSanity = 3
        self.invLim = 10
        self.inv = [0 for i in range(self.invLim)]
        self.loc = (0, 0)
        # Then load everything