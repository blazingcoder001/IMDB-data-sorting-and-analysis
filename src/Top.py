#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module has top function used to implement the TOP query."""

import Do_sort
import display_output
import time

def top(type,num,start,end,mov,rat):
    """ This function consists of 6 parameters. type refers to the titleType to be checked. num refers to the number of
    output to be displayed in each year, start and end refers to the lower and upper limits of years in which we have to
     find the solution, mov and rat are the copies of mov and rat dictionaries from the main function. This function
     calls Do_sort function and display_output function. Also, this function returns none."""
    starttime=time.perf_counter()
    print("processing: TOP "+type+" "+num+" "+start+" "+end)
    li=list()
    li2=list()
    k=int(num)
    for i in range(int(start),int(end)+1):
        print("\tYEAR: "+ str(i))
        for key in mov.keys():
            if key in rat.keys():
                if mov[key].startYear==str(i) and rat[key].numVotes>=1000 and mov[key].titleType==type:
                        li.append(mov[key])
        if len(li)!=0:
            li=Do_sort.do_sort(li,'primaryTitle')
            for i in li:
                li2.append(rat[i.tconst])
            li2=Do_sort.do_sort(li2,'numVotes',1)
            li2=Do_sort.do_sort(li2,'averageRating',1)
            for j in range(0,len(li2)):
                k = k - 1
                if k >= 0:
                    print("\t\t" + str(j+1) + ". RATING: " + str(li2[j].averageRating) + ", VOTES: ", end="")
                    print(str(li2[j].numVotes)+", MOVIE: ",end="")
                    display_output.dis(mov[li2[j].tconst],1)
            li.clear()
            li2.clear()
            k=int(num)
        else:
            print("\t\tNo match found!")
    stoptime=time.perf_counter()
    print("elapsed time (s): "+str(stoptime-starttime)+"\n")

