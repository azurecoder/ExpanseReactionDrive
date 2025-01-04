from enum import Enum

class PlanetType(Enum):
    TERRESTRIAL = "Rocky planet (like Earth or Mars)"
    GAS_GIANT = "Gas giant (like Jupiter or Saturn)"
    ICE_GIANT = "Ice giant (like Uranus or Neptune)"
    DWARF_PLANET = "Small, non-satellite body (like Pluto or Ceres)"
    HOT_JUPITER = "Gas giant orbiting very close to its star"
    SUPER_EARTH = "Planet larger than Earth but smaller than Neptune"
    MINI_NEPTUNE = "Planet smaller than Neptune but bigger than Earth"
    OCEAN_WORLD = "Possible planet with significant surface or subsurface oceans"