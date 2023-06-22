##client that requests the egress peer to send an authentication request
import hashlib

class SelfNode:
    def __init__(self,username,passkey,ip,hostname,port):
        self.ip = ip
        self.hostname = hostname
        self.username = username
        self.passkey = passkey
        self.response = None
        self.cnonce = None
        self.port = port

    def calculate_response(self,nonce):
        response = hashlib.sha1(nonce.encode('ascii'))
        response.update(self.passkey.encode('ascii'))
        self.response = response.hexdigest()

    def calculate_cnonce(self,nextnonce):
        cnonce = hashlib.sha1(nextnonce.encode('ascii'))
        cnonce.update(self.passkey.encode('ascii'))
        self.cnonce = hashlib.sha1(cnonce.hexdigest().encode("ascii")).hexdigest()


