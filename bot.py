import json
import random

with open('college.json', 'r') as file:
    data = json.load(file)['intents']

def search_word(search):
    for item in data:
        for pattern in item['patterns']:
            if search.lower() == pattern.lower():
                return random.choice(item['responses'])

def main():
    print("Welcome! Type 'quit' to exit.")
    while True:
        user = input("You: ")
        if user.lower() == 'quit':
            print("Bot: Goodbye!")
            break
        else:
            query = user.lower()
            sw = search_word(query)
            if sw:
                print(sw)
            else:
                print("Bot: I'm sorry, I don't understand that.") 

if __name__ == "__main__":
    main()
