import json
import os

# Initialize a knowledge base and a cache for quick access to used prompts
KNOWLEDGE_BASE_FILENAME = "knowledge_base.json"
CACHE_FILENAME = "cache.json"

# You can customize this initial knowledge base
INITIAL_KNOWLEDGE_BASE = {
    "Hello": "Hi there!",
    "What is your name?": "I am Nexil, a model created by Chandler Paulk",
    # Add more initial knowledge here
}

# Find the knowledge base in the current directory and read data to store for use in application
def load_knowledge_base():
    if os.path.exists(KNOWLEDGE_BASE_FILENAME):
        with open(KNOWLEDGE_BASE_FILENAME, "r") as f:
            return json.load(f)
    else:
        return INITIAL_KNOWLEDGE_BASE.copy()

# For when new knowledge is learned, store new knowledge into knowledge_base.json
def save_knowledge_base(knowledge_base):
    with open(KNOWLEDGE_BASE_FILENAME, "w") as f:
        json.dump(knowledge_base, f)

# Load current cache into the application
def load_cache():
    if os.path.exists(CACHE_FILENAME):
        with open(CACHE_FILENAME, "r") as f:
            return json.load(f)
    else:
        return {}

# When new prompt is learned, store prompt in cache for quick access by the user
def save_cache(cache):
    with open(CACHE_FILENAME, "w") as f:
        json.dump(cache, f)

# Combine all the methods necessary to create a new prompt for the computer to store
def create_new_learning_prompt(knowledge_base, cache):
    prompt = input("Create new learning prompt: ")
    response = input("Response you'd like to have the Computer output: ")
    knowledge_base[prompt] = response
    cache[prompt] = response
    save_knowledge_base(knowledge_base)
    save_cache(cache)

# Combine all the methods necessary to have computer respond to prompt
def test_prompts(knowledge_base, cache):
    while True:
        test_prompt = input("Enter a prompt to test or type 'exit' to exit: ")
        if test_prompt.lower() == "exit":
            break
        response = cache.get(test_prompt) or knowledge_base.get(test_prompt, "I don't know how to respond to that.")
        print("Computer response:", response)

# Main application 
def main():
    knowledge_base = load_knowledge_base()
    cache = load_cache()

    while True:
        action = input("Enter 'train' to train, 'test' to test, or 'exit' to exit: ").lower()
        if action == "train":
            create_new_learning_prompt(knowledge_base, cache)
        elif action == "test":
            test_prompts(knowledge_base, cache)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please enter 'train', 'test', or 'exit'.")

if __name__ == "__main__":
    main()