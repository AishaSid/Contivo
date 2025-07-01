# Contivo

Contivo is a multi-agent AI-powered video content generator designed to streamline the creation of SEO-optimized video scripts. By leveraging Google Gemini and a modular agent architecture, Contivo transforms a simple topic or keyword into a complete set of video content assets, including a catchy title, description, script, simplified voice-over script, and relevant hashtags.

---
## Features

- **Multi-Agent Pipeline:** Modular agents for topic analysis, script writing, simplification, and SEO.
- **Google Gemini Integration:** High-quality, creative content generation.
- **SEO Optimization:** Auto-generates hashtags for discoverability.
- **Voice-Over Output:** Simplified script for narration.
- **Streamlit UI:** Easy-to-use web interface.
- **Logging:** Tracks all agent activities and outputs.

---

## How It Works

1. Enter a topic in the app.
2. Agents generate a title, description, script, simplified script, and hashtags.
3. Review and export all content and logs in the app.


## Getting Started

### Prerequisites

- Python 3.8+
- [Google Gemini API key](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/contivo.git
   cd contivo
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your Google Gemini API key:**
   - Rename `.env.example` to `.env`.
   - Add your API key: `GEMINI_API_KEY='your_api_key'`.

4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

5. **Open your browser:**
   - Go to `http://localhost:8501`.

---

## Usage

- Enter a topic or keyword related to your video content.
- Review the generated title, description, and script.
- Modify the script as needed for your voice and style.
- Export the final content and hashtags for video production.

---

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/YourFeature`
6. Submit a pull request

---

## Acknowledgments

- made as an internship evaluation task.
- Powered by Google Gemini's advanced AI capabilities.
