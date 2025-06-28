#!/usr/bin/env python3
"""
Complete Real-time Conversational AI System
Speech → Text → AI Response → Speech
"""

import os
import sys
import time
from STT_whisper import ContinuousVoiceChat
from TTS_edge import EdgeTTSEngine


class FullConversationalAI:
    def __init__(self, api_key=None, voice="en-US-AriaNeural", speech_rate="+0%"):
        """
        Initialize the complete conversational AI system
        
        Args:
            api_key: OpenRouter API key
            voice: TTS voice to use
            speech_rate: Speech rate (e.g., "+20%" for faster)
        """
        print("🚀 Initializing Full Conversational AI System...")
        
        # Initialize Speech-to-Text engine
        print("📱 Loading Speech-to-Text engine...")
        self.stt_engine = ContinuousVoiceChat(api_key)
        
        # Initialize Text-to-Speech engine
        print("🔊 Loading Text-to-Speech engine...")
        self.tts_engine = EdgeTTSEngine(voice=voice, rate=speech_rate)
        
        # System settings
        self.enable_voice_responses = True
        self.conversation_history = []
        
        print("✅ Conversational AI System Ready!")
        print(f"🎭 Using voice: {voice}")
        print(f"⚡ Speech rate: {speech_rate}")
    
    def process_conversation_turn(self):
        """Handle one complete conversation turn: Listen → Transcribe → AI Response → Speak"""
        try:
            # 1. Listen and record speech
            print("\n🎯 === New Conversation Turn ===")
            frames = self.stt_engine.record_until_silence()
            
            if not frames:
                print("❌ No speech detected")
                return False
            
            # 2. Transcribe speech to text
            user_text = self.stt_engine.transcribe_direct(frames)
            
            if not user_text or len(user_text.strip()) <= 2:
                print("❌ No clear speech detected")
                return False
            
            # 3. Get AI response
            ai_response = self.stt_engine.ask_deepseek(user_text)
            
            if not ai_response:
                print("❌ No AI response received")
                return False
            
            # 4. Convert AI response to speech and play
            if self.enable_voice_responses:
                print("🔊 Converting response to speech...")
                success = self.tts_engine.speak(ai_response)
                if success:
                    print("✅ AI response spoken successfully")
                else:
                    print("⚠️ Speech synthesis failed, but got text response")
            
            # 5. Save conversation history
            self.conversation_history.append({
                "user": user_text,
                "ai": ai_response,
                "timestamp": time.time()
            })
            
            return True
            
        except Exception as e:
            print(f"❌ Error in conversation turn: {e}")
            return False
    
    def run_continuous_conversation(self):
        """Run the continuous conversation loop"""
        print("\n🎯 Full Conversational AI Started!")
        print("💡 Tips:")
        print("   - Speak clearly and pause when done")
        print("   - The AI will respond with both text and voice")
        print("   - Press Ctrl+C to exit")
        print("   - Say 'mute voice' to disable speech")
        print("   - Say 'enable voice' to re-enable speech")
        print("⏹️  Press Ctrl+C to exit\n")
        
        try:
            while True:
                # Handle one conversation turn
                success = self.process_conversation_turn()
                
                if success:
                    # Check for voice control commands
                    last_turn = self.conversation_history[-1]
                    user_text = last_turn["user"].lower()
                    
                    if "mute voice" in user_text or "disable voice" in user_text:
                        self.enable_voice_responses = False
                        print("🔇 Voice responses disabled")
                    elif "enable voice" in user_text or "unmute voice" in user_text:
                        self.enable_voice_responses = True
                        print("🔊 Voice responses enabled")
                
                # Brief pause before next turn
                time.sleep(0.5)
                print("\nListening... (speak now)")
        
        except KeyboardInterrupt:
            print("\n👋 Conversation ended!")
            self.show_conversation_summary()
    
    def show_conversation_summary(self):
        """Show a summary of the conversation"""
        if not self.conversation_history:
            print("No conversation history to display.")
            return
        
        print(f"\n📊 Conversation Summary ({len(self.conversation_history)} exchanges):")
        print("=" * 50)
        
        for i, turn in enumerate(self.conversation_history, 1):
            print(f"\nTurn {i}:")
            print(f"You: {turn['user']}")
            print(f"AI: {turn['ai'][:100]}{'...' if len(turn['ai']) > 100 else ''}")
        
        print("=" * 50)
    
    def change_voice(self, voice_name):
        """Change the TTS voice"""
        self.tts_engine.set_voice(voice_name)
        # Test the new voice
        self.tts_engine.speak(f"Voice changed to {voice_name}")
    
    def change_speech_rate(self, rate):
        """Change speech rate"""
        self.tts_engine.set_speed(rate)
        self.tts_engine.speak(f"Speech rate changed to {rate}")
    
    def list_voices(self):
        """List available voices"""
        return self.tts_engine.list_available_voices()
    
    def test_voice_output(self, text="Hello! This is a test of the voice output system."):
        """Test the voice output"""
        print("🧪 Testing voice output...")
        success = self.tts_engine.speak(text)
        return success


def main():
    """Main function to run the conversational AI"""
    print("🎙️ Welcome to Full Conversational AI System!")
    print("=" * 50)
    
    try:
        # Initialize the system
        ai_system = FullConversationalAI()
        
        # Test voice output first
        print("\n🧪 Testing voice output...")
        test_success = ai_system.test_voice_output("Hello! I'm your conversational AI assistant. I can now speak back to you!")
        
        if not test_success:
            print("⚠️ Voice output test failed, but continuing...")
        
        # Start the conversation
        ai_system.run_continuous_conversation()
        
    except ValueError as e:
        print(f"❌ Setup Error: {e}")
        print("\n🔧 Quick Fix Options:")
        print("1. Create a file called 'api_key.txt' in the same folder and paste your key there")
        print("2. Or set environment variable: set OPENROUTER_API_KEY=your_key")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main() 