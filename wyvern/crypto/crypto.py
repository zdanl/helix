import socket
import nacl.encoding
import logging

from nacl.public import PublicKey, PrivateKey, Box

class Crypto:

    private_key = None
    public_key  = None
    server_key  = None
    box         = None
    socket      = None

    def __init__(self, socket):
        self.socket = socket
        
        self.generate_keys()
        self.provide_publickey()
        self.receive_publickey()
        self.create_box()

    def generate_keys(self):
        """
        Generate a private and public key for the client
        
        """ 
        self.private_key = PrivateKey.generate()
        self.public_key = self.private_key.public_key
        logging.info("Generating Keypair.")

    def provide_publickey(self):
        # Send the client's public key to the server
        self.socket.sendall(self.public_key.encode())
        logging.info("Providing Public Key to Server.")

    def receive_publickey(self):
        # Receive the server's public key
        self.server_public_key = PublicKey(self.socket.recv(32), encoder=nacl.encoding.RawEncoder)
        logging.info("Received Server Public Key.")

    def create_box(self):
        logging.info("Computated crypto box")
        # Create a new Box using the client's private key and the server's public key
        self.box = Box(self.private_key, self.server_public_key)

    def receive_encrypted_data(self):
        """
        Receive a 4096 byte max. payload and decrypt it

        Logs
        Returns the decrypted data
        
        """

        encrypted_data = self.socket.recv(4096)
        decrypted_data = self.box.decrypt(encrypted_data)

        logging.info("Decrypted payload from server: %s" %(decrypted_data))
    
        return decrypted_data

    def send_encrypted_data(self, payload):
        """
        Encrypt & Send a max. 4096 bytes payload 

        Logs
        Returns 0 if it worked
        """
        
        logging.info("Encrypting & sending payload: %s" %(payload))
        encrypted_data = self.box.encrypt(payload)
        self.socket.sendall(encrypted_data)

if __name__ == "__main__":
    pass
