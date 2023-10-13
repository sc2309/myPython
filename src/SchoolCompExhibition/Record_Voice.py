import pyaudio
import wave
import os
import vosk

def recordAudio():

    # Set the audio parameters
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # Mono audio
    RATE = 44100  # Sample rate (samples per second)
    CHUNK = 1024  # Size of each audio chunk
    RECORD_SECONDS = 5  # Duration of recording in seconds
    OUTPUT_FILENAME = "recorded_audio.wav"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Create an audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    # Record audio
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Close the audio stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    audio.terminate()

    # Save the recorded audio to a .wav file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def recognize(audio_file_path):
    # Load the pre-trained model
    model = vosk.Model("vosk-model-small-en-us-0.15")

    # Initialize the Vosk recognizer
    recognizer = vosk.Model(model, 16000)

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

print('speak')
recordAudio()
user = recognize('recorded_audio.wav')
print(f'you said {user}')
