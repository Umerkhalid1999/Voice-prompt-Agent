#!/usr/bin/env python3
"""
Complete Real-time Voice Conversational AI System
Speech → Text → AI Response → Voice Speech
"""

import os
import sys
import time
from STT_whisper import ContinuousVoiceChat
from TTS_edge import EdgeTTSEngine


class VoiceConversationalAI:
    def __init__(self, api_key=None, voice="en-US-AriaNeural", speech_rate="+0%"):
        """
        Initialize the complete voice conversational AI system
        
        Args:
            api_key: OpenRouter API key
            voice: TTS voice to use
            speech_rate: Speech rate (e.g., "+20%" for faster)
        """
        print("🚀 Initializing Voice Conversational AI System...")
        
        # Initialize Speech-to-Text engine
        print("📱 Loading Speech-to-Text engine...")
        self.stt_engine = ContinuousVoiceChat(api_key)
        
        # Initialize Text-to-Speech engine
        print("🔊 Loading Text-to-Speech engine...")
        self.tts_engine = EdgeTTSEngine(voice=voice, rate=speech_rate)
        
        # System settings
        self.enable_voice_responses = True
        self.conversation_history = []
        
        print("✅ Voice Conversational AI System Ready!")
        print(f"🎭 Using voice: {voice}")
        print(f"⚡ Speech rate: {speech_rate}")
    
    def handle_conversation_turn(self):
        """Handle one complete conversation turn: Listen → Transcribe → AI Response → Speak"""
        try:
            # 1. Listen and record speech
            print("\n🎯 === Voice Conversation Turn ===")
            frames = self.stt_engine.record_until_silence()
            
            if not frames:
                print("❌ No speech detected")
                return False
            
            # 2. Transcribe speech to text
            user_text = self.stt_engine.transcribe_direct(frames)
            
            if not user_text or len(user_text.strip()) <= 2:
                print("❌ No clear speech detected")
                return False
            
            # 3. Get AI response from DeepSeek
            ai_response = self.stt_engine.ask_deepseek(user_text)
            
            if not ai_response:
                print("❌ No AI response received")
                return False
            
            # 4. Convert AI response to speech and play it
            if self.enable_voice_responses:
                print("🔊 Converting AI response to speech...")
                success = self.tts_engine.speak(ai_response)
                if success:
                    print("✅ AI spoke the response successfully")
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
    
    def run_voice_conversation(self):
        """Run the continuous voice conversation loop"""
        print("\n🎯 Voice Conversational AI Started!")
        print("💡 How it works:")
        print("   - Speak your question/message")
        print("   - AI will respond with both text and voice")
        print("   - Wait for the AI to finish speaking before your next turn")
        print("   - Say 'mute voice' to disable AI speech")
        print("   - Say 'enable voice' to re-enable AI speech")
        print("⏹️  Press Ctrl+C to exit\n")
        
        try:
            # Initial greeting
            if self.enable_voice_responses:
                greeting = "Hello! I'm your voice conversational AI assistant. I can hear you and speak back to you. What would you like to talk about?"
                print("🤖 AI:", greeting)
                self.tts_engine.speak(greeting)
            
            while True:
                print("\nListening... (speak now)")
                
                # Handle one conversation turn
                success = self.handle_conversation_turn()
                
                if success:
                    # Check for voice control commands
                    last_turn = self.conversation_history[-1]
                    user_text = last_turn["user"].lower()
                    
                    if "mute voice" in user_text or "disable voice" in user_text:
                        self.enable_voice_responses = False
                        print("🔇 Voice responses disabled - AI will only respond with text")
                    elif "enable voice" in user_text or "unmute voice" in user_text:
                        self.enable_voice_responses = True
                        print("🔊 Voice responses enabled - AI will speak responses")
                        self.tts_engine.speak("Voice responses are now enabled again.")
                
                # Brief pause before next turn
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n👋 Voice conversation ended!")
            
            # Farewell message
            if self.enable_voice_responses:
                farewell = "Goodbye! It was nice talking with you."
                print("🤖 AI:", farewell)
                self.tts_engine.speak(farewell)
            
            self.show_conversation_summary()
    
    def show_conversation_summary(self):
        """Show a summary of the conversation"""
        if not self.conversation_history:
            print("No conversation history to display.")
            return
        
        print(f"\n📊 Conversation Summary ({len(self.conversation_history)} exchanges):")
        print("=" * 60)
        
        for i, turn in enumerate(self.conversation_history, 1):
            print(f"\nTurn {i}:")
            print(f"🎙️ You: {turn['user']}")
            print(f"🤖 AI: {turn['ai'][:100]}{'...' if len(turn['ai']) > 100 else ''}")
        
        print("=" * 60)
        print(f"Total conversation time: {len(self.conversation_history)} turns")
    
    def change_voice(self, voice_name):
        """Change the TTS voice"""
        self.tts_engine.set_voice(voice_name)
        # Test the new voice
        self.tts_engine.speak(f"Voice changed to {voice_name}. How do I sound now?")
    
    def change_speech_rate(self, rate):
        """Change speech rate"""
        self.tts_engine.set_speed(rate)
        self.tts_engine.speak(f"Speech rate changed. I'm now speaking at {rate} speed.")
    
    def list_available_voices(self):
        """List available voices"""
        return self.tts_engine.list_available_voices()
    
    def test_voice_system(self):
        """Test the complete voice system"""
        print("🧪 Testing complete voice system...")
        
        # Test TTS
        test_message = "Hello! This is a test of the complete voice conversational AI system. I can hear you and speak back to you!"
        print("🔊 Testing Text-to-Speech...")
        tts_success = self.tts_engine.speak(test_message)
        
        if tts_success:
            print("✅ Voice system test successful!")
            return True
        else:
            print("❌ Voice system test failed")
            return False


def main():
    """Main function to run the voice conversational AI"""
    print("🎙️ Welcome to Voice Conversational AI System!")
    print("=" * 60)
    print("🚀 Features:")
    print("   ✅ Real-time speech recognition")
    print("   ✅ AI-powered responses via DeepSeek-R1")
    print("   ✅ Natural voice synthesis")
    print("   ✅ Continuous voice conversation")
    print("=" * 60)
    
    try:
        # Initialize the system
        ai_system = VoiceConversationalAI()
        
        # Test the voice system first
        print("\n🧪 Testing voice system...")
        test_success = ai_system.test_voice_system()
        
        if not test_success:
            print("⚠️ Voice test failed, but continuing with text-only responses...")
            ai_system.enable_voice_responses = False
        
        # Start the voice conversation
        ai_system.run_voice_conversation()
        
    except ValueError as e:
        print(f"❌ Setup Error: {e}")
        print("\n🔧 Quick Fix Options:")
        print("1. Create 'api_key.txt' file with your OpenRouter API key")
        print("2. Or set environment variable: set OPENROUTER_API_KEY=your_key")
        print("3. Make sure you have installed all dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure all dependencies are installed: pip install -r requirements.txt")


if __name__ == "__main__":
    main() 