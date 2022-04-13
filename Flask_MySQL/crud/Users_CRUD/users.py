# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database

NAME_OF_DATABASE = 'users_schema'
TABLE1_NAME = 'users'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        ## 2 Strings, 1 fstring, 1  prepared string, concat, put as arg in query_db
        query = f"SELECT * FROM {TABLE1_NAME};"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query = f"SELECT * FROM {TABLE1_NAME} WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)
        # Only 1 return
        return cls(results[0])

    @staticmethod
    def del_one(data):
        query = f"DELETE FROM {TABLE1_NAME} WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)
        # return none/bool
        return results

    # class method to save our user to the database
    @staticmethod
    def save(data ):
        query = f"INSERT INTO {TABLE1_NAME} ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(NAME_OF_DATABASE).query_db( query, data )

