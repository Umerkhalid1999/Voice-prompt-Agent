# 🎙️ Voice Prompt Agent

A real-time conversational AI system that converts speech to text using Whisper and gets intelligent responses from DeepSeek-R1 via OpenRouter.

## ✨ Features

- 🎤 **Real-time Speech Detection** - Automatically starts/stops recording when you speak
- 🔄 **Direct Memory Processing** - No file operations, processes audio directly in memory
- 🤖 **DeepSeek-R1 Integration** - Powered by state-of-the-art AI via OpenRouter
- ⚡ **Continuous Conversation** - Seamless back-and-forth dialogue
- 🎯 **Smart Silence Detection** - Intelligently detects when you finish speaking
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
   - Copy `api_key.txt.template` to `api_key.txt`
   - Add your OpenRouter API key to the file
   
   **Or use environment variable:**
   ```bash
   set OPENROUTER_API_KEY=your_api_key_here
   ```

4. **Run the system:**
   ```bash
   python STT_whisper.py
   ```

## 🎯 How It Works

1. **Speak** - The system listens continuously for your voice
2. **Auto-Record** - Starts recording automatically when speech is detected
3. **Transcribe** - Whisper converts your speech to text in real-time
4. **AI Response** - DeepSeek-R1 provides intelligent responses
5. **Continuous Loop** - Ready for your next question immediately

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
   - Verify your OpenRouter API key
   - Check internet connection

## 🎮 Usage Example

```
🎯 Continuous Voice Chat Started!
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