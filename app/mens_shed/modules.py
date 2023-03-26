from flask_login import LoginManager, UserMixin
from mens_shed import login_manager

@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))

class User(UserMixin):
    def __init__(self, id, username, email, name, address, password):
        self.id = id
        self.username = username
        self.email = email
        self.name = name
        self.address = address
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'
    