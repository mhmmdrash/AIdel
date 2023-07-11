from langchain import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.chains import LLMMathChain, LLMChain, SQLDatabaseChain, ConversationChain, SimpleSequentialChain, SequentialChain
from langchain.agents import Tool, load_tools, initialize_agent
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
import os
from apikey import apikey
import streamlit as st
import avatar
import get_video
import time
from langchain_custom_llm_wrapper import CustomLLM 
local_llm = CustomLLM(api_url="http://65.108.32.164:5000/chat") 

os.environ['OPENAI_API_KEY'] = "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" 

st.title('🦜🔗 AIdel 🦜🔗')
text = st.text_input("Enter you Question here: ")
# initialise the llm instance
# llm = OpenAI(
#     model_name = "text-davinci-003",
#     verbose = True,
#     temperature = 0.9,
# )

llm = local_llm

if st.button("ask", type="primary"):
    res = llm(text) 
    response_id = avatar.post_req(res)
    time.sleep(10)
    url = get_video.get_url(response_id)
    # url = "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C104415476892080133972/tlk_w617jorEiiXYgJse8rG30/1684411696575.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1684498100&Signature=2KaUv7nBSVNFN0dPySWvfR3aFIM%3D&X-Amzn-Trace-Id=Root%3D1-64661534-2ca585ea2226d800073067d2%3BParent%3Dc89fbcbaab8eccb8%3BSampled%3D1%3BLineage%3D6b931dd4%3A0"
    if url:
        st.video(url)