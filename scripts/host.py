
from .model import _Model_Wrapper

class _AISys:
    def __init__(self):
        print("Host initialized")
        model = _Model_Wrapper("meta-llama/Llama-3.2-3B-Instruct")
    
    #establishes mcp connection
    def _ConnectMCP():
        print("mock mcp connected")
    def _ShutdownMCP():
        print("mock mcp shutdown")
    
    #Initialize model object using Model_Wrapper
    