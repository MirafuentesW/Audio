import chunk
import pyaudio
import wave
import speech_recognition as sr
import subprocess
import subprocess as say

def say(text):
    subprocess.call('say ' + text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()

def initSpeech():
    print("Listening")
    play_audio("./audio/so-proud-notification.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("./audio/ringtone-you-would-be-glad-to-know.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Coudn't understand you, bro.")

    print("Your command:")
    print(command)
    say('you said: ' + command)


initSpeech()