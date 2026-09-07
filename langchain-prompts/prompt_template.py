from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

tempalte2 = PromptTemplate(
    template="Greet this person in 5 languages. The name of the person is {name}",
    input_variables=['name']
)

prompt = tempalte2.invoke({'name' : 'harshita'})

result = model.invoke(prompt)

print(result.content)

