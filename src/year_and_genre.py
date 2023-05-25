#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module consists of y_and_g function used for implementing YEAR_AND_GENRE query."""
import time
import Do_sort
import display_output


def y_and_g(type,year,genre,movcpy):
    """This function consists of 4 parameters type refers to the titleType of movies class. year refers to the year
    to be checked , genre refers to the genre to be checked and movcpy is the copy of the dictionary mov from the main
    function. This function returns none to the main function. This function calls Do_sort function to sort objects and
    It calls display_output function for printing the details of movie objects."""
    start = time.perf_counter()
    start = time.perf_counter()
    print("processing: YEAR_AND_GENRE "+type+" "+year+" "+genre)
    li=list()
    for key in movcpy.keys():
        if movcpy[key].startYear==year and genre in movcpy[key].genres and movcpy[key].titleType==type:
            li.append(movcpy[key])
    if len(li)==0:
        print("\tNo match found!")
    else:
        li= Do_sort.do_sort(li,'primaryTitle')
        for i in li:
            display_output.dis(i, 0)

    stop = time.perf_counter()
    print("elapsed time (s): "+str(stop-start)+"\n")


