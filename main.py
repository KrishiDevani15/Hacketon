import tkinter as tk
from tkinter import scrolledtext
import threading
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import re

data = {
    "name": "",
    "phone_number": "",
    "address": "",
}

genai.configure(api_key="AIzaSyDiHIeAsfCOY2bhV_S1bXk4Y966xFay4s8")  # Replace with your API key
model = genai.GenerativeModel('gemini-pro')

def generate_response(input_text):
    response = model.generate_content(input_text + ", And give the response under 300-400 characters")
    return response.text

def extract_names(sentence):
    # Regular expression to find capitalized words
    pattern = r'\b[A-Z][a-z]*\b'

    # Find all matches in the sentence
    matches = re.findall(pattern, sentence)

    # Filter out single-letter words
    names = [match for match in matches if len(match) > 1]

    return names


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

    def on_start_button():
        start_button['state'] = 'disabled'
        stop_button['state'] = 'normal'
        threading.Thread(target=start_listening).start()

    def on_stop_button():
        stop_button['state'] = 'disabled'
        start_button['state'] = 'normal'

    def start_listening():
        # Introduction
        introduction = "Hi, this is Mukul, your smart solution assistant. How may I help you?"
        print(introduction)
        output_text.insert(tk.END, "Assistant: " + introduction + "\n\n")
        speak(introduction)
        
        user_intput = convert_speech_to_text()
        name = extract_names(user_intput)
        print(name)

        if name==[]:
            def jump():
                pass
            
            speak("Can you provide me with your name please")
            user_intput = convert_speech_to_text()
            name = extract_names(user_intput)
            
            if name == []:
                jump()
        
        
        while True:
            user_input = convert_speech_to_text()
            
            name = extract_names(user_input)
            print(name)
            
            if name == []:
                speak("Can you tell your name please")
            else :
                if user_input:
                    response = generate_response(user_input)
                    output_text.insert(tk.END, "User: " + user_input + "\n\n")
                    output_text.insert(tk.END, "Assistant: " + response + "\n\n")
                    output_text.see(tk.END)
                    speak(response)

                    # Optionally, you can add a condition to exit the loop
                    if user_input.lower() == "exit":
                        speak("Goodbye!")
                        break

    # Create UI
    root = tk.Tk()
    root.title("Gemini Voice Interaction")

    start_button = tk.Button(root, text="Start Listening", command=on_start_button)
    start_button.grid(row=0,column=0, pady=(20, 0))

    stop_button = tk.Button(root, text="Stop Listening",command=on_stop_button, state='disabled')
    stop_button.grid(row=0,column=1, pady=(20, 0))

    output_text = scrolledtext.ScrolledText(root,width=100,height=20)
    output_text.grid(row=1, columnspan=2, pady=20, padx=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    speech_to_text()