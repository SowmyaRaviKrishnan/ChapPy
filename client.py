import rpyc
from utils import *
from time import sleep

def request_to_send_authenticate(peer_ip,peer_port):
    connection = connect_peer(peer_ip,peer_port)
    connection.root.send_authentication_request()


if __name__ == "__main__":
      while True:
            for peer in peers:
                connection = connect_peer(peers[peer].ip,peers[peer].port)
                nonce,nextnonce = connection.root.authenticate(current_node.username,current_node.response,current_node.cnonce)
                current_node.response = current_node.calculate_response(nonce)
                current_node.cnonce = current_node.calculate_cnonce(nextnonce)
            sleep(10)
            

    