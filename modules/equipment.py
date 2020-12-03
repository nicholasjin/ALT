class Equipment:
    def __init__(self, type, weapon_stats = None, plus_stats, effects):
        self.type = type
        if weapon_stats:
            self.weapon_stats = weapon_stats
        self.plus_stats = plus_stats
        self.effects = effects
