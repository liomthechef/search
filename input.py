import search
import json
import textwrap
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def welcome():
    print("""---------------------------------------------------------------------------------------------------------
            Welcome to the Zendesk search application, type the menu number and press enter to proceed.
            press o to search organization fields
            Press u to search user fields
            Press t to search ticket fields
            Press h for help
            Press q to quit""")

    i = input()

    if i == "o":
        startSearch("organizations")
    elif i == "u":
        startSearch("users")
    elif i == "t":
        startSearch("tickets")
    elif i == "h":
        help()
    elif i == "q":
        leave()
    else:
        print("Please enter a valid option letter")
        welcome()


def startSearch(datasource):

    searchkeys = search.searchableFields(datasource)

    response = False
    while response is False:
        print(f"\nSearchable fields in {datasource}")
        print(json.dumps(list(searchkeys), indent=2, sort_keys=True))
        print("\n")
        print("please type in a valid search key and press enter to begin, or type q to exit")
        k = input()
        if k == "q":
            leave()
        print("please type in a valid search value and press enter to begin, or type q to exit")
        v = input()
        if v == "q":
            leave()
        if k not in searchkeys:
            print("please type in a valid key and press enter to begin, type quit to exit")
        else:
            response = True
            v = normalizeString(v)
            if datasource == "organizations":
                search.orgSearch(k, v, datasource)
            if datasource == "users":
                search.userSearch(k, v, datasource)
            if datasource == "tickets":
                search.ticketSearch(k, v, datasource)
            welcome()


def normalizeString(v):
    try:
        value = int(v)
    except ValueError:
        value = v
    if v.casefold() == "true" or v.casefold() == "false":
        value = bool(v)
    return value


# It's important to be polite
def leave():
    print("Goodbye, come back soon")
    exit()


def help():
    text = "The Zendesk search option can be used to search users, tickets and organisations by any valid field. "\
           "If you search a user by ID, you will also find the user's tickets and organisation. "\
           "Searching an organisation by ID will return it's users and registered tickets. "\
           "Searching a ticket requires using the submitter, assignee, or organisation ID to return it's associated items."

    wrapper = textwrap.TextWrapper(width=90)
    word_list = wrapper.wrap(text=text)

    for element in word_list:
        print(element)
    print("\n")
    welcome()


if __name__ == "__main__":
    clear()
    search.main()
    welcome()
