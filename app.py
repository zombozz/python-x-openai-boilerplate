from openai_integration import setup_openai, verify_openai_key, get_reply
from config import Config
from make_logs import log_message

def main():
    config = Config()
    openai_client = setup_openai()

    if not verify_openai_key():
        log_message("Failed to verify OpenAI API key.")
        return

    ai_rules = config.get("AI-RULES")
    prompt = config.get("PROMPT")
    message_to_ai = "Tell me a joke."

    reply = get_reply(openai_client, message_to_ai, ai_rules)

    if reply:
        print(f"AI replied: {reply}")
    else:
        print("Failed to get a reply from AI.")

if __name__ == "__main__":
    main()
