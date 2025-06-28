#!/usr/bin/env python3
"""
Text-to-Speech module using edge_TTS
Converts AI responses to natural speech
"""

import asyncio
import edge_tts
import pygame
import io
import threading
import time
from typing import Optional


class EdgeTTSEngine:
    def __init__(self, voice="en-US-AriaNeural", rate="+15%"):
        """
        Initialize TTS engine with voice settings
        
        Args:
            voice: Voice to use (default: en-US-AriaNeural - female voice)
            rate: Speech rate (e.g., "+20%" for faster, "-20%" for slower)
        """
        self.voice = voice
        self.rate = rate
        
        # Initialize pygame mixer for audio playback
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        print(f"🔊 TTS Engine initialized with voice: {voice}")
    
    async def _generate_speech_async(self, text: str) -> bytes:
        """Generate speech audio data asynchronously"""
        try:
            communicate = edge_tts.Communicate(text, self.voice, rate=self.rate)
            audio_data = b""
            
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_data += chunk["data"]
            
            return audio_data
        except Exception as e:
            print(f"❌ TTS Generation Error: {e}")
            return b""
    
    def generate_speech(self, text: str) -> Optional[bytes]:
        """Generate speech audio data (synchronous wrapper)"""
        try:
            # Run the async function in a new event loop
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            audio_data = loop.run_until_complete(self._generate_speech_async(text))
            loop.close()
            return audio_data if audio_data else None
        except Exception as e:
            print(f"❌ TTS Error: {e}")
            return None
    
    def speak(self, text: str) -> bool:
        """Convert text to speech and play it"""
        if not text or not text.strip():
            return False
        
        print(f"🔊 Speaking: '{text[:50]}{'...' if len(text) > 50 else ''}'")
        
        try:
            # Generate speech
            audio_data = self.generate_speech(text)
            if not audio_data:
                print("❌ Failed to generate speech")
                return False
            
            # Play the audio using pygame
            audio_buffer = io.BytesIO(audio_data)
            pygame.mixer.music.load(audio_buffer)
            pygame.mixer.music.play()
            
            # Wait for playback to complete
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            print("✅ Speech completed")
            return True
            
        except Exception as e:
            print(f"❌ Speech playback error: {e}")
            return False
    
    def speak_async(self, text: str):
        """Speak text in background thread (non-blocking)"""
        def _speak_thread():
            self.speak(text)
        
        thread = threading.Thread(target=_speak_thread, daemon=True)
        thread.start()
        return thread
    
    def stop_speech(self):
        """Stop current speech playback"""
        try:
            pygame.mixer.music.stop()
            print("🔇 Speech stopped")
        except Exception as e:
            print(f"⚠️ Error stopping speech: {e}")
    
    def set_voice(self, voice: str):
        """Change the TTS voice"""
        self.voice = voice
        print(f"🎭 Voice changed to: {voice}")
    
    def set_speed(self, rate: str):
        """Change speech rate (e.g., '+20%', '-10%')"""
        self.rate = rate
        print(f"⚡ Speech rate changed to: {rate}")
    
    def list_available_voices(self):
        """List some popular available voices"""
        voices = [
            "en-US-AriaNeural",      # Female, friendly
            "en-US-JennyNeural",     # Female, assistant-like
            "en-US-GuyNeural",       # Male, warm
            "en-US-DavisNeural",     # Male, confident
            "en-GB-SoniaNeural",     # Female, British
            "en-GB-RyanNeural",      # Male, British
            "en-AU-NatashaNeural",   # Female, Australian
            "en-CA-ClaraNeural"      # Female, Canadian
        ]
        
        print("🎭 Available Voices:")
        for i, voice in enumerate(voices, 1):
            print(f"  {i}. {voice}")
        
        return voices


# Test function
async def test_tts():
    """Test the TTS engine"""
    tts = EdgeTTSEngine()
    
    test_messages = [
        "Hello! I'm your AI assistant. I can now speak to you!",
        "How can I help you today?",
        "This is a test of the text to speech system."
    ]
    
    for message in test_messages:
        tts.speak(message)
        time.sleep(1)


if __name__ == "__main__":
    print("🧪 Testing Edge TTS Engine...")
    
    # Run the test
    asyncio.run(test_tts())
    
    print("✅ TTS Test completed!") 