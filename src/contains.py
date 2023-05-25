#Done by Jishnuraj Prakasan , RIT username:jp415
"""This module consists of contains function to perform CONTAINS query."""
import time
import display_output
def contains(titletype,words,mov):
    """This function is used to perform CONTAINS query. IT has three parameters: titleType, words to check and
    the dictionary mov. titleType is a member of class movies in movies_dataclass and mov is a dictionary whose values
    are the objects of class movie. This function returns none to the main. It calls display_output function for
     printing the details of movie objects."""
    start = time.perf_counter()
    start=time.perf_counter()
    x=0
    print("processing: CONTAINS " + titletype + " " + words)
    for key in mov.keys():
        if mov[key].titleType==titletype and words in mov[key].primaryTitle:
            display_output.dis(mov[key],0)
            x=1
    if x==0:
        print("\t No match found!")
    stop=time.perf_counter()
    print("elapsed time (s): "+str(stop-start))
    print('\n')




