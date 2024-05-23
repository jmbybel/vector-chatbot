#this will handle functions invoking the ollama LLM via text from other sources

from langchain_community.llms import Ollama


def invokeModel(model, prompt):
    llm = Ollama(model=model)
    return llm.invoke(prompt)


def main():
#    llm = Ollama(model="llama2")
#    llm.invoke("Is this a successful test of invoking the LLM from a Python script?")
    result = invokeModel("llama2", "Is this a successful test of invoking the LLM from a Python script?")
    print(result)


if __name__ == "__main__":
    main()