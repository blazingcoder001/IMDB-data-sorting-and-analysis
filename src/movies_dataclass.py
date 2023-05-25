#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module is used for defining a dataclass called 'movies'"""
from dataclasses import dataclass
@dataclass
class movies:
    tconst:str
    titleType:str
    primaryTitle:str
    startYear:str
    runtimeMinutes:int
    genres:str