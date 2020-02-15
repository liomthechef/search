import search
import pprint
import json

def welcome():
    print("""Welcome to the Zendesk search application type the menu number and press enter to proceed
            press o to search organization fields
            Press u to search user fields
            Press t to search ticket fields
            Press q to quit""")

    i = input()

    if i == "o":
       startSearch("organizations")
    elif i == "u":
       startSearch("users")
    elif i == "t":
       startSearch("tickets")
    elif i == "q":
        leave()
    else:
        print("Please enter a valid option letter")
        welcome()

def startSearch(datasource):
    
    if datasource  == "organizations":
       searchkeys=search.searchableFields(search.organizations)
    if datasource  == "users":
       searchkeys=search.searchableFields(search.users)
    if datasource  == "tickets":
       searchkeys=search.searchableFields(search.tickets)
    
    response = False
    while response == False:
        print (f"\nSearchable fields in {datasource}")
        print (json.dumps(list(searchkeys), indent=2, sort_keys=True))
        print ("\n")
        print ("please type in a valid search key and press enter to begin, or type q to exit")
        k = input()
        if k == "q":
            leave()
        print ("please type in a valid search value and press enter to begin, or type q to exit")
        v = input()
        if v == "q":
            leave()
        if k not in searchkeys:
            print ("please type in a valid key and press enter to begin, type quit to exit")
            response == False
        else:
            response == True
            v = normalizeString(v)
            if datasource  == "organizations":
               search.orgSearch(k, v, datasource)
            if datasource  == "users":
               search.userSearch(k, v, datasource)              
            if datasource  == "tickets":
               search.ticketSearch(k, v, datasource)             
            welcome()

### This isn't great but the python input parses user input as a string, breaking the comparison later
### The alternative being to transform all the input data to strings as loaded, which is very slow.
### There's no doubt a better way to do this but I like my weekend :)
def normalizeString(v):
    try:
        value = int(v)
    except ValueError:
        value = v
    if v.casefold() ==  "true" or v.casefold() == "false":
        value = bool(v)
    return value

### It's important to be polite  
def leave():
    print("Goodbye, come back soon")
    exit()

if __name__ == "__main__":
    search.main()
    welcome()
