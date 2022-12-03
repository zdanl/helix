import sys, asyncio, logging

import wyvern.crypto
import wyvern.network

from wyvern.logging import wyvern_logger

wyvern_network = wyvern.network.Network("wyvra.net", 8888)
wyvern_crypto  = wyvern.crypto.Crypto(wyvern_network.socket)

async def wyvern_handle_connection():
    global wyvern_network, wyvern_crypto
    logging.info("Awaiting chatserver to dispatch.")

    while True:
        payload = wyvern_crypto.receive_encrypted_data()
        wyvern_logger.info("Got Payload: %s" %payload)

async def wyvern_init(loop=None):
    global wyvern_network, wyvern_crypto

    # Chat loop
    future = asyncio.ensure_future(wyvern_handle_connection())

    


def wyvern_cleanup():
    """
    Clean up memory and IO

    sys.exit(0) 

    """
    global wyvern_network

    # Close the socket
    wyvern_logger.info("Closing TCP/IP socket")
    wyvern_network.disconnect()
    wyvern_logger.info("TCP/IP socket closed.")
    sys.exit(0)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(wyvern_init(loop=loop))
    except KeyboardInterrupt:
        print("Keyboar Interrupt")
    
    wyvern_cleanup()
