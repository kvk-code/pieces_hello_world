# Hello World with Pieces Copilot SDK

This is a simple "Hello World" application that demonstrates how to use the Pieces Copilot SDK in Python. The application creates a conversation, asks a predefined question to the language model (LLM), and prints the generated response.

## Prerequisites

- Python 3.6 or higher
- `pieces_copilot_sdk` library

## Installation

1. **Clone the repository (if applicable):**

   ```bash
   git clone https://github.com/kvk-code/pieces_hello_world.git
   cd pieces_hello_world
   ```

2. **Install the required library:**

   Ensure you have the `pieces_copilot_sdk` library installed. If not, you can install it using pip:

   ```bash
   pip install pieces_copilot_sdk
   ```

## Usage

1. **Create a Python file (e.g., `hello.py`) and add the following code:**

   ```python
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
   ```

2. **Run the application:**

   Save the code to a file, for example, `hello.py`, and run it using Python:

   ```bash
   python hello.py
   ```

   This will create a conversation, ask the predefined question, and print the response from the language model.

## Explanation

1. **Import the PiecesClient:**

   ```python
   from pieces_copilot_sdk import PiecesClient
   ```

   This imports the `PiecesClient` class from the `pieces_copilot_sdk` library.

2. **Initialize the PiecesClient:**

   ```python
   pieces_client = PiecesClient(
       config={
           'baseUrl': 'http://localhost:1000'  # Replace with your actual base URL
       }
   )
   ```

   This initializes the `PiecesClient` with the base URL of the API.

3. **Create a new conversation:**

   ```python
   conversation_response = pieces_client.create_conversation(
       props={
           "name": "Pieces For Developers",
           "firstMessage": "What are the benefits of using Pieces for Developers?"
       }
   )
   ```

   This creates a new conversation with the name "Pieces For Developers" and a first message "What are the benefits of using Pieces for Developers?".

4. **Check if the conversation was created successfully:**

   ```python
   if conversation_response:
       print("Conversation Created:", conversation_response['conversation'].id)
       print("First Message Response:", conversation_response['answer']['text'])
   ```

   If the conversation is created successfully, it prints the conversation ID and the response to the first message.

5. **Ask a predefined question to the language model (LLM):**

   ```python
   question = "What is Pieces for Developer?"
   response = pieces_client.ask_question(question)
   print("Question Response:", response)
   ```

   This sends a predefined question "What is Pieces for Developer?" to the language model and prints the response.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
