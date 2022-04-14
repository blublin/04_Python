from flask_app.config.mysqlconnection import connectToMySQL

NAME_OF_DATABASE = 'dojos_and_ninjas_schema'
TABLE1_NAME = 'ninjas'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {TABLE1_NAME};"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query)
        ninjas_list = []
        for user in results:
            ninjas_list.append( cls(user) )

        return ninjas_list

    @classmethod
    def get_one(cls, data):
        query = f"SELECT * FROM {TABLE1_NAME} WHERE id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)

        return cls(results[0])

    @staticmethod
    def del_one(data):
        query = f"DELETE FROM {TABLE1_NAME} WHERE id = %(id)s;"
        results = connectToMySQL(NAME_OF_DATABASE).query_db(query, data)

        return results

    @staticmethod
    def update(data):
        query = f"UPDATE {TABLE1_NAME} SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;"

        return connectToMySQL(NAME_OF_DATABASE).query_db( query, data )
    
    @staticmethod
    def save(data):
        query = f"INSERT INTO {TABLE1_NAME} (first_name , last_name , age, dojo_id) VALUES (%(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s);"

        return connectToMySQL(NAME_OF_DATABASE).query_db( query, data )