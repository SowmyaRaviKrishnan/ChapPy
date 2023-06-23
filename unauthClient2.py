import rpyc
from utils import *
from time import sleep

def request_to_send_authenticate(peer_ip,peer_port):
    connection = connect_peer(peer_ip,peer_port)
    connection.root.send_authentication_request()


if __name__ == "__main__":
      counter = 0
      while True:
            counter +=1
            for peer in peers.peers:
                connection = connect_peer(peers.peers[peer].ip,peers.peers[peer].port)
                response = current_node.response[peers.peers[peer].username]
                cnonce = current_node.cnonce[peers.peers[peer].username]
                if counter == 5:
                    nonce,nextnonce,message = connection.root.authenticate("r1",response,cnonce)
                    print("Authentication Status for Peer :"+current_node.username+" "+message)
                    break
                nonce,nextnonce,_ = connection.root.authenticate(current_node.username,response,cnonce)
                current_node.calculate_response(peers.peers[peer].username,nonce)
                current_node.calculate_cnonce(peers.peers[peer].username,nextnonce)
            if counter == 5:
                 break
            sleep(10)

            

    