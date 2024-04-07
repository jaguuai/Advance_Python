import json
import os
# User class kullanici adi,parola,mail
class User:
    def __init__(self,username ,password , mail):
      self.username=username
      self.password=password
      self.mail=mail
    
# User class manager
class UserRepository:
    def __init__(self):
      self.users=[]
      self.isLoggedIn=False
      self.currentUser={}

      #load users from .json fiile
      self.loadUsers()
    
     
    def loadUsers(self):
       if os.path.exists("users.json"):
         with open("users.json","r",encoding="utf-8") as file:
           users=json.load(file)
           for user in users:
             user=json.loads(user)
             newUser=User(username= user["username"], password= user["password"],mail=user["mail"])
             self.users.append(newUser)
         print(self.users)    


    # Kullanici olusturma
    def register(self,user:User):
      self.users.append(user)
      self.savetoFile()
      print("User created.")
    
    # Kullanici giris islemi
    def login(self,username,password):
       for user in self.users:
           if user.username==username and user.password==password:
              self.isLoggedIn=True
              self.currentUser=user
              print("Login yapildi. ")
              break
           
    def logout(self):
           self.isLoggedIn=True
           self.currentUser={}
           print("Cikis yapildi. ")

    def identity(self):
          if self.isLoggedIn:
             print(f"username:{self.currentUser.username}")
          else:
             print("Giris yapılmadi.")

    # Kullanici bilgilerini jason verisi olarak database atsın
    def savetoFile(self):
      list=[]
      for user in self.users:
        list.append(json.dumps(user.__dict__))

      with open("users.json","w") as file:
         json.dump(list,file)


repository=UserRepository()

while True:
  print("Menu".center(50,"*"))
  choice=input("1- Register\n2- Login\n3- Logout\n4- Identitiy\n5- Exit\n Your cohoice: ")
  if(choice=="5"):
    break
  else:
    if choice=="1":
      #register
      username=input("username:")
      password=input("password:")
      mail=input("mail:")

      user=User(username=username,password=password,mail=mail)
      repository.register(user)

      print(repository.users)

    elif choice=="2":
       #login
       username=input("username:")
       password=input("password")

       repository.login(username=username,password=password)

    elif choice== "3":
       #log-out
       repository.logout()
    elif choice== "4":
       #identitiy(display username)
       repository.identity()
    else:
       print("Invalid choice..")


