import ibm_db

import db_conn

db2 = db_conn.DbConn()

class Database:

    def __init__(self):
        self.conn = db2.connect()
        create_query = """CREATE TABLE  IF NOT EXISTS "BBR24632"."CREDENTIALS"(
                        User_ID INTEGER NOT NULL,
                        first_name CHAR(20),
                        last_name CHAR(20),
                        email VARCHAR(200),
                        pwd VARCHAR(20),
                        PRIMARY KEY(User_ID)
                        )"""
        stmt = ibm_db.prepare(self.conn,create_query)
        result=ibm_db.execute(stmt)

        create_query2 = f"""CREATE TABLE  IF NOT EXISTS "BBR24632"."EXPENSE"(
                        User_ID INTEGER ,
                        Expense_Amt INTEGER,
                        Expense_name VARCHAR(200),
                        Expense_Date DATE,
                        CONSTRAINT FK_PersonOrder FOREIGN KEY (User_ID)
                        REFERENCES "BBR24632"."CREDENTIALS"(User_ID)
                        )"""
        stmt2 = ibm_db.prepare(self.conn,create_query2)
        result2=ibm_db.execute(stmt2)

    def insert(self,uid,fname,lname,email,pwd):
        
        insert_query = f"""insert  into "BBR24632"."CREDENTIALS" values('{uid}','{fname}','{lname}','{email}','{pwd}')"""
        insert_table = ibm_db.exec_immediate(self.conn,insert_query)
        print("Inserted Successfull")

    def wallet_insert(self,uid,expense_amt,expense_name,expense_date):
        insert_query = f"""INSERT
                        INTO  "BBR24632"."EXPENSE" ("USER_ID","EXPENSE_AMT","EXPENSE_NAME","EXPENSE_DATE")
                        VALUES('{uid}',{expense_amt},'{expense_name}','{expense_date}');"""
        insert_table = ibm_db.exec_immediate(self.conn,insert_query)

    def length_view(self):
        length_query = ibm_db.exec_immediate(self.conn,'SELECT COUNT(*) FROM "BBR24632"."CREDENTIALS"')
        length = ibm_db.fetch_tuple(length_query)[0]
        
        return length
    
    def view(self,email):

        view_query = f"""SELECT email FROM "BBR24632"."CREDENTIALS" WHERE email = '{email}'"""
        view_db = ibm_db.exec_immediate(self.conn,view_query)
        result = ibm_db.fetch_row(view_db)

        return result
        
    def lg_view(self,email):
        view_query = f"""SELECT email,pwd  FROM "BBR24632"."CREDENTIALS" WHERE email = '{email}'"""
        view_db = ibm_db.exec_immediate(self.conn,view_query)
        result = ibm_db.fetch_tuple(view_db)

        return result

    def uid_view(self,email):
        view_query = f"""SELECT USER_ID FROM "BBR24632"."CREDENTIALS" WHERE email = '{email}'"""
        view_db = ibm_db.exec_immediate(self.conn,view_query)
        result = ibm_db.fetch_tuple(view_db)
        
        return result[0]