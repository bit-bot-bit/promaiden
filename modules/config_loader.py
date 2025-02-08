from dotenv import load_dotenv
import json
import os

CONFIG_FILE = "config.json"

# Load environment variables from .env file
load_dotenv()

def load_config():
    """Load configuration from a JSON file."""
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)

    # Override API key with environment variable if available
    config["chatgpt_api_key"] = os.getenv("OPENAI_API_KEY", config.get("chatgpt_api_key", ""))
    return config