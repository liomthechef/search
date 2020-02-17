import sqlite3
import json
import database
import pandas as pd
from sqlite3 import Error
 
def query_columns(datasource):
    conn = database.conn

    query_cur = conn.cursor()
    query_cur.execute(f"SELECT * FROM {datasource};")
    col_name_list = [tuple[0] for tuple in query_cur.description]

    return col_name_list
    
def search_columns(key, value, datasource):
    conn = database.conn
    query_cur = conn.cursor()
    query_cur.execute("SELECT * FROM {tn} WHERE {cn}='{cv}' COLLATE NOCASE".\
            format(tn=datasource, cn=key, cv=value))
    id_exists = query_cur.fetchall()
    print(id_exists)

    return id_exists

def search_id_user(key, value, datasource):
    conn = database.conn
    query_cur = conn.cursor()
    query_cur.execute("SELECT * FROM users INNER JOIN tickets ON users._id = tickets.assignee_id WHERE users._id={cv} COLLATE NOCASE".\
            format(tn=datasource, cn=key, cv=value))
    id_exists = query_cur.fetchall()
    print(pd.DataFrame(id_exists))
    return id_exists


def main():
   database.main() 
   database.conn

