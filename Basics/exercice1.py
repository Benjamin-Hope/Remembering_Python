# this is to try out some exercices

# Exercice 1
word = ["Hello World!", "Radar", "Mama?", "Madam, I'm Adam.",
        "Race car!"]

# for i in word:
# print(i)
# print(i[::-1])
# value = True if (i == i[::-1]) else False
# print(value)

# this will return false because of the lower cases, spaces and punctuations.
# lets make a function that solves all this.


def fixer(my_list):
    global new
    new = my_list
    position = 0
    # make them lower
    for i in my_list:
        print(position)
        new[position] = i.lower()  # --> 'lower()'
        # ignore punctuation
        # ---> 'isalnum' is a function of python that checks if its alphanumeric == letter.
        new_word = ""  # creates a new word
        for j in new[position]:
            if j.isalnum():
                new_word += j  # if its not a letter this will not happen
                # print(new_word)
            new[position] = new_word
        position = position + 1


def selector(list_value):
    x = 0
    for i in list_value:
        x = x+1 if i == i[::-1] else x+0
    return x


def main():

    fixer(word)
    print(selector(new))


if __name__ == "__main__":
    main()
