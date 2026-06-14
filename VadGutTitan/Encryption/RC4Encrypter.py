from VadGutTitan.Encryption.RC4 import RC4

class RC4Encrypter:
    def __init__(self):
        self.key = b'9o23ljkmsdfsdippwe0qr2ke1jejhjhjdfb121fpWE802lss'
        self.nonce = b'nonce'
        
        combined_key = self.key + self.nonce

        self.RC4_Stream = RC4(combined_key)
        self.RC4_Stream2 = RC4(combined_key)

        self.RC4_Stream.process(combined_key)
        self.RC4_Stream2.process(combined_key)

    def decrypt(self, data: bytes) -> bytes:
        return self.RC4_Stream.process(data)

    def encrypt(self, data: bytes) -> bytes:
        return self.RC4_Stream2.process(data)
