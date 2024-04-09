import requests

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        # self.token="Güvenlik nedeniyle silinmistir"
    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json() # bu yontem json modulu ımport etmeden dict. cevirir
    def getRepositories(self,username):
        response=requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()
    def createRepository(self,name):
         headers = {
          'Authorization': 'Bearer ' + self.token,
          'Accept': 'application/json'
         }
         data = {
          "name": name,
          "description": "This is your first repo",
          "homepage": "https://github.com",
          "private": False,
          "has_issues": True,
          "has_projects": True,
          "has_wiki": True
          }
         response = requests.post(self.api_url + "/user/repos", headers=headers, json=data)
         return response.json()
    
    
    
github=Github()

while True:
    vote=input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nVote: ")
    
    if vote == "4":
        break
    else:
        if vote=="1":
             username=input("username:")
             result=github.getUser(username)
             print(f"namae: {result["name"]} public repos :{result["public_repos"]} follower:{result["followers"]}")
        elif vote=="2":
            username=input("username:")
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])
            
        elif vote=="3":
            name=input("repo name: ")
            result=github.createRepository(name)
            print(result)
        else:
            print("Invalid vote..")