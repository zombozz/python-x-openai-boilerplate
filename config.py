import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config_data = self._load_config()

    def _load_config(self):
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key):
        return self.config_data.get(key)

    def set(self, key, value):
        self.config_data[key] = value
        self._save_config()

    def _save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)

# Usage example:
if __name__ == "__main__":
    config = Config()
    print("Current OPENAI_API_KEY:", config.get("OPENAI_API_KEY"))
    
    config.set("OPENAI_API_KEY", "new_api_key_value")
    print("Updated OPENAI_API_KEY:", config.get("OPENAI_API_KEY"))