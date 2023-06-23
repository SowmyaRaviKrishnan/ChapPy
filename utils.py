import rpyc
from selfnode import *
from peer import *

r1 = Node("10.0.0.1",118811,"r1")
r1_r2 = Node("10.0.0.2",118811,"r2")
r3_r2 = Node("10.0.1.1",118811,"r2")
r2_r3 = Node("10.0.1.2",118811,"r3")
r4_r3 = Node("10.0.2.1",118811,"r3")
r4 = Node("10.0.2.2",118811,"r4")

peers_list = [r1,r1_r2,r3_r2]


r2_self = SelfNode("r2","r2password","10.0.0.2","r2",118811,peers_list)
r1_self = SelfNode("r1","r1password","10.0.0.1","r1",118811,peers_list)
r3_self = SelfNode("r3","r3password","10.0.1.2","r3",118811,peers_list)
r4_self = SelfNode("r4","r4password","10.0.2.2","r4",118811,peers_list)
current_node = r1_self 
peers = Peers(peers_list)

def connect_peer(peer_ip,peer_port):
    return rpyc.connect(peer_ip, peer_port)

