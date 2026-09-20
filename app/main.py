import sys
import os
import subprocess
import time
import speech_recognition as sr
import pyttsx3

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.agent.runtime import AgentRuntime
from app.llm.ollama import OllamaClient

def ensure_ollama():
    client = OllamaClient()
    if not client.check_connection():
        print("Starting Ollama server in the background...")
        try:
            # Start Ollama detached, ignoring output
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Wait for the server to be responsive
            for _ in range(15):
                time.sleep(1)
                if client.check_connection():
                    print("Ollama is up and running!")
                    break
            else:
                print("Warning: Ollama didn't respond in time. The agent might fail to connect.")
                return
        except FileNotFoundError:
            print("Error: 'ollama' command not found on your system. Please install Ollama first.")
            sys.exit(1)
            
    if not client.has_model():
        print(f"Model '{client.model}' not found locally.")
        print(f"To fix this, please open another terminal and run: ollama pull {client.model}")
        print("Or if you're using a different model, update app/config.py.")
        sys.exit(1)

def main():
    ensure_ollama()
    print("Deadpool Agent (V0.5 MVP) starting...")
    runtime = AgentRuntime()
    
    print("Agent is ready. Type 'exit' or 'quit' to stop.")
    print("Type '/voice' to toggle voice mode.")
    
    voice_mode = False
    recognizer = sr.Recognizer()
    tts_engine = pyttsx3.init()
    # Optional: adjust voice rate or volume here
    tts_engine.setProperty('rate', 170)

    while True:
        try:
            if voice_mode:
                print("\n[Listening... Speak now]")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
                print("[Processing speech...]")
                try:
                    user_input = recognizer.recognize_google(audio)
                    print(f"You (Voice): {user_input}")
                except sr.UnknownValueError:
                    print("Deadpool: Sorry, I didn't catch that.")
                    continue
                except sr.RequestError as e:
                    print(f"Deadpool: Could not request results; {e}")
                    continue
            else:
                user_input = input("\nYou: ")
                
            if user_input.lower() in ['exit', 'quit']:
                break
                
            if user_input.lower() == '/voice':
                voice_mode = not voice_mode
                print(f"Voice mode is now {'ON' if voice_mode else 'OFF'}.")
                continue
                
            if user_input.lower() == '/debug on':
                runtime.toggle_debug(True)
                print("Debug mode ON.")
                continue
                
            if user_input.lower() == '/debug off':
                runtime.toggle_debug(False)
                print("Debug mode OFF.")
                continue
                
            if not user_input.strip():
                continue
                
            response, voice_response = runtime.process_input(user_input)
            print(f"\nDeadpool: {response}")
            
            if voice_mode:
                # Remove emojis and special unicode characters that can make Windows TTS fail silently
                clean_response = voice_response.encode('ascii', 'ignore').decode('ascii')
                tts_engine.say(clean_response)
                tts_engine.runAndWait()
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nSystem Error: {e}")

if __name__ == "__main__":
    main()
