from flask_login import LoginManager, UserMixin
from user_model import *


login_manager = LoginManager()

class User1(UserMixin):  
    pass  
