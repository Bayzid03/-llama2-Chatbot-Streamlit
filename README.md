# LangChain Chatbot with Open Source Llama2

This project is a simple chatbot web app built with [Streamlit](https://streamlit.io/) and [LangChain](https://python.langchain.com/) using the open-source Llama2 model via [Ollama](https://ollama.com/).

## Features

- Chatbot interface powered by Llama2 (run locally with Ollama)
- Prompt templating and output parsing with LangChain
- Easy-to-use Streamlit web UI

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Llama2 model pulled in Ollama (`ollama pull llama2`)
- The following Python packages:
  - `langchain`
  - `langchain_openai`
  - `langchain_community`
  - `streamlit`
  - `python-dotenv`

## Setup

1. **Clone the repository**

   ```sh
   git clone <https://github.com/Bayzid03/-llama2-Chatbot-Streamlit.git>
   cd <>
   ```

2. **Install dependencies**

   ```sh
   pip install langchain langchain_openai langchain_community streamlit python-dotenv
   ```

3. **Set up Ollama and Llama2**

   - [Install Ollama](https://ollama.com/download)
   - Pull the Llama2 model:
     ```sh
     ollama pull llama2
     ```
   - Start the Ollama server (usually runs automatically).

4. **Create a `.env` file**

   Add your LangChain API key (if required):

   ```
   LANGCHAIN_API_KEY=your_api_key_here
   ```

   > If you are only using local models with Ollama, the API key may not be required.

5. **Run the app**

   ```sh
   streamlit run localama.py
   ```

6. **Open your browser**

   Visit [http://localhost:8501](http://localhost:8501) to use the chatbot.

## File Structure

- `localama.py` - Main Streamlit app
- `.env` - Environment variables (not included, create your own)
- `.vscode/settings.json` - VS Code settings (optional)

## Notes

- Make sure Ollama is running and the Llama2 model is available before starting the app.
- If you encounter issues, check that all dependencies are installed and environment variables are set.

## License

MIT License
