import search
import pprint

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
        print (searchkeys)
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
            search.search(k, v, datasource)
            welcome()
        
    
def leave():
    print("Goodbye, come back soon")
    exit()

if __name__ == "__main__":
    search.main()
    welcome()


    
    


# import json

# def search():

#     with open('./data/organizations.json') as json_file:
#         data = json.load(json_file)
#         for o in data:
#             print(o)

# if __name__ == "__main__":
#     print(search())
