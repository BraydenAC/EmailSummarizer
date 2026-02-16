from .logger import logger
from dotenv import load_dotenv
from huggingface_hub import login
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, pipeline

class _Model_Wrapper:
    def __init__(self, model_name, model_config: dict = {}):

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
            hf_model = AutoModelForCausalLM.from_pretrained(model_name, config=hf_config)
            hf_tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.hf_pipeline = pipeline("text-generation", model=hf_model, tokenizer=hf_tokenizer, pad_token_id = hf_tokenizer.eos_token_id)
            logger.info(f"{model_name} loaded as active model")
        except MemoryError as e:
            logger.critical("Ran out of memory while loading model!")
            exit(42)
    
    def generate_summary(self, input: str):
        logger.debug(f"generate_summary called with input of '{input}'")
        
        output = self.hf_pipeline(input, return_text=False)[0]["generated_text"]
        return output