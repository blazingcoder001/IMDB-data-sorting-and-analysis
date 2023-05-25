#Done by Jishnuraj Prakasan , RIT username:jp4154
"""This module consists of do_sort function to sort objects"""
import operator


def do_sort(lis,k,ch=0):
    """This function has three parameters. lis is the list element that is to be sort which is basically objects
      of movie dataclass. k determines the field with which the sorting is to be done. ch has been assigned 0 for
      automatic ascending order sorting. If its passed 1, descending order will be followed. This function returns
      the sorted list."""
    if ch==0:
        lis.sort(key=operator.attrgetter(k))
        return lis
    else:
        lis.sort(key=operator.attrgetter(k),reverse=True)
        return lis

