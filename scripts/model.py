from .logger import logger
from dotenv import load_dotenv
from huggingface_hub import login
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

class _Model_Wrapper:
    def __init__(self, model_name, model_config: dict = {}):
        logger.debug("Model initialized")

        #Log into huggingface
        try:
            load_dotenv()
            key = os.getenv("HF_TOKEN")
            login(key)
        except:
            logger.warning("Login to hf failed!  Ignore if model is not gated.")
        
        #Load model and its tokenizer
        try:
            logger.info("Loading model")
            hf_config = AutoConfig.from_pretrained(model_name, **model_config)
            self.hf_model = AutoModelForCausalLM.from_pretrained(model_name, config=hf_config)
            self.hf_tokenizer = AutoTokenizer.from_pretrained(model_name)
        except MemoryError as e:
            logger.critical("Ran out of memory while loading model!")
            exit(42)
    
    def generate_summary(self, input: str):
        logger.debug(f"generate_summary called with input of '{input}'")
        return input
    
    def pipeline()