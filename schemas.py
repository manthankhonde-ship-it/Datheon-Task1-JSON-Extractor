from pydantic import BaseModel, Field
from typing import List

# to store the experience details of the candidate
class Experience(BaseModel):
    company: str = Field(description="Name of the company or organization")
    role: str = Field(description="Job title or role")
    duration: str = Field(description="Time period of employment")

# to store the final JSON schema of the resume
class ResumeSchema(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address of the candidate")
    skills: List[str] = Field(description="List of technical and soft skills")
    experience: List[Experience] = Field(description="List of work experiences, projects or internships")