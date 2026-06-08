from googletrans import Translator
from gtts import gTTS
import os

# Initialize translator
translator = Translator()

# Language options
languages = {
    "1": ("Malayalam", "ml"),
    "2": ("Hindi", "hi"),
    "3": ("Tamil", "ta"),
    "4": ("Telugu", "te"),
    "5": ("Kannada", "kn")
}

# Input text
text = input("Enter the Text in English: ")

# Display language menu
print("\nAvailable Languages:")
for key, (name, _) in languages.items():
    print(f"{key}. {name}")

# User choice
choice = input("\nChoose language (1-5): ")

if choice in languages:
    lang_name, lang_code = languages[choice]

    try:
        # Translate text
        translated = translator.translate(text, dest=lang_code)
        translated_text = translated.text

        print(f"\n{lang_name} Translation:")
        print(translated_text)

        # Convert translated text to speech
        tts = gTTS(text=translated_text, lang=lang_code)

        # Save audio file
        filename = f"{lang_name}.mp3"
        tts.save(filename)

        print(f"\nAudio saved as: {filename}")

        # Play audio (Windows)
        os.system(f'start "" "{filename}"')

    except Exception as e:
        print("Error:", e)

else:
    print("Invalid choice. Please select a number between 1 and 5.")