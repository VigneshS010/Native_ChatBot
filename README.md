
# Tamil Chatbot and Translator

A Streamlit application for translating between English and Tamil, and interacting with a chatbot powered by OpenRouter's API.

## Features
- Real-time English to Tamil translation using Hugging Face models
- Chat interface with AI chatbot using Google's Gemma-3-1b model via OpenRouter
- Two-column interface for simultaneous translation and chat

## Installation

1. Clone the repository:
```bash
git clone [repository_url]
```

2. Install dependencies:
```bash
pip install streamlit transformers openai
```

3. Set up API keys:
   - Create `.streamlit/secrets.toml` file
   - Add your OpenRouter API key:
   ```toml
   [OPENROUTER_API_KEY]
   key = "your_api_key_here"
   ```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Use the interface:
- **Left Column (Chatbot):**
  - Enter text in the "Speak with Chatbot" text area
  - Click "Answer" to get responses
  - Use "Copy to Translator" to move responses to translation panel

- **Right Column (Translator):**
  - Enter English text in the input area
  - Click "Translate" to get Tamil translation

## Requirements
- Python 3.7+
- OpenRouter API key (free tier available)
- Internet connection for model downloads

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
4. Ensure code follows PEP8 standards

## License
MIT License
