import rpyc
from selfnode import *
from peer import *

current_node = SelfNode("r4","password","ip","r4",1234)
peers = Peers()

def connect_peer(peer_ip,peer_port):
    return rpyc.connect(peer_ip, peer_port)

