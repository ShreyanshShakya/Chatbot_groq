import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def coding_chatbot():
    print("Coding Chatbot is running. Type 'exit' to quit.")
    print("You can ask me to complete code, write code, or generate documentation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Provide a programming-specific context for the chatbot
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a coding assistant. You can help with code completion, "
                            "writing new code, and generating documentation. Provide clear, "
                            "concise, and accurate responses."
                        ),
                    },
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            response = chat_completion.choices[0].message.content
            print(f"Coding Chatbot: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    coding_chatbot()