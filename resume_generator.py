'''import os
import google.generativeai as genai
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))

# Function to generate AI-enhanced summary
def summarize_text(text):
    if not text.strip():
        return "Please enter some text to summarize."
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(text)
    
    return response.text

# Function to generate PDF Resume
def generate_resume(data, output_path="generated_resume.pdf"):
    """Creates a well-structured PDF Resume with proper formatting & spacing."""

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    y_position = height - 50  # Start position

    def draw_text(text, x=50, font="Helvetica", size=12, bold=False, spacing=20):
        """Helper function to draw text with spacing."""
        nonlocal y_position
        c.setFont(font + "-Bold" if bold else font, size)
        c.drawString(x, y_position, text)
        y_position -= spacing  

    def draw_divider():
        """Helper function to draw a horizontal line divider."""
        nonlocal y_position
        c.line(50, y_position, width - 50, y_position)
        y_position -= 20  

    # Header (Name, Contact Details)
    draw_text(data["name"], size=16, bold=True, spacing=30)
    draw_text(f"{data['email']}  |  {data['phone']}  |  📍 {data['address']}", size=10, spacing=15)

    # Add GitHub & LinkedIn links
    if data.get("github"):
        draw_text(f"GitHub: {data['github']}", size=10, spacing=15)
    if data.get("linkedin"):
        draw_text(f"🔗 LinkedIn: {data['linkedin']}", size=10, spacing=15)

    draw_divider()  

    # Summary Section
    draw_text("Summary", size=14, bold=True, spacing=25)
    draw_text(data["summary"], spacing=25)

    draw_divider()

    # Skills Section
    draw_text(" Skills", size=14, bold=True, spacing=25)
    for skill in data["skills"]:
        draw_text(f"• {skill}", spacing=15)

    draw_divider()

    # Experience Section
    draw_text("Experience", size=14, bold=True, spacing=25)
    for exp in data["experience"]:
        draw_text(f"🔹 {exp}", spacing=15)

    draw_divider()

    # Education Section
    draw_text(" Education", size=14, bold=True, spacing=25)
    for edu in data["education"]:
        draw_text(f"📖 {edu}", spacing=15)

    c.save()
    return output_path  # Return the file path for preview'''
    
    
    
    
    
    
    
'''import os
import google.generativeai as genai
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))

# Function to generate AI-enhanced summary
def summarize_text(text):
    if not text.strip():
        return "Please enter some text to summarize."
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(text)
    
    return response.text

# Function to generate PDF Resume
def generate_resume(data, output_path="generated_resume.pdf"):
    """Creates a well-structured PDF Resume with proper formatting & spacing."""

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    y_position = height - 50  # Start position

    def draw_text(text, x=50, font="Helvetica", size=12, bold=False, spacing=20):
        """Helper function to draw text with spacing."""
        nonlocal y_position
        c.setFont(font + "-Bold" if bold else font, size)
        c.drawString(x, y_position, text)
        y_position -= spacing  

    def draw_divider():
        """Helper function to draw a horizontal line divider."""
        nonlocal y_position
        c.line(50, y_position, width - 50, y_position)
        y_position -= 20  

    # Header (Name, Contact Details)
    draw_text(data["name"], size=16, bold=True, spacing=30)
    draw_text(f"{data['email']}  |  {data['phone']}  |  {data['address']}", size=10, spacing=15)

    # Add GitHub & LinkedIn links
    if data.get("github"):
        draw_text(f"GitHub: {data['github']}", size=10, spacing=15)
    if data.get("linkedin"):
        draw_text(f"LinkedIn: {data['linkedin']}", size=10, spacing=15)

    draw_divider()  

    # Summary Section
    draw_text("Summary", size=14, bold=True, spacing=25)
    draw_text(data["summary"], spacing=25)

    draw_divider()

    # Skills Section
    draw_text("Skills", size=14, bold=True, spacing=25)
    for skill in data["skills"]:
        draw_text(f"• {skill}", spacing=15)

    draw_divider()

    # Experience Section
    draw_text("Experience", size=14, bold=True, spacing=25)
    for exp in data["experience"]:
        draw_text(f"{exp['position']} at {exp['company']}", spacing=15)
        draw_text(f"{exp['dates']} | {exp['location']}", size=10, spacing=10)
        for detail in exp["details"]:
            draw_text(f"  - {detail}", size=10, spacing=10)  # Bullet points for details
        draw_text("", spacing=10)  # Extra space between experiences

    draw_divider()

    # Education Section
    draw_text("Education", size=14, bold=True, spacing=25)
    for edu in data["education"]:
        draw_text(f"{edu['degree']} at {edu['institution']}", spacing=15)
        draw_text(f"Year: {edu['year']}", size=10, spacing=10)
        draw_text("", spacing=10)  # Extra space between education entries

    c.save()
    return output_path  '''






import os
import google.generativeai as genai
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))

# Function to generate AI-enhanced summary (Only if not already provided)
def summarize_text(text):
    if not text.strip():
        return "Please enter some text to summarize."
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(text)
    
    return response.text.strip()

# Function to generate PDF Resume
def generate_resume(data, output_path="generated_resume.pdf"):
    """Creates a well-structured PDF Resume with proper formatting & spacing."""

    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    y_position = height - 50  # Start position

    def draw_text(text, x=50, font="Helvetica", size=12, bold=False, spacing=20):
        """Helper function to draw text with spacing."""
        nonlocal y_position
        c.setFont(font + "-Bold" if bold else font, size)
        c.drawString(x, y_position, text)
        y_position -= spacing  

    def draw_divider():
        """Helper function to draw a horizontal line divider."""
        nonlocal y_position
        c.line(50, y_position, width - 50, y_position)
        y_position -= 20  

    # Header (Name, Contact Details)
    draw_text(data["name"], size=16, bold=True, spacing=30)
    draw_text(f"{data['email']}  |  {data['phone']}  |  {data['address']}", size=10, spacing=15)

    # Add GitHub & LinkedIn links if provided
    if data.get("github"):
        draw_text(f"GitHub: {data['github']}", size=10, spacing=15)
    if data.get("linkedin"):
        draw_text(f"LinkedIn: {data['linkedin']}", size=10, spacing=15)

    draw_divider()  

    # Summary Section (Ensure AI-generated summary is used only once)
    draw_text("Summary", size=14, bold=True, spacing=25)
    if data.get("summary"):
        draw_text(data["summary"], spacing=25)

    draw_divider()

    # Skills Section
    draw_text("Skills", size=14, bold=True, spacing=25)
    for skill in data["skills"]:
        draw_text(f"• {skill.strip()}", spacing=15)

    draw_divider()

    # Experience Section
    draw_text("Experience", size=14, bold=True, spacing=25)
    for exp in data["experience"]:
        draw_text(f"{exp['position']} at {exp['company']}", bold=True, spacing=15)
        draw_text(f"{exp['dates']} | {exp['location']}", size=10, spacing=10)
        for detail in exp["details"]:
            draw_text(f"  - {detail.strip()}", size=10, spacing=10)  # Bullet points for details
        draw_text("", spacing=10)  # Extra space between experiences

    draw_divider()

    # Education Section
    draw_text("Education", size=14, bold=True, spacing=25)
    for edu in data["education"]:
        draw_text(f"{edu['degree']} at {edu['institution']}", bold=True, spacing=15)
        draw_text(f"Year: {edu['year']}", size=10, spacing=10)
        draw_text("", spacing=10)  # Extra space between education entries

    c.save()
    return output_path  # Return the file path for preview


