# main.py
import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemas import ResumeSchema
from prompt_templates import RESUME_EXTRACTION_PROMPT


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_resume_data(text: str):
    print(" Analyzing resume and extracting structured JSON...")
    

    formatted_prompt = RESUME_EXTRACTION_PROMPT.format(text=text)
    
   
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=formatted_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ResumeSchema, 
        ),
    )
    return response.text

if __name__ == "__main__":
    
    sample_resume_text = """
    Manthan Khonde
    Email: manthan.khonde@example.com
    Skills: Python, Generative AI, LangChain, FastAPI, React, SQL
    Experience:
    - AI Engineer Intern at Datheon (Jan 2026 - Present)
    - Developed MK-Agent AI Twin using LangGraph and FAISS database.
    - Software Developer at ABC Tech (June 2025 - Dec 2025)
    """

    try:
        
        result = extract_resume_data(sample_resume_text)
        
        parsed_json = json.loads(result)
        print("\n Extraction Successful! Here is the JSON output:\n")
        print(json.dumps(parsed_json, indent=4))
        
    except Exception as e:
        print(f"\n Error occurred: {e}")