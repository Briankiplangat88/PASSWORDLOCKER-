from cgi import print_directory
from ntpath import join
from optparse import Option
import string
from random import*

from click import option
from user import User 
from user import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser=User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_user():
    return User.display_users()
def create_account(accountusername,accountname,accountpassword):
    newaccount= Credentials(accountname,accountusername,accountpassword)  
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account() 
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()
def main():
         while True :
             print("welcome to passowrd locker write S or L to start")
             print("S -or- L") 
             option=input()
             if option == "S" :
                 print("create account")
                 print("-"*10)
                 print("enter your first name...")
                 firstname=input()
                 print("enter last name...")   
                 lastname=input()
                 print("set your username ...")
                 username=input()
                 print("set your password...")
                 userpassword=input()
                 save_user(create_user(firstname,lastname,username,userpassword)) 
                 print("you have sucessfuly created an account,here are your account details:") 
                 print("-"*10)
                 print(f"Name: {firstname} {lastname} \nusername: {username} \npassword: {userpassword}")
                 print( "\nuse login to your account with your details")
                 print("\n \n")
                 #for user in display_users()
                 #print
             elif option =="L":
                 print("your username...")
                 loginUsername=input() 
                 print("your password...")
                 loginPassword=input()
                 if find_user(loginPassword):
                     print("\n")
                     print("you can create multiple accounts (A) and (V)")
                     print("-"*40)
                     print("A -or- V")
                     choose= input()
                     print("\n")
                     if choose == "A":
                         print("add your credentials account")
                         print("-"*20)
                         accountusername=loginUsername
                         print("account name")
                         accountname=input()
                         print("\n")
                         print("generate automatic passowrd (G) or create password (c)? ")
                         decision=input()
                         if decision== "G":
                            characters=string.ascii_letters + string.digits
                            accountpassword="",join(choice(characters)for x in range(randint(6,16)))
                            print(f"password:{accountpassword}")
                         elif decision=="C" :
                              print("enter your password") 
                              accountpassword=input()
                         else:
                             print("please put in a valid choice")  
                             save_account(create_account(accountusername,accountname,accountpassword))
                             print("\n") 
                             print(f"Username {accountusername}  \naccountname: {accountname} \npassword: {accountpassword}") 
                     elif choose== "V" :
                            if find_account(accountusername):
                             print("here is is alist of accounts you created")
                             print("-"*20)
                             for user in display_accounts():
                                   print(f"account {accountusername} \npassword: {accountpassword} \n\n") 
                             else:
                                 print("invalid credentials")
                            else:
                                print("please try again") 
                                print("\n")
                     else:
                            print("incorrect info please try again")
                            print("\n")
                 else:
                     print("kindly choose valid option")  
                     print("\n") 
if __name__ == "_main_" :
     main()                         

                           
                           


                       
                

 














































































































































































































































































































































































































































































































































































































































































































