from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import warnings

load_dotenv()
warnings.filterwarnings("ignore")

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

result = model.invoke("write a 5 line poem on peacock in hinglish")

#  result.content se only AI output ke liye 
if isinstance(result.content, list):
    text = "".join(
        block.get("text", "") for block in result.content if isinstance(block, dict)
    )
else:
    text = result.content

print( "AI : " , text)