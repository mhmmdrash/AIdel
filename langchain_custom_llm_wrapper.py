from typing import Any, List, Mapping, Optional
import requests

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain import PromptTemplate,  LLMChain

class CustomLLM(LLM):

    api_url: str

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        response = requests.post(self.api_url, json={"question": prompt})
        if response.status_code != 200:
            raise ValueError(f"API request failed with status {response.status_code}.")
        return response.json()["answer"]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"api_url": self.api_url}


#usage
#from langchain_custom_llm_wrapper import CustomLLM 
#local_llm = CustomLLM(api_url="http://65.108.32.184:5000/chat") 
