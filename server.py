# server.py
import rpyc
from rpyc.utils.server import ThreadedServer
from utils import *
from pychap import *
from User import *
from peer import *

@rpyc.service
class CHAPService(rpyc.Service):
    
    @rpyc.exposed
    def register_user(self,ip,port,username):
        user = User(username)
        peerobj = Node(ip,port,username)
        #register user
        pychap.authenticate(peerobj.save_nonce_nextnonce,user)

        #save nonce nextnonce
        pychap.authenticate(peerobj.save_nonce_nextnonce,user)
        
    @rpyc.exposed
    def send_authenticate_request(self,server_ip,server_port):
        connection = connect_peer(server_ip,server_port)
        nonce,nextnonce = connection.root.authenticate(current_node.username,current_node.response,current_node.cnonce)
        current_node.response = current_node.calculate_response(nonce)
        current_node.cnonce = current_node.calculate_cnonce(nextnonce)
        return "Sent Request & authenticated succesfully"

    @rpyc.exposed
    def authenticate(self,peer_username,response,cnonce):
        peerobj = peers.get_peers()[peer_username]
        usr = User(peer_username)
        usr.response = response 
        usr.cnonce = cnonce
        usr.nonce = peerobj.nonce
        usr.nextnonce = peerobj.nextnonce
        usr.passkey = peerobj.passkey
        pychap.authenticate(peerobj.save_nonce_nextnonce,usr)
        return peerobj.nonce,peerobj.nextnonce,usr.message
        


print('starting server')
server = ThreadedServer(CHAPService, port=current_node.port)
server.start()