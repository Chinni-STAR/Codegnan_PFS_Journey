'''
import pyttsx3
engine=pyttsx3.init()
def audio_text(text):
    engine.say(text)
#audio_text("hello,i am your assiatant")
name="chinni"
location="Visakhapatnam"
collegename = "vignan's college"
year="2026"
branch="CSE"
skills="HTML,CSS,MS office,python"
hobbies="dancing,drawing"
audio_text("My name is"+name)
audio_text("I am  from "+location)
audio_text("I am recent graduate at "+collegename+"in"+year)
audio_text("in the branch of "+branch)
audio_text("My skills:"+skills)
audio_text("i am interested in "+hobbies)
engine.runAndWait()
'''

import pyttsx3
engine=pyttsx3.init()
def audio_text(text):
    engine.say(text)
text_=input("Enter your msg:").lower()
name="user"
if "my name is" in text_:
    name =text_.split("my name is")[-1].strip()
elif "name is" in text_:
    name =text_.split("name is")[-1].strip()
    
if text_ in ["hi","hello","hey"]:
    
    response="Hello! how can i help you?"
elif "name" in text_:
    response=f"Hello! {name} how can i help you?"
else:
    response="Sorry,I didn't understand that"
print(response)
audio_text(response)
engine.runAndWait()

































    
