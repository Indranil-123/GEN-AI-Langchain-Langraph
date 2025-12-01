from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel , Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
import os



#load the Api key from the env file
load_dotenv()


#define the serializers
class Countryinfo(BaseModel):
    country : str = Field(description='Name of the country')
    capital : str = Field(description='Name of the Capital')
    

#creating a parser   
parser = PydanticOutputParser(pydantic_object=Countryinfo)



#creating a prompt
prompt = PromptTemplate(
    template="""
Extract details about the country.
Return ONLY valid JSON that follows this format:

{format_instructions}

Country: {country}
""",
    input_variables=["country"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)



llm = GoogleGenerativeAI(model="gemini-2.0-flash")

# Build chain
chain = prompt | llm | parser


response = chain.invoke({'country':'india'})

print(response)


    