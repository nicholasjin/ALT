class Simulation:
    def __init__(self, duration, profile = {"light": 100, "medium": 0, "heavy": 0}):
        self.duration = duration
        self.profile = [profile["light"], profile["medium"], profile["heavy"]]
        assert sum(self.profile) == 100
        for _ in self.profile:
            assert _ > 0
