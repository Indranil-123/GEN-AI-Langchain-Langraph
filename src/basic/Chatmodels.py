from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import os


load_dotenv()


#creating a LLM object using 
llm = GoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.5)


#testing LLM by generating the response
response = llm.invoke('what is the capital of India')

print(response)