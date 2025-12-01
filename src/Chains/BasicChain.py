from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate



#importing the Keys
load_dotenv()


#creating a LLM object
llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)

#creating a prompt template
prompt = PromptTemplate(
    input_variables=['place'],
    template="What is the best tourist attraction in {place}?"  
)

#creating a chain
chain = prompt | llm

#generating the response
response = chain.invoke({'India'})

print(response)

