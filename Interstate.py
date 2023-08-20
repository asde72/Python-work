def new_func():
    # function for lab 5
    highway = int(input("What road are you looking for?"))
    intersate = highway % 100 #used to get last two digits of number
    if(0 < highway < 100): #main highway
        if(highway % 2 == 0):
            print("east/west")
            print("I-",highway, "Is primary going east/west")
        else:
            print("north/south")
            print("I-",highway,"Is primary going north/south")
            #auxillary highway cant equal the an even hundered because there is no intersate 0
    elif(99< highway < 1000 and intersate != 0):
        if(highway %2 == 0):
            print(" aux east/west")
            print("I-",highway,"serving I-",intersate, "Is auxillary going east/west")
        else:
            print ("aux north/south")
            print("I-",highway,"serving I-",intersate, "Is auxillary going north/south")
    else:
        print("Not a valid interstate")

new_func()