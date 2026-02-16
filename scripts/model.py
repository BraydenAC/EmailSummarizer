from .logger import logger

class _Model_Wrapper:
    def __init__(self, model_name, model_config: dict = {}):
        logger.debug("Model initialized")
    
    def generate_summary(self, input: str):
        logger.debug(f"generate_summary called with input of '{input}'")
        return input