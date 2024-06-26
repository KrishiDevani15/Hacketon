import google.generativeai as genai
import speech_recognition as sr
import json
import pyttsx3

# Configure GenerativeAI API keyd
genai.configure(api_key="AIzaSyDiHIeAsfCOY2bhV_S1bXk4Y966xFay4s8")

# Initialize GenerativeModel
model = genai.GenerativeModel('gemini-pro')

# Define function to transform conversations to JSON
def transform_conversations_to_json(conversations):
    transformed_data = []
    for conversation in conversations:
        transformed_conversation = {}
        # Extract caller information
        caller_info = {}
        caller_info["name"] = conversation["caller_name"]
        caller_info["phone_number"] = conversation["caller_phone"]
        transformed_conversation["caller"] = caller_info
        # Extract issue details
        issue_details = {}
        issue_details["description"] = conversation["issue_description"]
        issue_details["first_time_reporting"] = conversation["first_time_reporting"]
        transformed_conversation["issue"] = issue_details
        # Extract device details (laptop, printer, etc.)
        device_details = {}
        device_details["type"] = conversation["device_type"]
        device_details["make"] = conversation.get("device_make", None)
        device_details["model"] = conversation.get("device_model", None)
        device_details["model_number"] = conversation.get("device_model_number", None)
        transformed_conversation[conversation["device_type"] + "_details"] = device_details
        # Extract preferred contact time
        contact_time = {}
        contact_time["day"] = conversation["contact_day"]
        contact_time["time_range"] = conversation["contact_time_range"]
        transformed_conversation["preferred_contact_time"] = contact_time
        transformed_data.append(transformed_conversation)
    return transformed_data

# Define function to generate response based on transformed JSON data
def generate_response(input_text):
    # Convert input text to JSON
    conversations = json.loads(input_text)
    # Transform conversations to JSON format
    transformed_conversations = transform_conversations_to_json(conversations)
    # Generate response based on transformed JSON data
    response = model.generate_content(json.dumps(transformed_conversations) + "limit the response to 2 sentence")
    return response.text

# Define function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()

    def convert_speech_to_text():
        with sr.Microphone() as source:
            print("Please say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Sorry, an error occurred: {e}")

    def speak(text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1)
        engine.say(text)
        engine.runAndWait()
        
    # Introduction
    introduction = "Hello! I'm here to assist you. You can ask me anything or give me commands. To exit, simply say 'exit'. Let's get started!"
    print(introduction)
    speak(introduction)

    while True:
        user_input = convert_speech_to_text()
        if user_input:
            response = generate_response(user_input)
            print("Gemini:", response)
            speak(response)

            # Optionally, you can add a condition to exit the loop
            if user_input.lower() == "exit":
                speak("Goodbye!")
                break

if __name__ == "__main__":
    speech_to_text()
