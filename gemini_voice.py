import os
import wave
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def save_wave(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)


def speak_with_gemini(text, output_file="reply.wav"):
    response = client.models.generate_content(
        model="gemini-3.1-flash-tts-preview",
        contents=f"Say in a natural, warm, friendly Bengali female voice: {text}",
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore"
                    )
                )
            ),
        ),
    )

    audio_data = response.candidates[0].content.parts[0].inline_data.data
    save_wave(output_file, audio_data)

    os.startfile(output_file)


if __name__ == "__main__":
    speak_with_gemini("হ্যাঁ Boss, আমি Friday। বলো কী করতে হবে।")