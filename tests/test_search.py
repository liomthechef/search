import search


def test_org():
    organizations = search.initializeData("./testdata/organizations.json")
    key = "_id"
    value = 101
    match = False
    for element in organizations:
        for iter_key, iter_value in element.items():
            print(iter_key)
            print(iter_value)
            if iter_key == key and iter_value == value:
                match = True

    if match is True:
        print("org data test pass")
    else:
        raise Exception


def test_tickets():

    tickets = search.initializeData("./testdata/tickets.json")

    key = "external_id"
    value = "3e5ca820-cd1f-4a02-a18f-11b18e7bb49a"
    match = False
    for element in tickets:
        for iter_key, iter_value in element.items():
            print(iter_key)
            print(iter_value)
            if iter_key == key and iter_value == value:
                match = True

    if match is True:
        print("tickets data test pass")
    else:
        raise Exception


def test_users():

    users = search.initializeData("./testdata/users.json")

    key = "signature"
    value = "Don't Worry Be Happy!"
    match = False
    for element in users:
        for iter_key, iter_value in element.items():
            print(iter_key)
            print(iter_value)
            if iter_key == key and iter_value == value:
                match = True

    if match is True:
        print("users data test pass")
    else:
        raise Exception
