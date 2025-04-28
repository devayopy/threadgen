import os
import sys
from dotenv import load_dotenv
import openai

def test_openai_key():
    """Test if the OpenAI API key is valid and working."""
    print("Testing OpenAI API key...")
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the API key from environment
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        print("ERROR: No OpenAI API key found in .env file.")
        print("Please add your OpenAI API key to the .env file:")
        print("OPENAI_API_KEY=your_api_key_here")
        return False
    
    if api_key == "your_openai_api_key_here":
        print("ERROR: You're using the placeholder API key.")
        print("Please replace 'your_openai_api_key_here' with your actual OpenAI API key in the .env file.")
        return False
    
    # Set up the OpenAI client with the API key
    openai.api_key = api_key
    
    try:
        # Make a simple API call to test the key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, this is a test message."}
            ],
            max_tokens=10
        )
        
        # If we get here, the API key is working
        print("SUCCESS: OpenAI API key is valid and working!")
        print(f"Response from OpenAI: {response.choices[0].message['content']}")
        return True
        
    except Exception as e:
        print(f"ERROR: Failed to connect to OpenAI API.")
        print(f"Error details: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_openai_key()
    if not success:
        sys.exit(1) 