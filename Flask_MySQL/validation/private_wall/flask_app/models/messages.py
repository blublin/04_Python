from Flask_MySQL.validation.private_wall.flask_app.models.user import SECONDARY_TABLE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DATABASE = 'private_wall'
PRIMARY_TABLE = 'messagess'
SECONDARY_TABLE = 'users'

debug = False

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.message = data['message']
        self.user_sent_id = data['user_sent_id']
        self.user_recv_id = data['user_recv_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls) -> list:
        query = f"SELECT * FROM {PRIMARY_TABLE};"
        results = connectToMySQL(DATABASE).query_db(query)
        msg_list = []
        for msg in results:
            msg_list.append( cls(msg) )
        return msg_list

    @classmethod
    def get_one(cls, data:dict) -> object or bool:
        query = f"SELECT * FROM {PRIMARY_TABLE} WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else False

    ## ! used in user validation
    @classmethod
    def get_by_col(cls, data:dict) -> object or bool:
        # Only the first key,value pair combo from dict will be checked
        query = f"SELECT * FROM {PRIMARY_TABLE} WHERE { list(data.keys())[0] } = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Return an instance class of User if true, else return False
        return cls(result[0]) if result else False

    @classmethod
    def validate_model(cls, user:dict) -> bool:
        is_valid = True
        if len(user['first_name']) < 2 or not user['first_name'].isalpha():
            if debug:
                print(f"First name: {user['first_name']}")
                print(f"First name length: {len(user['first_name'])}")
                print(f"First name isalpha: {user['first_name'].isalpha()} ")
            flash("First name must be at least 2 characters an only letters.", "register")
            is_valid = False
        if len(user['last_name']) < 2 or not user['last_name'].isalpha():
            if debug:
                print(f"Last name: {user['last_name']}")
                print(f"Last name length: {len(user['last_name'])}")
                print(f"Last name isalpha: {user['last_name'].isalpha()} ")
            flash("Last name must be at least 2 characters an only letters.", "register")
            is_valid = False
        if not cls.valid_email_format(user):
            flash("Invalid email address.", "register")
            is_valid = False
        if cls.email_in_db(user):
            flash("Email in use already.", "register")
            is_valid = False
        if not cls.valid_password(user):
            is_valid = False
        return is_valid

    @staticmethod
    def save(data):
        query = f"INSERT INTO {PRIMARY_TABLE} ( message, user_sent_id, user_recv_id ) VALUES ( %(message)s, %(user_sent_id)s, %(user_recv_id)s );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def del_one(data):
        query = f"DELETE FROM {PRIMARY_TABLE} WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results