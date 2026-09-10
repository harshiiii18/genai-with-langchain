from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.6-flash')

prompt1 = PromptTemplate(
    template= "Geneate a detail report about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "give me 5 most important points in this report {text} and no bold text give ",
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

topic = input("write a toipc : ")

result = chain.invoke({'topic' : topic})
print(result)

chain.get_graph().print_ascii()