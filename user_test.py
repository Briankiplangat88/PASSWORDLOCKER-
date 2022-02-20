# from collections import UserList, UserString
# from operator import truediv
# import random
# import re
# from site import USER_BASE
# import string
# from typing_extensions import Self

# from click import UsageError


import unittest
from user import User

class Testuser( unittest.TestCase):
    """
    test class that defines test cases for the user class behaviours.
    Args:
    unittest.testcase:testcase class that helps in creating test cases 
    """
def settup(self):
    """
    setup method to run before  each test cases 
    """
    self.new_user = User ("bryan","kip","2022") #create object contact 
def test_init(self):
    """
    setup method to run before each test 
    """
    self.assertEqual (self.new_user.user_name,'bryan')


    self .assertEqual (self.new_user.password,'2022')
def test_save_user(self):
    """  
    test if the user object is saved to userlist 
    """
    self.new_user.save_user() #saving new contact 
    self.assertEqual(len(User.user_list),1)
def test_delete_user(self):
    """  
    to test if we can remove a contact from contact list
    """
    self.new_contact.save_contact()
    test_user= User ('test','user','1234','test@user.com') #new contact
    test_user.save_user()

    self.new_suer.delete_user() #deleting a contact object
    self.assertEqual(len(User.user_list),1)
if __name__== '_main_':
    unittest.main()    