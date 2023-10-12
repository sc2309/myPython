import os
import vosk
import pyaudio

def offline_speech_recognition(audio_file_path):
    # Load the pre-trained model
    model = vosk.Model("model")

    # Initialize the Vosk recognizer
    recognizer = vosk.KaldiRecognizer(model, 16000)

    # Open the audio file
    audio_file = open(audio_file_path, "rb")
    
    # Initialize PyAudio for audio input
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    
    # Initialize variables to store recognized text
    result = ""

    while True:
        data = audio_file.read(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result += recognizer.Result()
    
    # Finalize the recognition process
    result += recognizer.FinalResult()

    return result

if __name__ == "__main__":
    # Provide the path to an audio file (16kHz WAV format)
    audio_file_path = "gg.wav"

    if not os.path.exists(audio_file_path):
        print("Audio file not found.")
    else:
        result = offline_speech_recognition(audio_file_path)

        if result:
            print("Recognized Text:", result)
        else:
            print("No speech recognized.")
