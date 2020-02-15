import json

def initializeData(dbsource):
    with open(f"./inputdata/{dbsource}.json") as json_file:
      data = json.load(json_file)
    return data


def searchableFields(inputmap):
    keys = []
    for entry in inputmap:
       keys += entry.keys()
    return set(keys)


def search(key, value, datasource):
    print (key, value)
    if datasource == "organizations":
        for element in organizations:
           for iter_key, iter_value  in element.items():
              if iter_value == int(value):
                 print(element)

    print("searching....")

def main():
    global organizations
    global tickets
    global users

    organizations=initializeData("organizations")
    tickets=initializeData("tickets")
    users=initializeData("users")

if __name__ == "__main__":
    main()
    

    # print(searchableFields(organizations))

