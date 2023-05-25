#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module contains the main() function."""
import sys

import Most_votes
import Top
import read_files
import lookup
import contains
import year_and_genre
import Runtime

def main():
    """The main function is responsible for calling fileopen() function that decides whether to open small or large
    datasets. I also takes in the input from the user by using sys.stdin. The first element of the list formed by using
    split() is checked in order to call lookup, contains, y_and_g, runtime, most_votes and top function."""

    if len(sys.argv)==2:
        mov, rat=read_files.fileopen_small()
    else:
        mov, rat=read_files.fileopen_large()
    print('\n')


    for line in sys.stdin:
        line = line.strip()         # remove trailing newline
        listinp=line.split(' ')
        if listinp[0]=="LOOKUP":
            lookup.lookup(listinp[1],mov,rat)
        elif listinp[0]=='CONTAINS':
            words=' '.join(listinp[2:])
            contains.contains(listinp[1],words,mov)
        elif listinp[0]=='YEAR_AND_GENRE':
            year_and_genre.y_and_g(listinp[1],listinp[2],listinp[3],mov)
        elif listinp[0]=='RUNTIME':
            Runtime.runtime(listinp[1],listinp[2],listinp[3],mov)
        elif listinp[0]=='MOST_VOTES':
            Most_votes.most_votes(listinp[1],listinp[2],mov,rat)
        elif listinp[0]=='TOP':
            Top.top(listinp[1],listinp[2],listinp[3],listinp[4],mov,rat)




if __name__ == '__main__':
    main()