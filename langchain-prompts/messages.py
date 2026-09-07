from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

messages = [
    SystemMessage(content="you are a helpful assistent"),
    HumanMessage(content="tell a about langchain")
]

result = model.invoke(messages)

if isinstance(result.content, list):
    text = "".join(
        block.get("text", "") for block in result.content if isinstance(block, dict)
    )
else:
    text = result.content 

messages.append(AIMessage(content=text))

print(messages)