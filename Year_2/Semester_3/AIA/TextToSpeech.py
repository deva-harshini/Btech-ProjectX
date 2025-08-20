import pyttsx3

def setup_engine(rate=150, volume=1.0, voice_id=None):
    """Initialize and configure the TTS engine."""
    engine = pyttsx3.init()

    # Set speaking rate
    engine.setProperty("rate", rate)

    # Set volume (0.0 to 1.0)
    engine.setProperty("volume", volume)

    # Set voice (male/female)
    voices = engine.getProperty("voices")
    if voice_id is not None and 0 <= voice_id < len(voices):
        engine.setProperty("voice", voices[voice_id].id)

    return engine, voices

def speak_text(engine, text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def save_to_audio(engine, text, filename="output.mp3"):
    """Save speech to an audio file."""
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"✅ Audio saved as {filename}")

def main():
    # Setup engine with custom settings
    engine, voices = setup_engine(rate=170, volume=0.9, voice_id=1)

    print("Available voices:")
    for i, v in enumerate(voices):
        print(f"{i}: {v.name} ({v.languages})")

    # Get user input
    choice = input("\nDo you want to (1) type text or (2) read from file? Enter 1 or 2: ")

    if choice == "1":
        text = input("Enter text to speak: ")
    elif choice == "2":
        file_path = input("Enter file path: ")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print("❌ Error reading file:", e)
            return
    else:
        print("Invalid choice.")
        return

    # Speak text
    speak_text(engine, text)

    # Optionally save as audio
    save = input("\nDo you want to save the speech as an MP3 file? (y/n): ").lower()
    if save == "y":
        filename = input("Enter filename (e.g., speech.mp3): ")
        save_to_audio(engine, text, filename)

if __name__ == "__main__":
    main()
