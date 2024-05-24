
from langchain_community.llms import Ollama
from audioPlayer import play_mp3_vlc, record_audio
from googleTTS import generateAudioFile
from ollamaChatbot import invokeModel
import keyboard
import time
import os


audioFileNames = []

#one round-trip to and from the chatbot.
# record audio, pass it to the model as text, receive response, play the response as audio
def interactWithBot():
    global audioFileNames

    audioText = record_audio()
    #if audioText is empty, blank, or whitespace, return.
    if not audioText:
        return
    response = invokeModel(audioText)
    botAudioFile = generateAudioFile(response)
    play_mp3_vlc(botAudioFile)
    audioFileNames.append(botAudioFile)


'''
def interactWithBot_byteArray():
    audioText = record_audio()
    #if audioText is empty, blank, or whitespace, return.
    if not audioText:
        return
    response = invokeModel(audioText)
    botAudioFile = generateDirectPlayBytes(response)
    play_bytesIo_pydub(botAudioFile)
'''

#will listen for a F5 button press
#If detected will attempt to perform a full interaction with the chatbot.
# TODO find a sweet sleep delay for clean polling.
def listenForF5():
    global audioFileNames

    while True:
        if keyboard.is_pressed('F4'):
            interactWithBot()
        elif keyboard.is_pressed('F6'):
            print("F6 pressed -- exiting")
            break
        else:
            if len(audioFileNames) > 0:
                deleteMe = audioFileNames.pop()
                if os.path.isfile(deleteMe):
                    os.remove(deleteMe)
            time.sleep(0.5)
            
    for audioFile in audioFileNames:
        if os.path.isfile(audioFile):
            os.remove(audioFile)


#record audio by calling record_audio, return the text from it, generate mp3 of the same text via gTTS
#save the mp3 to the baseDirectory with a filename of the unix timestamp for now
def testFeedbackLoop():
    audioText = record_audio()
    
    resultAudio = generateAudioFile(audioText)
    play_mp3_vlc(resultAudio)

#record audio, pass it to the model as text, receive response, play the response as audio
def testOneShot():
    interactWithBot()

def main():
    listenForF5()
#    result = testOneShot()
#    print(result)




if __name__ == "__main__":
    main()