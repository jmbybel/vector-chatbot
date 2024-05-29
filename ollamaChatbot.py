#this will handle functions invoking the ollama LLM via text from other sources

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import OLLAMA_MODEL, OLLAMA_IDENTITY


identity = OLLAMA_IDENTITY
defaultModel = OLLAMA_MODEL


def invokeModel(inputText, model=defaultModel):

    llm = Ollama(model=model)
    output_parser = StrOutputParser()

    prompt = ChatPromptTemplate.from_messages([
        ("system", identity),
        ("user", "{input}")
    ])
    chain = prompt | llm | output_parser
    
    return  chain.invoke({"input": inputText})


def main():
    result = invokeModel("This prompt is being raised from a separate Python program. Did it successfully reach you for a response?")
    print(result)


if __name__ == "__main__":
    main()