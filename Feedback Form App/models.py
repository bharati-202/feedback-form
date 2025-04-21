from werkzeug.security import generate_password_hash, check_password_hash

class User:
    users = []
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    @classmethod
    def get_user_by_email(cls, email):
        for user in cls.users:
            if user.email == email:
                return user
        return None
    
    @classmethod
    def get_user_by_username(cls, username):
        for user in cls.users:
            if user.username == username:
                return user
        return None
    
    @classmethod
    def add_user(cls, user):
        cls.users.append(user)