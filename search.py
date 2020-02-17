import json
import pandas
pandas.set_option('max_colwidth', 100)
pandas.set_option('max_rows', 1000)


def initializeData(dbsource):
    with open(dbsource) as json_file:
        data = json.load(json_file)
    return data


def searchableFields(datasource):
    json_data = globals()[datasource]
    keys = []
    for entry in json_data:
        keys += entry.keys()
    return set(keys)


def orgSearch(key, value, datasource):

    print("searching....")
    for element in organizations:
        org_results = []
        for iter_key, iter_value in element.items():
            if iter_key == key and iter_value == value:
                org_results += element.items()
        if org_results:
            print("\nOrganization result for search:\n")
            dataframe = pandas.DataFrame.from_dict(org_results, orient='columns')
            print(dataframe)

    if key == "_id":
        for element in users:
            user_results = []
            for iter_key, iter_value in element.items():
                if iter_key == "organization_id" and iter_value == value:
                    user_results += element.items()
            if user_results:
                print("\nUser result for search:\n")
                dataframe = pandas.DataFrame.from_dict(user_results, orient='columns')
                print(dataframe)

    if key == "_id":
        for element in tickets:
            ticket_results = []
            for iter_key, iter_value in element.items():
                if iter_key == "organization_id" and iter_value == value:
                    ticket_results += element.items()
            if ticket_results:
                print("\nTicket result for search:\n")
                dataframe = pandas.DataFrame.from_dict(ticket_results, orient='columns')
                print(dataframe)


def userSearch(key, value, datasource):

    print("searching....")
    for element in users:
        user_results = []
        for iter_key, iter_value in element.items():
            if iter_key == key and iter_value == value:
                user_results = element.items()
        if user_results:
            print("\nUser result for search:\n")
            dataframe = pandas.DataFrame.from_dict(user_results, orient='columns')
            print(dataframe)

    if key == "_id":
        for element in tickets:
            ticket_results = []
            for iter_key, iter_value in element.items():
                if iter_key == "submitter_id" and iter_value == value or iter_key == "assignee_id" and iter_value == value:
                    ticket_results += element.items()
            if ticket_results:
                print("\nTicket result for search:\n")
                dataframe = pandas.DataFrame.from_dict(ticket_results, orient='columns')
                print(dataframe)

    if key == "organization_id":
        for element in organizations:
            org_results = []
            for iter_key, iter_value in element.items():
                if iter_key == key and iter_value == value:
                    org_results += element.items()
            if ticket_results:
                print("\nOrganization result for search:\n")
                dataframe = pandas.DataFrame.from_dict(org_results, orient='columns')
                print(dataframe)


def ticketSearch(key, value, datasource):

    print("searching....")
    print(key, value, datasource)
    for element in tickets:
        ticket_results = []
        for iter_key, iter_value in element.items():
            if iter_key == key and iter_value == value:
                ticket_results += element.items()
        if ticket_results:
            print("\nTicket result for search:\n")
            dataframe = pandas.DataFrame.from_dict(ticket_results, orient='columns')
            print(dataframe)

    if key == "submitter_id" or key == "assignee_id":
        for element in users:
            user_results = []
            for iter_key, iter_value in element.items():
                if iter_key == "_id" and iter_value == value:
                    user_results += element.items()
            if user_results:
                print("\nUser result for search:\n")
                dataframe = pandas.DataFrame.from_dict(user_results, orient='columns')
                print(dataframe)

    if key == "organization_id":
        for element in organizations:
            org_results = []
            for iter_key, iter_value in element.items():
                if iter_key == "_id" and iter_value == value:
                    org_results += element.items()
            if org_results:
                print("\nOrganisation result for search:\n")
                dataframe = pandas.DataFrame.from_dict(org_results, orient='columns')
                print(dataframe)


def main():
    global organizations
    global tickets
    global users

    organizations = initializeData("./inputdata/organizations.json")
    tickets = initializeData("./inputdata/tickets.json")
    users = initializeData("./inputdata/users.json")


if __name__ == "__main__":
    main()
