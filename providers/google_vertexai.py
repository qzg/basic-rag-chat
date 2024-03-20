# DEVELOPMENT NOTES 

# LANGCHAIN VERSION FROM: https://python.langchain.com/docs/integrations/llms/google_ai
# %pip install --upgrade --quiet  langchain-google-genai

# from langchain_google_genai import GoogleGenerativeAI

# from getpass import getpass

# api_key = getpass()

# llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)
# print(
#     llm.invoke(
#         "What are some of the pros and cons of Python as a programming language?"
#     )
# )

# ---- NATIVE VERSION FROM: https://colab.research.google.com/notebooks/snippets/gemini.ipynb?utm_medium=link&utm_campaign=gemini#scrollTo=eJ2d2cIhcmyw
# The Gemini API allows you to connect to Google's most powerful multi-modal model. This example configures your API key and sends an example message to the API and prints a response.
# Before you start, visit https://makersuite.google.com/app/apikey to create an API key.

# #@title Configure Gemini API key

# import google.generativeai as genai
# from google.colab import userdata

# gemini_api_secret_name = 'GOOGLE_API_KEY'  # @param {type: "string"}

# try:
#   GOOGLE_API_KEY=userdata.get(gemini_api_secret_name)
#   genai.configure(api_key=GOOGLE_API_KEY)
# except userdata.SecretNotFoundError as e:
#    print(f'Secret not found\n\nThis expects you to create a secret named {gemini_api_secret_name} in Colab\n\nVisit https://makersuite.google.com/app/apikey to create an API key\n\nStore that in the secrets section on the left side of the notebook (key icon)\n\nName the secret {gemini_api_secret_name}')
#    raise e
# except userdata.NotebookAccessError as e:
#   print(f'You need to grant this notebook access to the {gemini_api_secret_name} secret in order for the notebook to access Gemini on your behalf.')
#   raise e
# except Exception as e:
#   # unknown error
#   print(f"There was an unknown error. Ensure you have a secret {gemini_api_secret_name} stored in Colab and it's a valid key from https://makersuite.google.com/app/apikey")
#   raise e

# #connect to the API and send an example message

# text = 'What is the velocity of an unladen swallow?' #@param {type: 'string'}

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])

# response = chat.send_message(text)
# response.text