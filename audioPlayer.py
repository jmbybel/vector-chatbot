import speech_recognition as sr

import vlc
import time

#Play an MP3 file, but will read an MP3 file.
#Note there is a delay between player.play() firing and player.is_playing() being true. the 0.05 second sleep time is a magic number that works locally.
#Not 100% sure i am satisfied with using VLC just yet but it seems to work for the moment.
def play_mp3_vlc(mp3_file):
    player = vlc.MediaPlayer(mp3_file)
    player.play()
    time.sleep(0.05)
    while player.is_playing():
        time.sleep(0.1)
    player.stop()


#Record audio from the microphone and return the text
#TODO make sure this doesn't save the audio somewhere without being maintained/deleted
def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        print("Sorry, I didn't get that.")



#just to test things inline
def main():
    text = record_audio()
    print(text)

if __name__ == "__main__":
    main()