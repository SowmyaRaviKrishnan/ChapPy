import rpyc
from utils import *
from time import sleep

def request_to_send_authenticate(peer_ip,peer_port):
    connection = connect_peer(peer_ip,peer_port)
    connection.root.send_authentication_request()


if __name__ == "__main__":
      while True:
            for peer in peers:
                request_to_send_authenticate(peers[peer].ip,peers[peer].port)
            sleep(10)
            

    