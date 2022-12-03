import logging

# Create a logger
wyvern_logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler('wyvern.log')

# Create a stream handler
stream_handler = logging.StreamHandler()

# Set the logging level
wyvern_logger.setLevel(logging.INFO)

# Set the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
wyvern_logger.addHandler(file_handler)
wyvern_logger.addHandler(stream_handler)
