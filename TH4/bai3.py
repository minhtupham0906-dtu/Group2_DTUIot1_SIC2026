from openai import OpenAI
client = OpenAI()  # Initialize OpenAI client (reads API key from environment)

def audio_to_text(filename: str = "input.wav") -> str:
    with open(filename, "rb") as audio_file:  # Open the WAV file in binary read mode
        # Send the audio to the transcription (STT) model
        result = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",      # STT model name
            file=audio_file,                # audio file object
            response_format="text",         # ask for plain text output
            prompt="The user will speak English commands such as 'turn on', 'turn off', or 'blink'"
        )

    return result.strip()  # Remove space and return the text

if __name__ == "__main__":
    text = audio_to_text("input.wav")
    print("Recognized text:", text)
