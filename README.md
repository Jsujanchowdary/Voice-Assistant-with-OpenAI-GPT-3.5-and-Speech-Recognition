# Voice Assistant with OpenAI GPT-3.5 and Speech Recognition

This project implements a voice assistant using OpenAI's GPT-3.5 language model and speech recognition. The assistant is capable of listening to user input, generating responses using GPT-3.5, and speaking back the responses.

## Features

- **Speech Recognition:** Utilizes the `sounddevice` library to record and transcribe user input.
- **Chat Interaction:** Communicates with the OpenAI GPT-3.5 model for generating contextual responses.
- **Text-to-Speech:** Employs `pyttsx3` for converting the assistant's responses into speech.

## How It Works

1. **Listening to User Input:**
   - The assistant records user input using the `sounddevice` library for a specified duration.
   - The recorded audio is then transcribed into text using OpenAI's GPT-3.5 Audio API.

2. **Generating Responses:**
   - The assistant maintains a chat history, leveraging OpenAI's GPT-3.5 model to generate responses based on the conversation context.
   - The `think` method uses the OpenAI Chat Completion API to get responses.

3. **Speaking Back Responses:**
   - The `pyttsx3` library is used for converting the assistant's generated responses into speech.

## Setup

1. Install the required dependencies:

   ```bash
   pip install openai
   pip install sounddevice
   pip install numpy
   pip install scipy
   pip install pyttsx3  

## `think` Method

The core functionality of generating responses and interacting with the OpenAI GPT-3.5 model is encapsulated in the `think` method of the `VoiceAssistant` class. This method orchestrates the conversation between the user and the assistant.

```python
def think(self, user_input):
    # Append user input to the chat history
    self.chat_history.append({"role": "user", "content": user_input})

    # Use OpenAI's Chat Completion API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.chat_history,
        temperature=0.5
    )

    # Extract the assistant's response from the API response
    assistant_response = dict(response.choices[0])['message']['content']

    # Append the assistant's response to the chat history
    self.chat_history.append({"role": "system", "content": assistant_response})

    # Print and return the assistant's response
    print('Assistant: ', assistant_response)
    return assistant_response
```
## output

![image](https://github.com/Jsujanchowdary/Voice-Assistant-with-OpenAI-GPT-3.5-and-Speech-Recognition/assets/91127394/71a1f52b-1204-4b0f-8b85-e86a217e9c52)
