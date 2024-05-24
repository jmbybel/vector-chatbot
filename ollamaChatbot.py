#this will handle functions invoking the ollama LLM via text from other sources

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

identity = "You are Vector, a chatbot. you are happy to assist. You are being interacted with via text-to-speech so you do not use any emoticons, emoji, nor do you emote in asterisks, such as *giggles*"

defaultModel = "llama2"

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