
from .logger import logger
from .model import _Model_Wrapper

class _AISys:
    def __init__(self):
        logger.debug("Host initialized")
        self.model = _Model_Wrapper("meta-llama/Llama-3.2-3B-Instruct")
        self._ConnectMCP()

    def RunSummaryTask(self, input):
        logger.debug(f"Task begun for project: {input}")
        result = self.model.generate_summary(input)
        return result

    
    #establishes mcp connection
    def _ConnectMCP(self):
        logger.info("mock mcp connected")
    def _ShutdownMCP(self):
        logger.info("mock mcp shutdown")
    
    #Initialize model object using Model_Wrapper
    