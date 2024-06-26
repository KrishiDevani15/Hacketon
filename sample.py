import speech_recognition as sr
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to extract information from text using NER
def extract_information(text):
    doc = nlp(text)
    info = {}
    for ent in doc.ents:
        info[ent.label_] = ent.text
    return info

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results"

# Main function to simulate CVA
def simulate_cva():
    # Get input from user (simulating speech input)
    user_input = speech_to_text()
    print("User Input:", user_input)
    
    # Extract information using NER
    extracted_info = extract_information(user_input)
    
    # Print extracted information
    print("Extracted Information:")
    for key, value in extracted_info.items():
        print(f"{key}: {value}")

# Simulate the CVA
simulate_cva()