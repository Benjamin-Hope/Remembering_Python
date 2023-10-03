# we will see how to access the information of a file

import os  # this imports the lib of operation systems
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # print the name of the os:
    print(os.name)  # -- internally the official name of windows is 'nt'

    # to check if an item exists we can run  'path.exists("")'
    print("this text files exists?: ", path.exists("mytext.txt"))
    # we can also get information on the type of the file
    print("file?: ", path.isfile("mytext.txt"))
    print("directory?: ", path.isdir("mytext.txt"))

    # we should know the file full path, for this we run:
    print("mytext.txt: ", path.realpath("mytext.txt"))
    # we can use the function 'split' to separate the file name from the path
    # this returns the path and after that the name of the file in a tuple
    print(path.split(path.realpath("mytext.txt")))

    # we can access the modification time of a file using:
    mytime = time.ctime(path.getmtime("mytext.txt"))
    print("\n", mytime)

    # We can also calculate how long the file exists for, by doing:
    time_now = datetime.datetime.now()  # this provides the current time
    diff = time_now - \
        datetime.datetime.fromtimestamp(path.getmtime(
            "mytext.txt"))  # this is a time delta or a space of time
    print(diff)
    # for better visualization we can see this in seconds:
    # --> 'total_seconds()' converts the previous value to seconds
    print("\n", diff.total_seconds())


if __name__ == "__main__":
    main()
