# execute streamlit run main.py

from langchain.llms import CTransformers
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from typing import Any, Dict, List, Union
import sys

# for adding memory to the conversation
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory

model_id = 'TheBloke/Mistral-7B-codealpaca-lora-GGUF'
#'TheBloke/sqlcoder-7B-GGUF'
#'TheBloke/Mistral-7B-codealpaca-lora-GGUF'
config = {'temperature':0.00, 'context_length':8000,} 
llm = CTransformers(model=model_id, 
                    model_type='mistral',
                    config=config,
                    )

template = """As an AI Assistant answer the question provided as input.
Current conversation:
{history}
Human: {input}
AI Assistant:"""
PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)
conversation_buf = ConversationChain(
    llm=llm,
    prompt=PROMPT,
    memory=ConversationBufferMemory()
)

def genai_engine(query):
    response = conversation_buf.run(query)
    return response