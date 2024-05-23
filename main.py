
from langchain_community.llms import Ollama


#This file will become a minimal launcher for this application. any sample/testing data will be removed.
#other files will 
# 1) handle interactions with the llama2 model specifically
# 2) provide a general LLM wrapper to swap models trivially
# 3) create a text-to-speech engine to convert model responses to speech, and play them back to the user
# 4) create a speech-to-text engine to convert user speech to text, and pass it to the model

def main():
    llm = Ollama(model="llama2")
    llm.invoke("Is this a successful test of invoking the LLM from a Python script?")



if __name__ == "__main__":
    main()