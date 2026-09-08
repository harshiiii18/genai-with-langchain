from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal, Annotated
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.6-flash')

#schema 
class preprocess(BaseModel): 
    key_themes: list[str] = Field(description="")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")




s = model.with_structured_output(preprocess)

review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh

"""
 
result = s.invoke(review)

print(result)


# key_themes=['Performance', 'Camera quality', 'Battery life', 'S-Pen', 'Weight and Size', 'Software bloatware', 'Price'] summary='A highly positive review of the Samsung Galaxy S24 Ultra highlighting its top-tier performance, excellent 200MP camera, and battery life, despite minor drawbacks like its heavy size, bloatware, and steep price.' sentiment='pos' pros=['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'] cons=['Heavy weight and large size make one-handed use uncomfortable', 'One UI comes with Samsung bloatware', 'High price tag at $1,300'] name='Nitish Singh'