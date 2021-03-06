from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DATABASE = 'private_wall'
PRIMARY_TABLE = 'users'
SECONDARY_TABLE = 'messages'

debug = True

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.msg_sent_count = data['msg_sent_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.messages = []

    @classmethod
    def get_all(cls) -> list:
        query = f"SELECT * FROM {PRIMARY_TABLE};"
        results = connectToMySQL(DATABASE).query_db(query)
        user_lisst = []
        for user in results:
            user_lisst.append( cls(user) )
        return user_lisst

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

    # ! Many To One, skip otherwise
    @classmethod
    def get_user_with_messages( cls , data:dict ) -> list:
        query = f"""SELECT msg.id AS msg_id, msg.message as message, sent.first_name, msg.created_at
        FROM {PRIMARY_TABLE} AS recv
        LEFT JOIN {SECONDARY_TABLE} AS msg
        ON recv.id = msg.user_recv_id
        LEFT JOIN {PRIMARY_TABLE} AS sent
        ON sent.id = msg.user_sent_id
        WHERE recv.id = %(id)s;"""
        results = connectToMySQL(DATABASE).query_db( query , data )
        if debug:
            print(results)
        
        message_list = []
        for row in results:
            msg_data = {
                "id" : row['msg_id'],
                "message" : row['message'],
                "user_sent_id" : row['first_name'],
                "created_at" : row["created_at"],
            }
            message_list.append( msg_data )
        return message_list

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
    def valid_email_format( data:dict ) -> bool:
        # create regex pattern
        regex = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
        match = re.search(regex, data['email'])
        if debug:
            print(f"Email: {data['email']}")
            print(match)
        return True if match else False

    @classmethod
    def email_in_db( cls, data: dict ) -> bool:
        users_emails = {user.email for user in cls.get_all()}
        # set comprehension, make a set (unique values) of all user emails
        # from the users in User.get_all()
        if debug:
            print(f"Users Email List: {users_emails}")
            print(f"User Email: {data['email']}")

        return True if data['email'] in users_emails else False
        # while the total number of users is small and total run time between list and set
        # isn't going to matter on this scale, it will when size gets large enough.
        # https://stackoverflow.com/a/40963434
        # https://stackoverflow.com/a/68438122

    @staticmethod
    def valid_password(user:dict) -> bool:
        if debug:
            print("Starting password validation.")
        # Checks matching passwords, length, contains upper, lower and digit
        is_valid = True
        if debug:
            print(f"password: {user['password']}")
            print(f"password confirm: {user['password-confirm']}")
        if user['password'] != user['password-confirm']:
            flash("Passwords do not match.", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters long.", "register")
            is_valid = False
        
        hasUpper = hasLower = hasDigit = False
        charInd = 0
        while (not (hasUpper and hasLower and hasDigit)) and (charInd < len(user['password'])):
            if debug:
                print("Inside password while loop.")
            # while TRUE and TRUE
            # not (A and B and C) == (not A) or (not B) or (not C)
            # True or True or True == True or False or False == True
            if user['password'][charInd].isupper(): hasUpper = True
            if user['password'][charInd].islower(): hasLower = True
            if user['password'][charInd].isdigit(): hasDigit = True
            charInd += 1
        if debug:
            print("End password while loop")
        if not (hasUpper and hasLower and hasDigit):
            flash("Password must contain at least 1 lower character, 1 upper character and a digit.", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def save(data):
        query = f"INSERT INTO {PRIMARY_TABLE} ( first_name, last_name, email, password ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def del_one(data):
        query = f"DELETE FROM {PRIMARY_TABLE} WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @staticmethod
    def update(data):
        query = f"UPDATE {PRIMARY_TABLE} SET msg_sent_count = %(msg_sent_count)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )