# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:30:58 2020

@author: caleb
"""


import os
import psycopg2


DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a who-you-are').read()[:-1]
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

table_columns = '(user_id,name,rel_info)'
records= [('xxx','yyy','父親'),
          ('xxx','yya','母親'),
          ('xxa','yyy','父親'),
          ('xxa','yya','母親'),
          ('xxb','yyc','哥哥'),
          ('xxb','yya','母親')]
postgres_insert_query = f"""INSERT INTO rel_db {table_columns} VALUES (%s,%s,%s);"""
cursor.executemany(postgres_insert_query,records)
conn.commit()
count = cursor.rowcount

print(count,"Record inserted successfully into rel_db")

postgres_select_query = f"""SELECT * FROM rel_db WHERE rel_info='母親'"""
cursor.execute(postgres_select_query)
a = cursor.fetchall()
print(a)

rel = '哥哥'
postgres_update_query = f"""UPDATE rel_db SET rel_info = '哥哥' WHERE rel_info = %s"""
cursor.execute(postgres_update_query,(rel,))
conn.commit()

count = cursor.rowcount
print(count, "Record updated successfully into rel_db")

cursor.close()
conn.close()