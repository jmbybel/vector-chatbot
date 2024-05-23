
from langchain_community.llms import Ollama
from audioPlayer import play_mp3_vlc, record_audio
from googleTTS import generateAudioFile
from ollamaChatbot import invokeModel



#This file will eventually become  launcher for this application. any sample/testing data will be removed.
#other files will 
# 1) handle interactions with the llama2 model specifically
# 2) provide a general LLM wrapper to swap models trivially
# 3) DONE create a text-to-speech engine to convert model responses to speech, and play them back to the user
# 4) DONE create a speech-to-text engine to convert user speech to text, and pass it to the model


#record audio by calling record_audio, return the text from it, generate mp3 of the same text via gTTS
#save the mp3 to the baseDirectory with a filename of the unix timestamp for now
def testFeedbackLoop():
    audioText = record_audio()
    
    resultAudio = generateAudioFile(audioText)
    play_mp3_vlc(resultAudio)

#record audio, pass it to the model as text, receive response, play the response as audio
def testOneShot():
    audioText = record_audio()
    response = invokeModel(audioText)
    botAudioFile = generateAudioFile(response)
    play_mp3_vlc(botAudioFile)

def main():
    result = testOneShot()
    print(result)
#    testFeedbackLoop()
#    llm = Ollama(model="llama2")
#    llm.invoke("Is this a successful test of invoking the LLM from a Python script?")



if __name__ == "__main__":
    main()