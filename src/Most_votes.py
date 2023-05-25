#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module is used to implement MOST_VOTES query and has most_votes function."""
import Do_sort
import display_output
import time

def most_votes(type,no,mov,rat):
    """This function is responsible for performing MOST_VOTES Query. It calls Do_sort function for sorting the objects
    passed. This function consists of four parameter. type refers to the titleType to be checked. no refers to the
    total number of movies to be displayed, mov and rat are copies of mov and rat dictionaries from main function.
    It also calls display_output function for printing the details of movie objects."""
    start = time.perf_counter()
    start=time.perf_counter()
    print("processing: MOST_VOTES "+type+" "+no)
    li=list()
    li2=list()
    c=1
    no=int(no)
    for key in mov.keys():
        if key in rat.keys():
            if mov[key].titleType==type:
                li.append(mov[key])
    if len(li)==0:
        print("\tNo match found!")
    else:
        li=Do_sort.do_sort(li,'primaryTitle')
        for i in li:
            li2.append(rat[i.tconst])
        li2=Do_sort.do_sort(li2,'numVotes',1)

        for j in li2:
            no=no-1
            if no>=0:
                print("\t"+str(c)+". VOTES: "+str(j.numVotes)+", MOVIE: ",end="")
                display_output.dis(mov[j.tconst],1)
                c=c+1
    stop=time.perf_counter()
    print("elapsed time (s): "+str(stop-start)+"\n")
