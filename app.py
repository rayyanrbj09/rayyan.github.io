from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# ── Portfolio Data ──────────────────────────────────────────────────────────

PROFILE = {
    "name": "Mohd Rayyan",
    "full_name": "Mohd Rayyan Bin Mohd Jaweed",
    "title": "Data Scientist Intern",
    "tagline": "Building data-driven AI systems with a focus on finance, analytics, and scalable ML pipelines.",
    "email": "rayyan.rbj0409@gmail.com",
    "phone": "+91 8106931514",
    "location": "Hyderabad, India",
    "linkedin": "https://www.linkedin.com/in/mohd-rayyan-bin-mohd-jaweed",
    "github": "https://github.com/rayyanrbj09",
    "bio": (
        "Data Scientist Intern at The Ascent Group with hands-on experience in financial datasets, "
        "ETL pipelines, and backend-driven AI systems. Skilled in building scalable machine learning "
        "solutions using Python and AWS. Experienced in data preprocessing, exploratory analysis, "
        "and deploying production-ready models for real-world decision-making."
    ),
}

SKILLS = {
    "Programming & Core": ["Python", "SQL", "Jupyter Notebook"],
    "Data Analysis": ["Pandas", "Polars", "NumPy"],
    "Visualization": ["Matplotlib", "Seaborn"],
    "Statistics": ["EDA", "Feature Engineering", "Correlation Analysis", "Hypothesis Testing", "Outlier Detection"],
    "Machine Learning": ["Model Training", "Evaluation", "ML APIs"],
    "Frameworks": ["Flask", "FastAPI"],
    "Cloud & Tools": ["AWS (S3, EC2, SageMaker, Bedrock, RDS)", "Git", "GitHub"],
    "Databases": ["MySQL", "PostgreSQL"],
}
EDUCATION = [
    {
        "degree": "B.Tech in Computer Science Engineering",
        "institution": "JNTUH College of Engineering",
        "location": "Hyderabad",
        "year": "2022 – 2026 (Expected)",
    },
    {
        "degree" : "MPC (Intermediate) - 93.3 %",
        "institution": "Sri Chaitanya Junior College",
        "location" : "Hyderabad",
        "year": "2020 – 2022",
    },
    {
        "degree" : "SSC - 10 CGPA",
        "institution": "MS Future School",
        "location" : "Hyderabad",
        "year": "2019 – 2020",
    },
]

PROJECTS = [
    {
        "id": 1,
        "title": "SurgiMind — Surgical Tool Detection & AI Platform",
        "tag": "AI · Computer Vision · Healthcare",
        "color": "teal",
        "description": (
            "AI-powered surgical workflow analysis system combining medical report detection, "
            "surgical tool recognition, and procedural insights."
        ),
        "tech": ["Python", "AWS", "Computer Vision", "ML"],
        "highlights": [
            "Built ML inference endpoints for surgical predictions",
            "Designed backend database for annotations and logs",
            "Delivered production-ready healthcare AI system",
            "Supports surgical decision-making with AI insights",
        ],
    },
    {
        "id": 2,
        "title": "MoodJournal — Voice-based Emotion Recognition",
        "tag": "AI · NLP · Emotion Detection",
        "color": "purple",
        "description": (
            "Voice-based emotion recognition and mood tracking system that provides "
            "personalized suggestions and mental wellness insights."
        ),
        "tech": ["Python", "NLP", "Speech Processing", "APIs"],
        "highlights": [
            "Voice-based mood detection using speech input",
            "Backend architecture + database design",
            "Integrated Google APIs for personalized recommendations",
            "Combines emotion analytics with wellness content",
        ],
    },
]

EXPERIENCE = [
    {
        "role": "Data Scientist Intern",
        "company": "The Ascent Group",
        "period": "Jan 2026 – Present",
        "description": (
            "Working on financial datasets and backend-driven AI systems. Built ETL pipelines, "
            "performed exploratory data analysis, and developed machine learning workflows for analytics."
        ),
        "highlights": [
            "Built preprocessing pipelines for transactional financial data",
            "Performed EDA on trading and ledger datasets",
            "Worked on PnL validation and margin interest calculations",
            "Improved data pipeline accuracy and reporting efficiency",
        ],
    },
    {
        "role": "Mathematics & Applied Science Tutor",
        "company": "Independent",
        "period": "Nov 2022 – Jan 2026",
        "description": (
            "Taught mathematical reasoning and problem-solving across academic levels, "
            "strengthening students’ analytical and statistical thinking."
        ),
    },
]

CERTIFICATIONS = [
    {"name": "Complete Data Science, Machine Learning, Deep Learning, NLP", "issuer": "Udemy"},
]

# ── Routes ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        education=EDUCATION,
        projects=PROJECTS,
        experience=EXPERIENCE,
        certifications=CERTIFICATIONS,
        year=datetime.now().year,
    )

@app.route("/api/projects")
def api_projects():
    return jsonify(PROJECTS)

@app.route("/api/profile")
def api_profile():
    return jsonify(PROFILE)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host = "0.0.0.0")
