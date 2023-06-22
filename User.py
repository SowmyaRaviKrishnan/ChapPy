import pychap
import hashlib
class User:
    def __init__(self,username):
        self.username = username 
        self.passkey  = None 
        self.nonce  = None 
        self.nextnonce  = None 
        self.cnonce  = None 
        self.response  = None 
        self.message = None
    
"""
def putuser(user):
    print(user.username,user.nonce,user.nextnonce,user.message)    
#user creation
user = User("test")
pychap.authenticate(putuser,user)

#1st auth
print("second try")





pychap.authenticate(putuser,user)

#2nd auth

print("third try")

response = hashlib.sha1(user.nonce.encode('ascii'))
response.update("password".encode('ascii'))
user.response = response.hexdigest()


cnonce = hashlib.sha1(user.nextnonce.encode('ascii'))
cnonce.update("password".encode('ascii'))
user.cnonce = hashlib.sha1(cnonce.hexdigest().encode("ascii")).hexdigest()

pychap.authenticate(putuser,user)
"""