from pieces_copilot_sdk import PiecesClient

def main():
    # Initialize the PiecesClient with the base URL of the API
    pieces_client = PiecesClient(
        config={
            'baseUrl': 'http://localhost:1000'  # Replace with your actual base URL
        }
    )

    # Create a new conversation
    conversation_response = pieces_client.create_conversation(
        props={
            "name": "Pieces For Developers",
            "firstMessage": "What are the benefits of using Pieces for Developers?"
        }
    )

    # Check if the conversation was created successfully
    if conversation_response:
        print("Conversation Created:", conversation_response['conversation'].id)
        print("First Message Response:", conversation_response['answer']['text'])

        # Ask a predefined question to the language model (LLM)
        question = "What is Pieces for Developer?"
        response = pieces_client.ask_question(question)
        print("Question Response:", response)

if __name__ == "__main__":
    main()
