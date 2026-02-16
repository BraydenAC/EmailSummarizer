
from .logger import logger
from .model import _Model_Wrapper

class _AISys:
    def __init__(self):
        logger.debug("Host initialized")
        model = _Model_Wrapper("meta-llama/Llama-3.2-3B-Instruct")
    
    #establishes mcp connection
    def _ConnectMCP(self):
        logger.info("mock mcp connected")
    def _ShutdownMCP(self):
        logger.info("mock mcp shutdown")
    
    #Initialize model object using Model_Wrapper
    