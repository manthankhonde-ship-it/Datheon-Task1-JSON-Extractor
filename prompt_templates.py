
RESUME_EXTRACTION_PROMPT = """
You are an expert AI data extractor. Your task is to extract structured information from the provided resume text.
Carefully analyze the text and extract the candidate's name, email, skills, and work experience.
Ensure the output strictly follows the required JSON schema. 
If any specific information is missing from the text, leave it empty.

Resume Text to analyze:
{text}
"""