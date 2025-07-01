import google.generativeai as genai
import json
import os 
from dotenv import load_dotenv
# Set your Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # Replace with your API key

# Shared data between agents
shared_data = {}
logs = []

# Logging helper
def log_activity(agent, message):
    logs.append(f"Agent {agent}: {message}")
    print(f"Agent {agent}: {message}")

# Generic Gemini call
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error from Gemini: {str(e)}"

# Agent 1: Title and description
def agent_1_topic_analyzer(topic):
    log_activity(1, f"Received topic: {topic}")
    result = ask_gemini(
        f"Generate ONLY a catchy video title and a one-line description for the topic: {topic}. "
        "Respond with exactly two lines: the first line is the title, the second line is the description. Do not include any extra text."
    )
    lines = result.strip().split('\n')
    title = lines[0].strip() if len(lines) > 0 else ""
    description = lines[1].strip() if len(lines) > 1 else ""
    shared_data["title"] = title
    shared_data["description"] = description
    log_activity(1, f"Generated title: {title} and description: {description}")

# Agent 2: Script generator
def agent_2_script_builder():
    log_activity(2, "Received title and description")
    title = shared_data.get("title", "")
    description = shared_data.get("description", "")
    prompt = (
        f"Write ONLY a creative video 3-paragraph short script (max 3 paragraphs) for the title: '{title}'. "
        f"Description: {description}\n"
        "Do NOT add introductions, explanations, or any extra comments."
    )
    script = ask_gemini(prompt)
    # Ensure script is no more than 3 paragraphs
    paragraphs = [p for p in script.split('\n') if p]
    if len(paragraphs) > 3:
        script = '\n'.join(paragraphs[:3])
    shared_data["script"] = script
    log_activity(2, f"Generated script: {script}")

# Agent 3: Hashtag/SEO optimizer
def agent_3_seo_optimizer():
    log_activity(3, "Received script")
    script = shared_data.get("script", "")
    prompt = (
        "Generate ONLY 5 to 8 relevant hashtags for the following script. "
        "Respond with each hashtag on a new line, and do not include any extra text, explanations, or keywords—just the hashtags:\n\n"
        f"{script}"
    )
    hashtags_text = ask_gemini(prompt)
    hashtags = [tag.strip() for tag in hashtags_text.split('\n') if tag.strip()]
    shared_data["hashtags"] = hashtags
    log_activity(3, f"Generated hashtags: {hashtags}")

# Save logs and outputs to file
def save_logs_and_output():
    data = {
        "logs": logs,
        "output": shared_data
    }
    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def agent_4_script_simplifier():
    log_activity(4, "Received script from Agent 2")
    script = shared_data.get("script", "")
    prompt = (
        "Rewrite the following script to be highly suitable for voice-over narration. "
        "Break down complex sentences into short, clear, and easy-to-understand statements. "
        "Use simple vocabulary, a friendly and conversational tone, and ensure the flow is natural for spoken delivery. "
        "Do NOT add introductions, explanations, or any extra comments:\n\n"
        f"{script}"
    )
    simplified_script = ask_gemini(prompt)
    shared_data["simplified_script"] = simplified_script  # <-- Use a new key
    log_activity(4, f"Simplified script for voice-over: {simplified_script}")
