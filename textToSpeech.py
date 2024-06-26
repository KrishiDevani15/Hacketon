from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the audio to a file
    tts.save("response.mp3")

    # Play the audio
    os.system("start response.mp3")  # For Windows
    # os.system("mpg321 response.mp3")  # For Linux (requires mpg321 installed)

# Example usage:
text = "Hello! This is a human-like tone audio response."   
text_to_speech(text)
