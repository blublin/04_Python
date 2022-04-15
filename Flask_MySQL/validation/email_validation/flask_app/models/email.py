from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

NAME_OF_DATABASE = 'email_schema'
TABLE1 = 'emails'
# TABLE2 = 'ninjas'

debug = True

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
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

    @staticmethod
    def validate_comment(data):
        is_valid = True # we assume this is true
        if len(data['email']) < 3:
            if debug:
                print(f"email key: {data['email']} -- len: {len(data['email'])}")
            flash("Email must be at least 3 characters.")
            is_valid = False
        return is_valid

    @staticmethod
    def valid_email( data ):
        is_valid = True
        # test whether a field matches the pattern
        regex = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
        if not re.search(regex, data['email']): 
            flash("Invalid email address!")
            is_valid = False

        return is_valid

    @classmethod
    def get_one(cls, data):
        query = f"SELECT * FROM {TABLE1} WHERE id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)

        return cls(results[0])

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