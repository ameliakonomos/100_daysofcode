#Class is a blueprint of the code structure
#day 17 start

#class nameofclass:
class User: #class definition

    def __init__(self, user_id, username): #init function is called every time i create an object from this class
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "amelia") #initialize object in class
user_2 = User("002", "fiona") #initialize object in class

user_1.follow(user_2) #user 1 object and follow method with person who were going to follow
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#

