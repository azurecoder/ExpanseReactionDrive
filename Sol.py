from StarType import Star, StarType

class Sol(Star):
    def __init__(self):
        super().__init__("Sol", 1.0, StarType.G)