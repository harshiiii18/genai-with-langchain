from typing import TypedDict, Optional, Annotated

class student(TypedDict):
    name = str
    age = int


st: student = {'name' : 'harshita', 'age' : '20'}

print(st['name'])    