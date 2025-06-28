#!/usr/bin/env python3
"""
Continuous Speech-to-Text system using Whisper and DeepSeek-R1
Automatically detects when you start and stop speaking
"""

import os
import pyaudio
import numpy as np
import whisper
import requests
import threading
import time


class ContinuousVoiceChat:
    def __init__(self, api_key=None):
        # Try multiple ways to get the API key
        self.api_key = "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" or os.getenv('OPENROUTER_API_KEY') or os.getenv('OPENROUTER_API_KEY'.lower())

        # If still no key, try to read from a config file
        if not self.api_key and os.path.exists('api_key.txt'):
            try:
                with open('api_key.txt', 'r') as f:
                    self.api_key = f.read().strip()
            except:
                pass

        if not self.api_key:
            raise ValueError("API key not found. Try one of these methods:\n"
                             "1. Pass it directly: ContinuousVoiceChat('your_key')\n"
                             "2. Create api_key.txt file with your key\n"
                             "3. Set environment variable (Windows): set OPENROUTER_API_KEY=your_key")

        # Audio settings
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.silence_threshold = 500  # Adjust based on your mic
        self.silence_duration = 2  # Stop recording after 2 seconds of silence

        # Load Whisper
        print("Loading Whisper...")
        self.whisper_model = whisper.load_model("base")
        print("Ready! Start speaking...")

        self.audio = pyaudio.PyAudio()
        self.is_listening = True

    def detect_speech(self, data):
        """Simple speech detection based on audio level"""
        audio_data = np.frombuffer(data, dtype=np.int16)
        return np.abs(audio_data).mean() > self.silence_threshold

    def record_until_silence(self):
        """Record audio until silence is detected"""
        stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )

        frames = []
        silent_chunks = 0
        recording = False

        print("Listening... (speak now)")

        while self.is_listening:
            data = stream.read(self.chunk)

            if self.detect_speech(data):
                if not recording:
                    print("🎤 Recording...")
                    recording = True
                frames.append(data)
                silent_chunks = 0
            else:
                if recording:
                    silent_chunks += 1
                    frames.append(data)

                    # Stop if silent for too long
                    if silent_chunks > (self.silence_duration * self.rate / self.chunk):
                        print("✅ Speech ended")
                        break

        stream.stop_stream()
        stream.close()

        return frames if frames else None

    def transcribe_direct(self, frames):
        """Transcribe audio directly from memory without file operations"""
        if not frames:
            return None

        try:
            print("🔄 Transcribing directly from memory...")
            
            # Convert audio frames to numpy array
            audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
            
            # Convert to float32 and normalize (Whisper expects float32 between -1 and 1)
            audio_float = audio_data.astype(np.float32) / 32768.0
            
            # Transcribe directly from memory
            result = self.whisper_model.transcribe(audio_float)
            text = result["text"].strip()
            
            print(f"📝 Transcribed: '{text}'")
            return text if text else None

        except Exception as e:
            print(f"⚠️ Transcription error: {e}")
            return None

    def ask_deepseek(self, text):
        """Send text to DeepSeek and get response"""
        print(f"You: {text}")
        print("🤖 DeepSeek thinking...")

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek/deepseek-r1:free",
                    "messages": [{"role": "user", "content": text}],
                    "temperature": 0.7,
                    "max_tokens": 800
                },
                timeout=30  # Add timeout to prevent hanging
            )

            if response.status_code == 200:
                ai_response = response.json()["choices"][0]["message"]["content"]
                print(f"DeepSeek: {ai_response}\n")
                return ai_response
            elif response.status_code == 401:
                print("❌ API Error: Invalid API key")
                return None
            elif response.status_code == 429:
                print("⏳ API Error: Rate limit exceeded. Try again in a moment.")
                return None
            else:
                print(f"❌ API Error: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.Timeout:
            print("⏰ Request timed out. Try again.")
            return None
        except requests.exceptions.ConnectionError:
            print("🌐 Connection error. Check your internet connection.")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None

    def run(self):
        """Main continuous loop"""
        print("🎯 Continuous Voice Chat Started!")
        print("💡 Tip: Speak clearly and pause when done")
        print("⏹️  Press Ctrl+C to exit\n")

        try:
            while True:
                # Record speech
                frames = self.record_until_silence()

                if frames:
                    # Transcribe directly from memory
                    text = self.transcribe_direct(frames)

                    if text and len(text.strip()) > 2:
                        # Get AI response
                        self.ask_deepseek(text)
                    else:
                        print("❌ No clear speech detected\n")
                else:
                    print("❌ No speech detected\n")

                # Brief pause before listening again
                time.sleep(0.5)
                print("Listening... (speak now)")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            self.is_listening = False

    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'audio'):
            self.audio.terminate()


# Simple usage
if __name__ == "__main__":
    try:
        # Try these methods in order:
        # Method 1: Direct API key (uncomment and add your key)
        # chat = ContinuousVoiceChat("your_api_key_here")

        # Method 2: Environment variable or config file
        chat = ContinuousVoiceChat()
        chat.run()

    except ValueError as e:
        print(f"❌ Setup Error: {e}")
        print("\n🔧 Quick Fix Options:")
        print("1. Create a file called 'api_key.txt' in the same folder and paste your key there")
        print("2. Or edit the script and put your key directly in line 149")
        print("3. Or use Windows command: set OPENROUTER_API_KEY=your_key && python STT_whisper.py")
    except Exception as e:
        print(f"❌ Error: {e}")