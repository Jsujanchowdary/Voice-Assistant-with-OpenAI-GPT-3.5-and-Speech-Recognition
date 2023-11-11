import openai
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import tempfile
import pyttsx3

class VoiceAssistant:
    def __init__(self):
        # Set your OpenAI API key
        openai.api_key = "add_your_API_KEY"
        # Initialize the assistant's history
        self.chat_history = [
            {"role": "system", "content": "You are a helpful assistant. The user is English. Only speak English."}
        ]

    def listen(self):
        print("Listening...")
        # Record the audio
        recording_duration = 3  # Record for 3 seconds
        sample_rate = 44100  # Sample rate

        audio_recording = sd.rec(int(recording_duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
        sd.wait()

        # Save the NumPy array to a temporary wav file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
            wavfile.write(temp_wav_file.name, sample_rate, audio_recording)

            # Use the temporary wav file in the OpenAI API
            transcript = openai.Audio.transcribe("whisper-1", temp_wav_file)

        print(f"User: {transcript['text']}")
        return transcript['text']

    def think(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_history,
            temperature=0.5
        )
        assistant_response = dict(response.choices[0])['message']['content']
        self.chat_history.append({"role": "system", "content": assistant_response})
        print('Assistant: ', assistant_response)
        return assistant_response

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    assistant = VoiceAssistant()

    while True:
        user_input = assistant.listen()

        if "goodbye" in user_input.strip().lower():
            print("Assistant: Goodbye! Have a great day!")
            assistant.speak("Goodbye! Have a great day!")
            break

        assistant_response = assistant.think(user_input)
        assistant.speak(assistant_response)
