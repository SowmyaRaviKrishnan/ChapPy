import rpyc
from utils import *
from time import sleep

def request_to_send_authenticate(peer_ip,peer_port):
    connection = connect_peer(peer_ip,peer_port)
    connection.root.send_authentication_request()


if __name__ == "__main__":
      while True:
            for peer in peers.peers:
                connection = connect_peer(peers.peers[peer].ip,peers.peers[peer].port)
                response = "abcdef"
                cnonce = "qwerty"
                nonce,nextnonce = connection.root.authenticate(current_node.username,response,cnonce)
                current_node.calculate_response(peers.peers[peer].username,nonce)
                current_node.calculate_cnonce(peers.peers[peer].username,nextnonce)
            sleep(10)
            

    