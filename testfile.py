
from langchain_community.llms import Ollama


#This file is a temporary tester for any code being experimented with. this will not be used in the real project.

def main():
    llm = Ollama(model="llama2")
    llm.invoke("Is this a successful test of invoking the LLM from a Python script?")



if __name__ == "__main__":
    main()