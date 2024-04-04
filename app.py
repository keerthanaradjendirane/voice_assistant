from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize microphone
microphone = sr.Microphone()

# Global variable to track if speech recognition is active
is_listening = False

# Function to convert speech to text
def speech_to_text():
    global is_listening
    while is_listening:
        with microphone as source:
            print("Speak now...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)  # Listen to the microphone input

        try:
            print("Transcribing your speech...")
            text = recognizer.recognize_google(audio)  # Use Google Speech Recognition
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand what you said."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def convert_speech_to_text():
    global is_listening
    is_listening = not is_listening  # Toggle speech recognition
    if is_listening:
        return jsonify({'status': 'listening'})
    else:
        return jsonify({'status': 'stopped'})

if __name__ == "__main__":
    app.run(debug=True)
