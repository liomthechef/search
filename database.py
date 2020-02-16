import sqlite3
import json
from sqlite3 import Error
 
 
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def configure_tables(conn):
    create_users = """ CREATE TABLE IF NOT EXISTS users (
                                    _id integer PRIMARY KEY,
                                    url text,
                                    external_id text,
                                    name text,
                                    alias text,
                                    created_at text,
                                    active integer,
                                    verified integer,
                                    shared integer,
                                    locale text,
                                    timezone text,
                                    last_login_at text,
                                    email text,
                                    phone text,
                                    signature text,
                                    organization_id integer,
                                    tags text,
                                    suspended integer,
                                    role text,
                                    FOREIGN KEY (organization_id) REFERENCES organizations (_id)
                                    ); """

    create_tickets = """CREATE TABLE IF NOT EXISTS tickets (
                                    _id text PRIMARY KEY,
                                    url text,
                                    external_id text,
                                    created_at text,
                                    type text,
                                    subject text,
                                    description text,
                                    priority integer,
                                    status text,
                                    submitter_id integer,
                                    assignee_id integer,
                                    organization_id integer,
                                    tags text,
                                    has_incidents integer,
                                    due_at text,
                                    via text,
                                    FOREIGN KEY (assignee_id) REFERENCES users (_id)
                                    FOREIGN KEY (submitter_id) REFERENCES users (_id)
                                    FOREIGN KEY (organization_id) REFERENCES organizations (_id)
                                );"""

    create_organizations = """CREATE TABLE IF NOT EXISTS organizations (
                                    _id integer PRIMARY KEY,
                                    url text NOT NULL,
                                    external_id text,
                                    name text NOT NULL,
                                    domain_names text NOT NULL,
                                    created_at text NOT NULL,
                                    details text NOT NULL,
                                    shared_tickets text,
                                    tags text
                                );"""


    create_table(conn, create_organizations)
    create_table(conn, create_users)
    create_table(conn, create_tickets)

def initialize_organizations(conn):
    with open("./inputdata/organizations.json") as json_file:
      data = json.load(json_file)

    sql = '''INSERT INTO organizations(_id,url,external_id,name,domain_names,created_at,details,shared_tickets,tags) VALUES(?,?,?,?,?,?,?,?,?)'''
    for element in data:
        valuelist = []
        for iter_key, iter_value in element.items():
            valuelist.append(str(iter_value))
        with conn:
            cur = conn.cursor()
            cur.execute(sql, valuelist)

    cur.execute("SELECT * FROM organizations;")
    print(cur.fetchall())

def initialize_tickets(conn):
    with open("./inputdata/tickets.json") as json_file:
      data = json.load(json_file)

    
    for element in data:
        keylist = []
        valuelist = []
        valuelength = []
        for iter_key, iter_value in element.items():
            keylist.append(str(iter_key))
            valuelist.append(str(iter_value))
            valuelength += "?"
        print (valuelength)

        sql = f'''INSERT INTO tickets({(",".join(map(str, keylist)))}) VALUES({(",".join(map(str, valuelength)))})'''
        print (sql)
        with conn:
            conn.set_trace_callback(print)
            cur = conn.cursor()
            cur.execute(sql, valuelist)

    cur.execute("SELECT * FROM tickets;")
    print(cur.fetchall())

def initialize_table(conn, table):
    with open(f"./inputdata/{table}.json") as json_file:
      data = json.load(json_file)


    for element in data:
        keylist = []
        valuelist = []
        valuelength = []
        for iter_key, iter_value in element.items():
            keylist.append(str(iter_key))
            valuelist.append(str(iter_value))
            valuelength += "?"

        sql = f'''INSERT INTO {table}({(",".join(map(str, keylist)))}) VALUES({(",".join(map(str, valuelength)))})'''
        print (sql)
        with conn:
            conn.set_trace_callback(print)
            cur = conn.cursor()
            cur.execute(sql, valuelist)

def main():
    conn = create_connection()
    conn.set_trace_callback(print)
    configure_tables(conn)
    initialize_table(conn, "organizations")
    initialize_table(conn, "tickets")
    initialize_table(conn, "users")

if __name__ == '__main__':
    main()
