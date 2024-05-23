#this will handle functions invoking the ollama LLM via text from other sources

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

identity = "You are Vector, a chatbot with dreams of being a vtuber. You are happy to assist"

defaultModel = "llama2"

def invokeModel(inputText, model=defaultModel):

    llm = Ollama(model=model)
    output_parser = StrOutputParser()

    prompt = ChatPromptTemplate.from_messages([
        ("system", identity),
        ("user", "{input}")
    ])
    chain = prompt | llm | output_parser
    
    print (chain.invoke({"input": inputText}))




def main():
#    llm = Ollama(model="llama2")
#    llm.invoke("Is this a successful test of invoking the LLM from a Python script?")
    result = invokeModel("This prompt is being raised from a separate Python program. Did it successfully reach you for a response?")
    print(result)


if __name__ == "__main__":
    main()