import pyttsx3

def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak the provided text
    engine.say(text)
    
    # Wait for speech to finish
    engine.runAndWait()

# Example usage
speak("Hello! I am your virtual assistant.")