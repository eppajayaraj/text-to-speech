from gtts import gTTS
import os

text="Hello, welcome to my github account this is simple text to speech program developed by the python package of gtts"

lang = "en"

obj=gTTS(text=text,lang=lang,slow=False)

obj.save("hello.mp3")

os.system("hello.mp3")