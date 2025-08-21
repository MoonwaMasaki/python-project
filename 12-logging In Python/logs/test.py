from logger import logging

def add(x, y):
    logging.debug("The addition operation is being performed.")
    return x + y

logging.debug("The addition function is called")
add(5, 3)