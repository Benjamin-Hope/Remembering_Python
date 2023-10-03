# Here we will look over some basic file operations


def main():
    # -- lets start by opening a file and creating if it does not exist
    # -- we need to define the name of the file and the mode we want to use w -> write w+ -> write and create if does not exist
    myfile = open("mytext.txt", "w+")

    # to write something in our file we we use the '.write()' command:
    for i in range(10):
        myfile.write("this is line:\t" + str(i) + "\n")

    # after finished writing it is always a good practice to close the files:
    myfile.close()

    # to add something to an existing file we just need to use the 'a+' command on the definition of the file
    # this means 'append', which informs that we will add to the file not overwrite it
    myfile2 = open("mytext.txt", "a+")  # 'a+' --> append
    myfile2.write("\nThis is altering the file not overwriting it")
    myfile2.close()

    # lets read and access files: bust define the aspect as 'r' --> read
    file3 = open("mytext.txt", "r")
    # -- it is a good habit to check if the file has been correctly opened.
    if file3.mode == 'r':
        print("correctly opened in: ", file3.mode)
        # now lets read our files
        content = file3.read()
        print(content)
        file3.close  # ------>if we are reading the file this is not necessary, only when altering it

        # lets read and access files: bust define the aspect as 'r' --> read
    file4 = open("mytext.txt", "r")
    # -- it is a good habit to check if the file has been correctly opened.
    if file4.mode == 'r':
        print("correctly opened in: ", file4.mode)
        # we can also read lines to be easier to see.
        fl = file4.readlines()
        for x in fl:  # -----> for each line...
            print(x)
        # file3.close  # ------>if we are reading the file this is not necessary, only when altering it


if __name__ == "__main__":
    main()
