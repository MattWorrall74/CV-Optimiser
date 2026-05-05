from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Grab the required environment variables
CV_INPUT_FOLDER = os.getenv('CV_INPUT_FOLDER')