from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Curriculum - Lucas Ramos Dias França", ln=True, align='C')
pdf.ln(10)

# Contact information
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Address: Belo Horizonte", ln=True)
pdf.cell(200, 10, txt="Phone: +55(31)99401-4855", ln=True)
pdf.cell(200, 10, txt="Email: lucasrfranca@hotmail.com", ln=True)
pdf.cell(200, 10, txt="GitHub: https://www.github.com/eluriomilmar", ln=True)
pdf.cell(200, 10, txt="LinkedIn: https://www.linkedin.com/in/eluriomilmar", ln=True)
pdf.ln(10)

# Profile in English
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Profile", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""I am a professional with experience in hardware systems maintenance, search engine evaluation, training algorithms for autonomous vehicles, and language models (LLMs), working independently. I am seeking a transition to software development with solid experience in Python and various personal projects, such as games (hangman, tic-tac-toe) and mathematical solutions. I am a self-taught student of Java, JavaScript, and HTML, having completed the Systems Analysis and Development course at Estácio in December 2025.
I have an analytical profile, with a focus on self-learning and fluency in English since adolescence.
I have ASD, which enhances my ability to analyze detailed and literal code.""")
pdf.ln(10)

# Education in English
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Education", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Estácio - 2023 - 2025 (Course completed in December 2025) - Systems Analysis and Development
UFMG - 2017 - 2018 - Statistics (Incomplete)
UNIBH - 2016 - Electrical Engineering (Incomplete)
UFMG - 2011 - 2013 - Physics (Incomplete)
Escola Estadual Ilacir Pereira Lima - 2010 - High School (Completed)""")
pdf.ln(10)

# Experience in English
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Experience", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""AeC - 12/2024 - 10/2025 - Call Center Agent
Remotasks/Outlier - 09/2023 - 11/2024 - AI Model Trainer
Freelancer - 12/2018 - 08/2023 - IT Technician
Appen - 01/2012 - 06/2015 - Search Engine Evaluator""")
pdf.ln(10)

# Skills in English
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Skills", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Programming Languages: Python, Java, JavaScript, HTML, CSS, Scilab
Tools and Technologies: Microsoft Office, GitHub
Web Development: HTML, CSS, JavaScript""")
pdf.ln(10)

# Languages in English
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Languages", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""Portuguese: Native
English: Fluent
Spanish: Basic""")

# Save the PDF
file_path = 'Lucas_Ramos_Dias_Franca_Curriculum_English.pdf'
pdf.output(file_path)

print(f"PDF saved as {file_path}")