class CombatLog:
    """
    The CombatLog class describes a sequence of events. An "event" is one of the
    following:
    0. Initial fleet/target configuration
    1. A weapon being fired/launched
    2. Damage registering (Source)
    3. Buffs/debuffs being applied/unapplied

    """
    def __init__(self, fleet, target):
        self.fleet = fleet
        self.target = target
