from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

NAME_OF_DATABASE = 'dojos_and_ninjas_schema'
TABLE1 = 'dojos'
TABLE2 = 'ninjas'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {TABLE1};"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query)
        dojos_list = []
        for dojo in results:
            dojos_list.append( cls(dojo) )

        return dojos_list

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
        query = f"INSERT INTO {TABLE1} ( name ) VALUES ( %(name)s);"

        return connectToMySQL(NAME_OF_DATABASE).query_db( query, data )

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = f"SELECT * FROM {TABLE1} LEFT JOIN {TABLE2} ON {TABLE2}.{TABLE1}_id = {TABLE1}.id WHERE {TABLE1}.id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db( query , data )
        dojo = cls( results[0] )
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