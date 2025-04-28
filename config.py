import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-testing'
    
    # OpenAI API Configuration
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    
    # DevAyo Social Links
    TWITTER_URL = os.environ.get('TWITTER_URL')
    TIKTOK_URL = os.environ.get('TIKTOK_URL')
    GITHUB_URL = os.environ.get('GITHUB_URL') 