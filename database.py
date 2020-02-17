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
                                    active text,
                                    verified text,
                                    shared text,
                                    locale text,
                                    timezone text,
                                    last_login_at text,
                                    email text,
                                    phone text,
                                    signature text,
                                    organization_id integer,
                                    tags text,
                                    suspended text,
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
                                    has_incidents text,
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
                                    details text,
                                    shared_tickets text,
                                    tags text
                                );"""


    create_table(conn, create_organizations)
    create_table(conn, create_users)
    create_table(conn, create_tickets)

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
        ### SQL statements in python with dynamic values is a bit unfortunate.
        sql = f'''INSERT INTO {table}({(",".join(map(str, keylist)))}) VALUES({(",".join(map(str, valuelength)))})'''
        print (sql)
        with conn:
            conn.set_trace_callback(print)
            cur = conn.cursor()
            cur.execute(sql, valuelist)

def main():
    global conn 
    conn = create_connection()

    conn.set_trace_callback(print)
    configure_tables(conn)
    initialize_table(conn, "organizations")
    initialize_table(conn, "tickets")
    initialize_table(conn, "users")

if __name__ == '__main__':
    main()
