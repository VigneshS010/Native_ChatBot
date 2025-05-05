TAMIL CHATBOT AND TRANSLATOR

A Streamlit application combining a chatbot powered by the Google Gemma model (via OpenRouter API) and an English-to-Tamil translation tool using a Hugging Face model. Interact with an AI chatbot and translate text between English and Tamil in real-time.

---

INSTALLATION

1. Install required Python packages:
   pip install streamlit transformers openai

2. Set up OpenRouter API access:
   - Create a free account at https://openrouter.ai
   - Generate an API key in your account settings
   - Create a .streamlit/secrets.toml file in your project directory with:
     OPENROUTER_API_KEY = "your-api-key-here"

---

USAGE

1. Start the application:
   streamlit run app.py

2. Interface components:
   - Left Column (Chatbot):
     * Enter text in "Speak with Chatbot" box
     * Click "Answer" to get AI response
     * Use "Copy to Translator" to transfer responses

   - Right Column (Translator):
     * Input English text in conversion box
     * Click "Translate" to get Tamil output

3. Example workflow:
   a. Ask chatbot: "Explain quantum physics simply"
   b. Copy response to translator
   c. View Tamil translation of the explanation

---

CONTRIBUTING

Contributions are welcome through:
1. Bug reports via GitHub Issues
2. Feature requests with detailed descriptions
3. Code contributions via pull requests:
   - Fork the repository
   - Create feature branch
   - Add tests for new functionality
   - Submit PR with clear documentation

---

LICENSE

MIT License

---

NOTES

- Chatbot requires valid OpenRouter API key in secrets.toml
- Translation model automatically downloads from Hugging Face
- Internet connection required for model access
- Rate limits may apply based on OpenRouter API usage
