class User:
    def __init__(self,username,password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password
    
    def set_password(self, new_pass):
        if len(new_pass) >= 6:
            self.__password = new_pass
        else:
            print("password too shortt !!!")


u = User("shryuu", "12345")
print("old password ",u.get_password())