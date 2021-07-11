import json 
from difflib import get_close_matches
Data=json.load(open("data.json"))

class Dictionary():
    def __init__(self,word):
        self.word=word.lower()
    def searchword(self):
        if self.word in Data:
            return Data[self.word]
        elif len(get_close_matches(self.word,Data.keys()))>0:
             suggest=input("suggestion for your word %s press y for Yes and n for No " %get_close_matches(self.word,Data.keys())[0])
             if suggest=="y":
                 return Data[get_close_matches(self.word,Data.keys())[0]]
             elif suggest=="n":
                 return ("word does not exist ")
             else:
                 return("Enter a valid word ")
        else:
            return("Check the word again")

urword=Dictionary(input("Enter a word "))
if type(urword)==list:
    for i in urword:
        print(i)
else:
    print(urword.searchword())


             



        

