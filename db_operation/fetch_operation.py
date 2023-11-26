import mysql.connector

class FetchOperation:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dudeabides1999",
        database="Customer"
        )
        self.mycursor = self.mydb.cursor()
    
    

    def fetch(self, query):
        self.mycursor.execute("SELECT * FROM Customer")
        myresult = self.mycursor.fetchall()
        myresult.insert(0, ("Uid", "Name", "number", "limit"))
        print(myresult)
        print(myresult[0] is dict)
        print(myresult[0] is tuple)
        return myresult
        result_list = []
        element = "Query: " + query + " has been fetched.", "Query: "
        result_list = [element] * 50
        return result_list