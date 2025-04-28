import openai
from flask import current_app
import json

def generate_thread(content):
    """
    Generate a Twitter/X thread from raw content using OpenAI API
    
    Args:
        content (str): Raw user content (bullets, notes, etc.)
        
    Returns:
        list: A list of tweets forming the thread
    """
    openai.api_key = current_app.config.get('OPENAI_API_KEY')
    
    # If API key is not set, return a mock response for development
    if not openai.api_key:
        return _generate_mock_thread(content)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are an expert Twitter/X thread writer. 
                Your job is to transform raw thoughts into an engaging, informative thread.
                Follow these rules:
                1. Break content into 280 character tweets (max 10 tweets)
                2. Keep the voice natural but polished
                3. Add engagement hooks and questions
                4. Make the first tweet catchy to drive interest
                5. End with a call-to-action
                
                Format your response as a JSON array of strings, where each string is one tweet.
                """}, 
                {"role": "user", "content": content}
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        
        # Extract the thread from the response
        thread_text = response.choices[0].message['content']
        
        # Try to parse as JSON if it's properly formatted
        try:
            thread = json.loads(thread_text)
            if isinstance(thread, list):
                return thread
            else:
                # Handle case where JSON is not a list
                return thread_text.split('\n\n')
        except:
            # If not valid JSON, split by double newlines as a fallback
            return thread_text.split('\n\n')
            
    except Exception as e:
        # Log the error and fall back to mock data
        print(f"Error calling OpenAI API: {e}")
        return _generate_mock_thread(content)

def _generate_mock_thread(content):
    """Generate a mock thread for development/testing purposes"""
    # Simple logic to split content into chunks
    words = content.split()
    
    # Create 3-5 mock tweets
    tweets = []
    tweet_length = min(10, max(3, len(words) // 20))  # Try to make 3-5 tweets
    
    for i in range(0, len(words), tweet_length):
        chunk = words[i:i+tweet_length]
        if chunk:
            tweets.append(' '.join(chunk))
        if len(tweets) >= 5:  # Cap at 5 tweets for mock data
            break
    
    # Add numbering and a mock hook to the first tweet
    if tweets:
        tweets[0] = "🧵 " + tweets[0]
        
    # Add a call to action at the end
    if tweets:
        tweets[-1] = tweets[-1] + "\n\nLike and retweet if this was helpful! 🙏"
        
    return tweets 