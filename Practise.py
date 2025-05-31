import logging

logger = logging.getLogger(__name__)   # here the name of the module will appear instead of root
logger.propagate = False  # Prevents the log messages from propagating to the root logger
logger.info('Hello from the other side')