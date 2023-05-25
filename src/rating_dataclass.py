#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module is used for defining 'rating' dataclass."""
from dataclasses import dataclass
@dataclass
class rating:
    tconst:str
    averageRating:float
    numVotes:int