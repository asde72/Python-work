# Prolog
# Author:  Jordan Gaffney
# Email:  jgafffney5@gsu.edu
# Section: 058


def main():
    #Create the list of contacts from an input
    contact_list = input("Enter word pairs that have a name and a phone number (both strings), separated by a comma.").split()

    #List of pairs
    contacts = { }
    for unique_pairs in contact_list:
        names, phone_num = unique_pairs.split(',')
        contacts[names] = phone_num

    #Display the listed name from the corresponding phone number
    search_name = input('What name would you like the number to be associated with?: ').strip()
    print(contacts[search_name])


main()
