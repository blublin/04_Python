from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

NAME_OF_DATABASE = 'dojo_survey_schema'
TABLE1 = 'dojos'
# TABLE2 = 'ninjas'

debug = True

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {TABLE1};"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query)
        dojos_list = []
        for dojo in results:
            dojos_list.append( cls(dojo) )

        return dojos_list

    @staticmethod
    def validate_comment(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            if debug:
                print(f"name key: {data['name']} -- len: {len(data['name'])}")
            flash("Name must be at least 3 characters.")
            is_valid = False
        if data['location'] == '999':
            if debug:
                print(f"Location : {data['location']}")
            flash("Location must be from dropdown selection menu.")
            is_valid = False
        if data['language'] == '999':
            if debug:
                print(f"language : {data['language']}")
            flash("Language must be from dropdown selection menu.")
            is_valid = False
        if len(data['comment']) < 5:
            if debug:
                print(f"Comment: {data['comment']} -- len: {len(data['comment'])}")
            flash("Comment must be at least 10 characters.")
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
        query = f"INSERT INTO {TABLE1} ( name, location, language, comment ) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s );"

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