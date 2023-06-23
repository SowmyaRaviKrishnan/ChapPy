##client that requests the egress peer to send an authentication request
import hashlib

class SelfNode:
    def __init__(self,username,passkey,ip,hostname,port,peers_list):
        self.ip = ip
        self.hostname = hostname
        self.username = username
        self.passkey = passkey
        self.response = {}
        self.cnonce = {}
        for each in peers_list:
            self.response[each.username] = None
            self.cnonce[each.username] = None
        self.port = port

    def calculate_response(self,peer_user,nonce):
        response = hashlib.sha1(nonce.encode('ascii'))
        response.update(self.passkey.encode('ascii'))
        self.response[peer_user] = response.hexdigest()

    def calculate_cnonce(self,peer_user,nextnonce):
        cnonce = hashlib.sha1(nextnonce.encode('ascii'))
        cnonce.update(self.passkey.encode('ascii'))
        self.cnonce[peer_user] = hashlib.sha1(cnonce.hexdigest().encode("ascii")).hexdigest()


