import json

from dataclasses import dataclass



def initializeData(dbsource):
    with open(dbsource) as json_file:
      data = json.load(json_file)
    return data


def searchableFields(inputmap):
    keys = []
    for entry in inputmap:
       keys += entry.keys()
    return set(keys)


def orgSearch(key, value, datasource):
    
    results = ""
    print("searching....")
    for element in organizations:
        for iter_key, iter_value  in element.items():
            if iter_key == key and iter_value == value:
                results += json.dumps(element, indent=2)

    if key == "_id":
        for element in users:
            for iter_key, iter_value  in element.items():
                if iter_key == "organization_id" and iter_value == value:
                    results += json.dumps(element, indent=2)

    if key == "_id":
        for element in tickets:
            for iter_key, iter_value  in element.items():
                if iter_key == "organization_id" and iter_value == value:
                    results += json.dumps(element, indent=2)

    print(results)

def userSearch(key, value, datasource):
    
    results = ""
    print("searching....")
    for element in users:
        for iter_key, iter_value in element.items():
            if iter_key == key and iter_value == value:
                results += json.dumps(element, indent=2)

    if key == "_id":
        for element in tickets:
            for iter_key, iter_value in element.items():
                if iter_key == "submitter_id" and iter_value == value or iter_key == "assignee_id" and iter_value == value:
                    results += json.dumps(element, indent=2)

    if key == "organization_id":
        for element in organizations:
            for iter_key, iter_value in element.items():
                if iter_key == key and iter_value == value:
                    results += json.dumps(element, indent=2)

    print(results)

def ticketSearch(key, value, datasource):
    
    results = ""
    print("searching....")
    for element in tickets:
        for iter_key, iter_value in element.items():
            if iter_key == key and iter_value == value:
                results += json.dumps(element, indent=2)

    if key == "submitter_id" or key == "assignee_id":
        for element in users:
            for iter_key, iter_value  in element.items():
                if iter_key == "_id" and iter_value == value:
                    results += json.dumps(element, indent=2)

    if key == "organization_id":
        for element in organizations:
            for iter_key, iter_value  in element.items():
                if iter_key == "_id" and iter_value == value:
                   results += json.dumps(element, indent=2)
    print(results)

def main():
    global organizations
    global tickets
    global users

    organizations=initializeData("./inputdata/organizations.json")
    tickets=initializeData("./inputdata/tickets.json")
    users=initializeData("./inputdata/users.json")

if __name__ == "__main__":
    main()


