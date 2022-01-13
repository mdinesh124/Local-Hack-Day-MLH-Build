#Translate any language's text to english

import googletrans
from googletrans import Translator
translater = Translator()

print(googletrans.LANGUAGES)
text = input("Enter the text to be translated to english")
result = translater.translate(text, dest='en')
print(result)
