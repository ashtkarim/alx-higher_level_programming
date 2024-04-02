#!/usr/bin/python3
""" Find a peak module """


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] > list_of_integers[i - 1] \
         and list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
    return list_of_integers[0] \
        if list_of_integers[0] > list_of_integers[-1] else list_of_integers[-1]
