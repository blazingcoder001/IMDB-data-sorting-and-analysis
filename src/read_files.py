#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module has the methods for reading files from small and large data sets.These are fileopen_small and
fileopen_large respectively."""
import time
import movies_dataclass
import rating_dataclass
def fileopen_small():
    """This function is used for reading data from small.basics.tsv and small.ratings.tsv. It doesn't have any
    parameters. It returns the corresponding dictionaries to the main function where they are stored in mov and rat
    respectively. This function also finds the total number of movies and ratings in the given dataset."""
    dict_sm_mov=dict()
    print("reading small.basics.tsv into dict...")
    cou=0
    start=time.perf_counter()
    with open('data/small.basics.tsv',encoding='utf-8') as file:
        for line in file:
            line=line.strip()
            read_list=line.split('\t')
            if read_list[4]=='0':
                cou = cou + 1
                if read_list[7]!='\\N':
                    dict_sm_mov[read_list[0]]=movies_dataclass.movies(tconst=read_list[0],titleType=read_list[1],
                                                                      primaryTitle=read_list[2], startYear=read_list[5],
                                                                      runtimeMinutes=int(read_list[7]),genres=read_list[8])
                else:
                    dict_sm_mov[read_list[0]] = movies_dataclass.movies(tconst=read_list[0], titleType=read_list[1],
                                                                        primaryTitle=read_list[2],
                                                                        startYear=read_list[5],
                                                                        runtimeMinutes=0,
                                                                        genres=read_list[8])

    stop=time.perf_counter()
    cou1=cou
    print("elapsed time(s)"+str(stop-start))
    print("\n")



    dict_sm_rat=dict()
    print("reading small.ratings.tsv into dict")
    cou=0
    start=time.perf_counter()
    with open("data/small.ratings.tsv", encoding='utf-8') as file:
        for line in file:
            line=line.strip()
            read_list_2=line.split('\t')
            if read_list_2[0] in dict_sm_mov.keys():
                cou=cou+1
                if read_list_2[2] != '\\N':
                    dict_sm_rat[read_list_2[0]]=rating_dataclass.rating(tconst=read_list_2[0],averageRating=float(read_list_2[1]),
                                                                        numVotes=int(read_list_2[2]))
                else:
                    dict_sm_rat[read_list_2[0]] = rating_dataclass.rating(tconst=read_list_2[0],
                                                                          averageRating=float(read_list_2[1]),
                                                                          numVotes=0)

    stop=time.perf_counter()
    cou2=cou
    print("elapsed time(s)"+str(stop-start))
    print("\n")
    print("Total movies: "+str(cou1))
    print("Total ratings: "+str(cou2))

    return dict_sm_mov, dict_sm_rat

def fileopen_large():
    """This function is used for reading data from title.basics.tsv and title.ratings.tsv. It doesn't have any
        parameters. It returns the corresponding dictionaries to the main function where they are stored in mov and rat
        respectively. This function also finds the total number of movies and ratings in the given dataset."""
    dict_la_mov = dict()
    print("reading title.basics.tsv into dict...")
    cou = 0
    start = time.perf_counter()
    with open('data/data/title.basics.tsv', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            read_list = line.split('\t')
            if read_list[4] == '0' :
                cou = cou + 1
                if read_list[7] != '\\N':
                    dict_la_mov[read_list[0]] = movies_dataclass.movies(tconst=read_list[0],titleType=read_list[1],
                                                                        primaryTitle=read_list[2],startYear=read_list[5],
                                                                        runtimeMinutes=int(read_list[7]),genres=read_list[8])
                else:
                    dict_la_mov[read_list[0]] = movies_dataclass.movies(tconst=read_list[0], titleType=read_list[1],
                                                                        primaryTitle=read_list[2],
                                                                        startYear=read_list[5],
                                                                        runtimeMinutes=0,
                                                                        genres=read_list[8])

    stop = time.perf_counter()
    print("elapsed time(s)" + str(stop - start))
    cou1=cou

    dict_la_rat = dict()
    print("reading title.ratings.tsv into dict")
    cou = 0
    start = time.perf_counter()
    with open("data/data/title.ratings.tsv", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            read_list_2 = line.split('\t')
            if read_list_2[0] in dict_la_mov.keys():
                cou = cou + 1
                if read_list_2[2] != '\\N':
                    dict_la_rat[read_list_2[0]] = rating_dataclass.rating(tconst=read_list_2[0],averageRating=float(read_list_2[1]),
                                                                          numVotes=int(read_list_2[2]))
                else:
                    dict_la_rat[read_list_2[0]] = rating_dataclass.rating(tconst=read_list_2[0],
                                                                          averageRating=float(read_list_2[1]),
                                                                          numVotes=0)

    stop = time.perf_counter()
    cou2 = cou
    print("elapsed time(s)" + str(stop - start))
    print("\n")
    print("Total movies: " + str(cou1))
    print("Total ratings: " + str(cou2))
    return dict_la_mov, dict_la_rat