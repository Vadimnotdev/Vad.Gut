import threading
from VadGutServer.Network.TCPNetwork import TcpNetwork
from VadGutServer.Network import HTTPServer
http_thread = threading.Thread(target=HTTPServer.run, daemon=True)
http_thread.start()
TcpNetwork(("0.0.0.0", 9339))