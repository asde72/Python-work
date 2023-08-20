# Prolog
# Author: Jordan Gaffney
# Email:  jgaffney5@gsu.edu
# Section: 058

def main():
    #SentenceInput
    sentence = input("First sentence?: ").split()
    sentence2 = input("Second sentnce?: ").split()

    #Pairs per line
    for i, e in zip(sentence, sentence2):
        if i != e:
            print(i, e)


main()
