import socket
import threading
import traceback
from VadGutTitan.Logic.Debug.Debugger import Debugger
from VadGutServer.Protocol.Messaging import Messaging
from VadGutTitan.Encryption.RC4Encrypter import RC4Encrypter
from VadGutTitan.Logic.Message.PiranhaMessage import PiranhaMessage
from VadGutLogic.LogicGutMessageFactory import LogicGutMessageFactory
from VadGutServer.Protocol.MessageManager import MessageManager


class Connection(threading.Thread):
    def __init__(self, socket: socket.socket, address):
        super().__init__()
        self.client = socket
        self.address = address
        self.messaging = Messaging(self.client)
        self.manager = MessageManager(self.messaging,)
        self.rc4_encrypter = RC4Encrypter()
    
    def recv(self, n) -> bytearray:
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                Debugger.warning("Data is NULL")
                return b''
            data.extend(packet)
        return data
    
    def run(self) -> None:
        try:
            while True:
                header = self.client.recv(7)
                
                if len(header) >= 7:
                    messageType, encodingLength, messageVersion = self.messaging.readHeader(header)
                    payload = self.recv(encodingLength)
                    if messageType != 10105:
                        decPayload = self.rc4_encrypter.decrypt(payload)
                    else:
                        decPayload = payload
                    
                    message: PiranhaMessage = LogicGutMessageFactory.createMessageByType(messageType)

                    if message is not None:
                        message.setMessageVersion(messageVersion)
                        message.getByteStream().setByteArray(decPayload, encodingLength, len(decPayload))

                        message.decode()
                        self.manager.receiveMessage(message)
        except ConnectionError:
            Debugger.debug(f"Client {self.address[0]}:{self.address[1]} has disconnected")
            self.client.close()
        except Exception as e:
            Debugger.error("Error: " + str(e))
            traceback.print_exc()
