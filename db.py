# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:08:52 2020

@author: caleb
"""

import os
import psycopg2

conn = ''
cursor = ''
def log_mes():
    return "輸入“存入”開始存入親戚資訊\n輸入“查詢”開始查詢親戚資訊\n輸入“更新”以更新親戚資訊\n輸入“刪除”以刪除親戚資訊"

def db_init():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

def create_table():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    delete_table_query = '''DROP TABLE IF EXISTS rel_db'''
    cursor.execute(delete_table_query)
    conn.commit()

    create_table_query = '''CREATE TABLE rel_db(
                        record_no serial PRIMARY KEY,
                        user_id VARCHAR (50) NOT NULL,
                        name VARCHAR (50) NOT NULL,
                        rel_info VARCHAR (50) NOT NULL
                        );'''    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def insert(user_id,name,rel):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    table_columns = '(user_id,name,rel_info)'
    records= (user_id,name,rel)
    postgres_insert_query = f"""INSERT INTO rel_db {table_columns} VALUES (%s,%s,%s);"""
    cursor.execute(postgres_insert_query,records)
    conn.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully into rel_db")
    cursor.close()
    conn.close()

def select(user_id,col_use,key):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    info = "查詢到的資料包含："
    if col_use == "名字":
        postgres_select_query = f"""SELECT * FROM rel_db WHERE user_id=%s,name=%s"""
        cursor.execute(postgres_select_query,(user_id,key,))
    elif col_use == "稱呼":
        postgres_select_query = f"""SELECT * FROM rel_db WHERE user_id=%s,rel_info=%s"""
        cursor.execute(postgres_select_query,(user_id,key,))
    elif col_use == "全部":
        postgres_select_query = f"""SELECT * FROM rel_db"""
        cursor.execute(postgres_select_query)
    d = cursor.fetchall()
    for p in d:
        info = info+"\n"+p[2]+":"+p[3]
    cursor.close()
    conn.close()
    return info

def update(user_id,col_use,key,up_col,upkey):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    if col_use == "名字":
        if up_col == "名字":
            postgres_select_query = f"""UPDATE rel_db SET name = %s WHERE user_id=%s,name=%s"""
        elif up_col == "稱呼":
            postgres_select_query = f"""UPDATE rel_db SET rel_db = %s WHERE user_id=%s,name=%s"""
        
    elif col_use == "稱呼":
        if up_col == "名字":
            postgres_select_query = f"""UPDATE rel_db SET name = %s WHERE user_id=%s,rel_info=%s"""
        elif up_col == "稱呼":
            postgres_select_query = f"""UPDATE rel_db SET rel_info = %s WHERE user_id=%s,rel_info=%s"""
    cursor.execute(postgres_select_query,(upkey,user_id,key,))
    conn.commit()

    count = cursor.rowcount
    cursor.close()
    conn.close()
    return (str(count)+"筆資料成功更新")

def delete(user_id,col_use,key):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    if col_use == "名字":
        postgres_delect_query = f"""DELETE * FROM rel_db WHERE user_id=%s,name=%s"""
        cursor.execute(postgres_delect_query,(user_id,key,))
    elif col_use == "稱呼":
        postgres_delect_query = f"""DELETE * FROM rel_db WHERE user_id=%s,rel_info=%s"""
        cursor.execute(postgres_delect_query,(user_id,key,))
    elif col_use == "全部":
        postgres_delect_query = f"""DELETE * FROM rel_db"""
        cursor.execute(postgres_delect_query)
    cursor.close()
    conn.close()

def db_exit():
    cursor.close()
    conn.close()