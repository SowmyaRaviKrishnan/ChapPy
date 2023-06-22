import rpyc
from selfnode import *
from peer import *

#current_node = SelfNode("r2","password","10.0.0.2","r2",118811)
#current_node = SelfNode("r1","password","10.0.0.1","r1",118811)
current_node = SelfNode("r3","password","10.0.1.2","r3",118811)
peers = Peers()

def connect_peer(peer_ip,peer_port):
    return rpyc.connect(peer_ip, peer_port)

