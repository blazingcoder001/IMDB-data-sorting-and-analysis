#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module contains lookup function."""
from dataclasses import dataclass

import display_output
import movies_dataclass
import rating_dataclass
import time
import read_files
def lookup(id,mov,rat):
    """The lookup function has three parameters: the id to be checked with the key of the dictionary, mov and rat
    are copy of mov and rat dictionaries from main function. This function returns none. It calls display_
    output function for printing the details of movie objects."""
    start = time.perf_counter()
    print("processing: LOOKUP "+str(id))
    if id in mov.keys() and id in rat.keys():
        if rat[id].averageRating!='\\N':
            print("\tMOVIE: ",end="")
            display_output.dis(mov[id],1)
            print("\tRATING: Identifier: "+str(id)+", Rating:"+str(rat[id].averageRating)+", Votes: ",end="")
            print(rat[id].numVotes)
    else:

        print("\tMovie not found!")
        print("\tRating not found!")
    stop=time.perf_counter()
    et=stop-start
    print("elapsed time (s): "+str(et))
    print('\n')


