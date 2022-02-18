import random
import string
from typing_extensions import Self

class User:
    """
    class that generate new instances of users 
    """
    userlist=[]
    def __init__(self,firstname,lastname,username,password):
        """"
        helps us define properties
        """
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user( self):
        """   
        save user info 
        """
        User.userlist.append(self)
    def delete_user(self)