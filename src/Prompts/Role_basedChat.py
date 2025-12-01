from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate



#importing the  API key
load_dotenv()


#creating my LLm object
llm = GoogleGenerativeAI(model='gemini-2.0-flash',temperature=0.5)


#creating a role based cha prompt
prompt = ChatPromptTemplate([
    ("system", "You are a highly professional data science mentor. Always explain in simple steps."),
    ("human", "Explain the concept of {concept}")
])



final_prompt = prompt.format_messages(concept="Neural Networks")

response = llm.invoke(final_prompt)

print(response)

