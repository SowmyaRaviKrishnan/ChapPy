import pychap
class User:
    def __init__(self,username,passkey):
        self.username = username 
        self.passkey  = passkey 
        self.nonce  = None 
        self.nextnonce  = None 
        self.cnonce  = None 
        self.response  = None 
        self.message = None
    

def putuser(user):
    print(user.username,user.nonce,user.nextnonce,user.message)    

user = User("test","password")
pychap.authenticate(putuser,user)
print("second try")
pychap.authenticate(putuser,user)
print(user.message)
