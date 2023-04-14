from ursinanetworking import *
Server=UrsinaNetworkingServer(Ip_=socket.gethostbyname(socket.gethostname()),Port_=12121)
@Server.event
def sent(client,message):
    Server.broadcast("get",message)
while True:
    Server.process_net_events()