from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


#import the api Key
load_dotenv()

#creating the llm object
llm = GoogleGenerativeAI(model='gemini-2.0-flash',temperature=0.5)


prompt = PromptTemplate(
    input_variables=['topic',"detail_level"],
    template='''
    
    You are an AI expert. Explain the topic below.

Topic: {topic}
Detail Level: {detail_level}

Provide a clear, structured, and easy explanation.
    
    '''
)


finalTemplate = prompt.format(
    topic="Machine Learning",
    detail_level="Beginner-friendly"
)

response = llm.invoke(finalTemplate)

print(response)