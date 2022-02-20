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
    def delete_user(self):
    
    
     User.userlist.remove(self)

    @classmethod
    def display_users(cls):
        """
        method that  return info from userlist
        """
        return cls.userlist
    @classmethod 
    def find_by_number(cls,number):
        """
         method that takes in a username and returns a user that matches that numer 
        """ 
        for user in cls.userlist:
            if user.passowrd ==number:
               return user 
    @classmethod
    def user_exists(cls,number):
         """
         to test if the user exist
         """
         for user in cls.userlist:
             if user.username == number:
                 return True
    class Credentials:
        """   
        class to generate credentials    
        """
        accounts=[]
        def _init_(self,accountusername,accountname,accountpassword):
            """
            method to defie properties
            
            """ 
            self.accountusername=accountusername
            self.accountname=accountname
            self.accountpassword=accountpassword

        def save_account(self):
            """ 
            save account

            """
        

 