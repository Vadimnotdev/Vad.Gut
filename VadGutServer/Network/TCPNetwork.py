import socket
from VadGutServer.Network.Connection import Connection


class TcpNetwork:
    def __init__(self, address) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        print("""
              
__     __        _        ____       _   
\ \   / /_ _  __| |      / ___|_   _| |_ 
 \ \ / / _` |/ _` |     | |  _| | | | __|
  \ V / (_| | (_| |  _  | |_| | |_| | |_ 
   \_/ \__,_|\__,_| (_)  \____|\__,_|\__|                   
    
              """)
        print("Server is listening connections at " + str(address))
        while True:
            self.server.listen()
            connection, addr = self.server.accept()
            print(f"New connection from {addr[0]}:{addr[1]}")
            Connection.Connection(connection, addr).start()