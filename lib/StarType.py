from enum import Enum
import math

class StarType(Enum):
    """
    Basic spectral classes of stars in cosmology/astronomy, 
    roughly ordered from hottest (O-type) to coolest (M-type).
    """
    O = "O-type (very hot, blue stars)"
    B = "B-type (blue-white stars)"
    A = "A-type (white stars)"
    F = "F-type (yellow-white stars)"
    G = "G-type (yellow stars like the Sun)" 
    K = "K-type (orange stars)" 
    M = "M-type (red stars, includes most red dwarfs)"  # Coolest stars