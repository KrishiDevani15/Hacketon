import pyttsx3

def configure_engine(engine):
    # Adjust speech rate (words per minute)
    engine.setProperty('rate', 150)  # You can adjust this value to change the speaking rate

    # Adjust volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)  # Increase or decrease as needed

    # Select a human-like voice (if available)
    voices = engine.getProperty('voices')
    if voices:
        for voice in voices:
            if "english" in voice.languages[0].lower():
                engine.setProperty('voice', voice.id)
                break

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Configure the engine for a more human-like response
    configure_engine(engine)

    # Convert text to speech
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()

# Example usage:
text = "Hello! This is a more human-like text-to-speech demonstration using pyttsx."
text_to_speech(text)
