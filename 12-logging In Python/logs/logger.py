## Configuring Logging Levels
# You can set the logging level to control which messages are logged
import logging

logging.basicConfig(
    filename='app.log',  # Log messages will be written to this file
    filemode='w',  # 'w' to overwrite the file, 'a' to append
    level=logging.DEBUG,
    FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )  # Set to INFO level