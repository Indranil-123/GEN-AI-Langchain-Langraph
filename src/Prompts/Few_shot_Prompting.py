from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


#importing the Key
load_dotenv()

#generating the LLM object
llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)



#creating a prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a smart AI that explains terms in a short and simple way."),

    ("human", "What is Machine Learning?")
    , ("assistant", "Machine Learning is a technique that allows computers to learn patterns from data to make predictions."),

    ("human", "What is Deep Learning?")
    , ("assistant", "Deep Learning is an advanced form of ML that uses neural networks with many layers to learn complex patterns."),

    ("human", "What is Data Science?")
    , ("assistant", "Data Science uses data + algorithms to extract insights and support decision-making."),

    # New question (The model will follow the same pattern)
    ("human", "What is Reinforcement Learning?")
])



#creating final object
messages = prompt.format_messages()
response = llm.invoke(messages)

print(response)
