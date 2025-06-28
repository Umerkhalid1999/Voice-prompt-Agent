# 🎙️ Voice Conversational AI

A complete real-time voice conversational AI system: Speak → AI Understands → AI Responds with Voice! Uses Whisper for speech recognition, DeepSeek-R1 for intelligent responses, and Edge TTS for natural voice synthesis.

## ✨ Features

- 🎤 **Real-time Speech Recognition** - Automatically starts/stops recording when you speak
- 🔄 **Direct Memory Processing** - No file operations, processes audio directly in memory
- 🤖 **DeepSeek-R1 Integration** - Powered by state-of-the-art AI via OpenRouter
- 🔊 **Natural Voice Synthesis** - AI responds with realistic human-like speech using Edge TTS
- ⚡ **Complete Voice Conversation** - True voice-to-voice interaction with AI
- 🎯 **Smart Silence Detection** - Intelligently detects when you finish speaking
- 🎭 **Multiple Voice Options** - Choose from various realistic voices
- 🛡️ **Robust Error Handling** - Graceful handling of network and audio issues

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Microphone
- OpenRouter API key ([Get one here](https://openrouter.ai/))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Umerkhalid1999/Voice-prompt-Agent.git
   cd Voice-prompt-Agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - Copy `env_template` to `.env`
   - Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

4. **Run the system:**
   ```bash
   python STT_whisper.py
   ```

## 🎯 How It Works

1. **🎙️ Speak** - The system listens continuously for your voice
2. **📹 Auto-Record** - Starts recording automatically when speech is detected
3. **📝 Transcribe** - Whisper converts your speech to text in real-time
4. **🤖 AI Processing** - DeepSeek-R1 generates intelligent responses
5. **🔊 Voice Synthesis** - Edge TTS converts AI response to natural speech
6. **🔄 Continuous Loop** - Ready for your next voice interaction immediately

**Complete Pipeline: Your Voice → Text → AI Brain → AI Voice → Your Ears** 🎙️→📝→🧠→🔊→👂

## 🔧 Configuration

You can customize the system by modifying these settings in `STT_whisper.py`:

```python
self.silence_threshold = 500    # Microphone sensitivity
self.silence_duration = 2       # Seconds of silence before stopping
temperature = 0.7               # AI response creativity (0.0-1.0)
max_tokens = 800               # Maximum response length
```

## 📋 Dependencies

- `pyaudio` - Audio recording and playback
- `numpy` - Audio data processing  
- `openai-whisper` - Speech-to-text transcription
- `requests` - API communication
- `edge-tts` - Text-to-speech synthesis
- `pygame` - Audio playback for TTS

## 🛠️ System Requirements

- **Windows/macOS/Linux** - Cross-platform compatible
- **Microphone** - Any standard microphone device
- **Internet Connection** - Required for DeepSeek-R1 API calls
- **Python 3.7+** - Modern Python environment

## 🔧 Troubleshooting

### Common Issues

1. **"No module named 'pyaudio'"**
   ```bash
   pip install pyaudio
   ```

2. **Microphone not detected**
   - Check microphone permissions
   - Adjust `silence_threshold` value

3. **API errors**
   - Verify your OpenRouter API key in .env file
   - Make sure .env file exists and has correct format
   - Check internet connection

## 🎮 Usage Example

```
🎙️ Welcome to Voice Conversational AI!
==================================================
🎯 Voice Conversational AI Started!
🎙️ Features:
   ✅ Speech-to-Text (Whisper)
   ✅ AI Responses (DeepSeek-R1)
   ✅ Text-to-Speech (Edge TTS)
💡 Tip: Speak clearly and pause when done
⏹️  Press Ctrl+C to exit

Listening... (speak now)
🎤 Recording...
✅ Speech ended
🔄 Transcribing directly from memory...
📝 Transcribed: 'What is the weather like today?'
You: What is the weather like today?
🤖 DeepSeek thinking...
DeepSeek: I'd be happy to help you with weather information! However, I don't have access to real-time weather data...

🔊 Converting response to speech...
✅ AI response spoken

Listening... (speak now)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition
- [OpenRouter](https://openrouter.ai/) - AI model access
- [DeepSeek](https://www.deepseek.com/) - Language model

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Built with ❤️ by [Umerkhalid1999](https://github.com/Umerkhalid1999)** 