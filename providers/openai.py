# DEVELOPMENT DOCUMENTATION FROM: https://python.langchain.com/docs/integrations/llms/openai
# get a token: https://platform.openai.com/account/api-keys

# from getpass import getpass

# OPENAI_API_KEY = getpass()
# import os

# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# #optional - if using default organization
# OPENAI_ORGANIZATION = getpass()

# os.environ["OPENAI_ORGANIZATION"] = OPENAI_ORGANIZATION

# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_openai import OpenAI

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate.from_template(template)

# llm = OpenAI()

# # ALTERNATIVELY
# llm = OpenAI(openai_api_key="YOUR_API_KEY", openai_organization="YOUR_ORGANIZATION_ID")

# question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

# llm_chain.run(question)


from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Interface implementation methods
def load_embedding_model():
    print("load_openai_embedding")
    # Get the OpenAI Embedding
    return OpenAIEmbeddings()

def load_llm():
    print("load_openai_model")
    # Get the OpenAI Chat Model
    return ChatOpenAI(
        temperature=0.3,
        model='gpt-4-0125-preview',
        streaming=True,
        verbose=True
    )

# # Interface implementation methods
# def load_embedding_model():
#     print("load_openai_embedding")
#     # Get the OpenAI Embedding
#     return OpenAIEmbeddings()

# def load_llm():
#     print("load_openai_model")
#     # Get the OpenAI Chat Model
#     return ChatOpenAI(
#         temperature=0.3,
#         model='gpt-4-0125-preview',
#         streaming=True,
#         verbose=True
#     )