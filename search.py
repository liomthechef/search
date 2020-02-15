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
    
    searchorder = ["tickets", "organizations", "users"]
    ## searching inputted order first
    searchorder.insert(0,searchorder.pop(searchorder.index(datasource))) 

    results = ""
    print("searching....")

    for datasource in searchorder:
        for element in globals()[datasource]:
            for iter_key, iter_value  in element.items():
                if iter_key == key and iter_value == value:
                    results += json.dumps(element, indent=2)
    print(results)

def main():
    global organizations
    global tickets
    global users

    organizations=initializeData("organizations")
    tickets=initializeData("tickets")
    users=initializeData("users")

if __name__ == "__main__":
    main()


