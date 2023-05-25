#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module is used for dis function that prints the objects passed to it."""
def dis(obj,dummy):
    """ This function has two arguments. obj is the movie object that is passed to print and dummy variable decides how
    it should be printed. This function only returns none."""
    if dummy==1:
        x=""
    else:
        x="\t"
    print(x+"Identifier: " + str(obj.tconst) + ", Title: " + str(obj.primaryTitle) + ", Type: ", end="")
    print(str(obj.titleType) + ", Year: ", end="")
    if obj.startYear == '\\N':
        print(0, end="")
    else:
        print(str(obj.startYear), end="")
    if obj.runtimeMinutes == '\\N':
        print(", Runtime: " + str(0), end="")
    else:
        print(", Runtime: " + str(obj.runtimeMinutes), end="")
    if obj.genres == '\\N':
        print(", Genres:" + str(None))
    else:
        print(", Genres: " + str(obj.genres))
