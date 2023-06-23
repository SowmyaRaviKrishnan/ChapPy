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
    
