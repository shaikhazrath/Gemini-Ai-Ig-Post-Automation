import random
import google.generativeai as genai
from google.generativeai import GenerativeModel
from dotenv import load_dotenv
import os
load_dotenv()
def generate_response(input_text):

    api_key = os.environ.get('API_KEY')
    genai.configure(api_key=api_key)
    model_name = "gemini-pro"
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(input_text)
    response_text = response._result.candidates[0].content.parts[0].text



    return response_text


