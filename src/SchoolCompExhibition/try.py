import vosk

# Specify the path to the extracted model files
model_path = "C:\sarthak\py\SchoolCompExhibition\vosk-model-small-en-us-0.15"

# Initialize the Vosk recognizer with the English model
recognizer = vosk.Model(model_path)

audio_file = "recorded_audio.wav"

# Open and read the audio file
with open(audio_file, "rb") as audio_data:
    audio = audio_data.read()

# Perform speech recognition
result = recognizer.recognize(audio)

# Extract and print the recognized text
recognized_text = result["text"]
print("Recognized text:", recognized_text)
