from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate,ChatPromptTemplate


#importing the API key
load_dotenv()


#creating the Langchain object
llm = GoogleGenerativeAI(model='gemini-2.0-flash',temperature=0.3)


#summary prompt
summary_prompt = ChatPromptTemplate.from_template(
    "Write a short professional summary about: {topic}"
)

#question prompt
question_prompt = ChatPromptTemplate.from_template(
    "Based on this summary:\n\n{summary}\n\nGenerate 5 interview questions."
)


#sequential Process Function
def Sequential_process(text):
    
    #1. Summary Chain
    summary_chain = summary_prompt | llm
    #2. Summary chain response
    summary_result = summary_chain.invoke({'topic'})
    #3. extract the main content
    summary_text = summary_result
    
    
    #step 2
    question_chain = question_prompt | llm
    questions_result = question_chain.invoke({"summary": summary_text})
    
    return summary_text,questions_result



topic_input = "Machine Learning"
summary, questions = Sequential_process(topic_input)


print('summary',summary)
print('questions',questions)