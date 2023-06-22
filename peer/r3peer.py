class Node:
    def __init__(self,ip,port,username):
        self.ip = ip
        self.port = port
        self.username = username
        self.nonce  = None 
        self.nextnonce  = None
        self.passkey = None

    def save_nonce_nextnonce(self,user):
        print(user.message)
        self.nonce = user.nonce
        self.nextnonce = user.nextnonce
        self.passkey = user.passkey

class Peers:
    def __init__(self):
        self.peers = {}
        #r1 = Node("10.0.0.1",118811,"r1")
        #r2 = Node("10.0.0.2",118811,"r2")
        r2 = Node("10.0.1.1",118811,"r2")
        #r3 = Node("10.0.1.2",118811,"r3")
        #self.add_peer("r1",r1)
        self.add_peer("r2",r2)

    def add_peer(self,username,node):
        self.peers[username] = node

    def get_peers(self):
        return self.peers


