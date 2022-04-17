from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

NAME_OF_DATABASE = 'login_schema'
TABLE1 = 'users'
# TABLE2 = 'ninjas'

debug = True

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls) -> list:
        query = f"SELECT * FROM {TABLE1};"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query)
        emails_list = []
        for email in results:
            emails_list.append( cls(email) )
        return emails_list

    @classmethod
    def get_one(cls, data):
        query = f"SELECT * FROM {TABLE1} WHERE id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def validate_model(cls, user:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(user['first_name']) < 2 or not user['first_name'].isalpha():
            flash("First name must be at least 2 characters an only letters.")
            is_valid = False
        if len(user['last_name']) < 2 or not user['last_name'].isalpha():
            flash("Last name must be at least 2 characters an only letters.")
            is_valid = False
        if not cls.valid_email_format(user):
            flash("Invalid email address.")
            is_valid = False
        if not cls.email_in_db(user):
            flash("Email in use already.")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Passwords do not match.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        return is_valid

    @staticmethod
    def valid_email_format( data:dict ) -> bool:
        is_valid = True
        # test whether a field matches the pattern
        regex = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
        if not re.search(regex, data['email']): 
            # flash("Invalid email address!") # no need for duplicate
            is_valid = False
        return is_valid

    @classmethod
    def email_in_db( cls, data: dict ) -> bool:
        users_emails = {user['email'] for user in cls.get_all()}
        # set comprehension, make a set (unique values) of all user emails
        # from the users in User.get_all()
        if data['email'] in users_emails:
            return True
        return False
        # while the total number of users is small and total run time between list and set
        # isn't going to matter on this scale, it will when size gets large enough.
        # https://stackoverflow.com/a/40963434
        # https://stackoverflow.com/a/68438122
        
    @staticmethod
    def del_one(data):
        query = f"DELETE FROM {TABLE1} WHERE id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)
        return results

    @staticmethod
    def update(data):
        query = f"UPDATE {TABLE1} SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(NAME_OF_DATABASE).query_db( query, data )
    
    @staticmethod
    def save(data):
        query = f"INSERT INTO {TABLE1} ( email ) VALUES ( %(email)s );"
        return connectToMySQL(NAME_OF_DATABASE).query_db( query, data )

    # ! Only for one to many, skip otherwise
    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = f"SELECT * FROM {TABLE1} LEFT JOIN {TABLE2} ON {TABLE2}.{TABLE1[:-1]}_id = {TABLE1}.id WHERE {TABLE1}.id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db( query , data )
        dojo = cls( results[0] )
        # print(results[0])
        for row in results:
            ninja_data = {
                "id" : row[f"{TABLE2}.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "dojo_id" : row["dojo_id"],
                "created_at" : row[f"{TABLE2}.created_at"],
                "updated_at" : row[f"{TABLE2}.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo