#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module consists of runtime function to implement RUNTIME query."""
import Do_sort
import display_output
import time

def runtime(type,starttime,endtime,mov):
    """This function implements RUNTIME query. It has 4 parameters. type refers to the titleType to be checked,
    starttime and endtime refers to the lower and upper limits of the runtime of the movies to be searched,
    and mov is a copy of the mov dictionary in main function. It returns none to the main function. It returns none.
    It calls display_output function for printing the details of movie objects and Do_sort function to sort the movie
    objects passed."""
    start = time.perf_counter()
    start=time.perf_counter()
    print("processing: RUNTIME "+type+" "+starttime+" "+endtime)
    li=list()
    for key in mov.keys():
        if mov[key].runtimeMinutes!='\\N':
            if mov[key].titleType==type and int(mov[key].runtimeMinutes) >= int(starttime) and int(mov[key].runtimeMinutes)<=int(endtime):
                li.append(mov[key])
    if len(li)==0:
        print("\tNo match found!")
    else:
        li=Do_sort.do_sort(li,'primaryTitle')
        li=Do_sort.do_sort(li,'runtimeMinutes',1)
        for i in li:
            display_output.dis(i,0)
    stop=time.perf_counter()
    print("elapsed time (s): "+str(stop-start)+"\n")
