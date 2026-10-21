# Datheon Task 1: Structured LLM Prompt Pipeline & JSON Extractor

## Project Overview
This project is part of the **Datheon Python + Generative AI & LangChain Internship**. 
The goal of this task is to build a robust pipeline that extracts structured data (JSON) from unstructured text (e.g., Resumes) using Large Language Models (LLMs) and strict schema validation.

## Tech Stack
* **Language:** Python 3
* **LLM API:** Google Gemini API (`google-genai` SDK, `gemini-1.5-flash`)
* **Validation:** Pydantic (Strict JSON Schema Enforcement)
* **Environment:** `python-dotenv` for secure API key management

## Key Features
1. **Parameterized Prompt Templates:** Custom instructions to guide the LLM for precise data extraction.
2. **Strict Schema Validation:** Utilizing Pydantic models to ensure the output strictly adheres to the requested JSON format (Name, Email, Skills, Experience).
3. **Robust Handling:** Graceful fallback and empty field handling if specific data points are missing from the unstructured text.

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd Task1_JSON_Extractor