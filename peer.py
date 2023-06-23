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
    def __init__(self,peers_list):
        self.peers = {}
        for each in peers_list:
            self.add_peer(each.username,each)

    def add_peer(self,username,node):
        self.peers[username] = node

    def get_peers(self):
        return self.peers


