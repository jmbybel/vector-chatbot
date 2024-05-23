
from gtts import gTTS
from audioPlayer import play_mp3

import os

#hardcode audio file save/load location to be windows directory C:/programming/data/sound/gtts
baseDirectory = "C:/programming/data/sound/gtts"
language = "en"

#generate a hello world audio file with gtts
#if directories do not exist, create them
def generateHelloWorldAudio():
    #if the file already exists, just return the file path
    if os.path.isfile(baseDirectory + "/helloWorld.mp3"):
        return baseDirectory + "/helloWorld.mp3"

    tts = gTTS(text="Hello World", lang=language)
    fullAudioFilePath = baseDirectory + "/helloWorld.mp3"
    util_createPathIfMissing(baseDirectory)
    tts.save(fullAudioFilePath)
    return fullAudioFilePath


def playAudioFile(audioFile):
    play_mp3(audioFile)
#    os.system("start " + audioFile)



#utility function to create directories if they do not exist
def util_createPathIfMissing(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main():
    filePath = generateHelloWorldAudio()
    playAudioFile(filePath)

if __name__ == "__main__":
    main()