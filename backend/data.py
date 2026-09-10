# data.py - All fake data for prototype

# ==================== USERS ====================
users = {
    "student1": {
        "id": 1,
        "username": "student1",
        "password": "pass123",
        "name": "Rahul Kumar",
        "role": "student",
        "email": "rahul@student.com",
        "skills": ["Python", "Java", "HTML", "CSS"],
        "soft_skills": {"communication": "Good", "teamwork": "Excellent", "problem_solving": "Good"},
        "career_interest": "Software Development",
        "certifications": ["Python for Data Science", "Web Development Basics"],
        "applications": []
    },
    "company1": {
        "id": 2,
        "username": "company1",
        "password": "pass123",
        "name": "Google India",
        "role": "company",
        "email": "hr@google.com",
        "posted_jobs": [101, 102]
    },
    "faculty1": {
        "id": 3,
        "username": "faculty1",
        "password": "pass123",
        "name": "Dr. Sharma",
        "role": "faculty",
        "email": "sharma@college.edu",
        "department": "Computer Science"
    },
    "admin1": {
        "id": 4,
        "username": "admin1",
        "password": "pass123",
        "name": "IIT Delhi",
        "role": "admin",
        "email": "admin@iitd.ac.in"
    }
}

# ==================== SKILLS DATABASE ====================
# Industry-required skills for different job roles
job_roles = {
    "Software Developer": ["Python", "React", "Docker", "Git", "SQL"],
    "Data Scientist": ["Python", "AI/ML", "Statistics", "SQL", "Pandas"],
    "Frontend Developer": ["React", "HTML", "CSS", "JavaScript", "Git"],
    "Backend Developer": ["Python", "Django", "PostgreSQL", "Docker", "AWS"],
    "Cloud Engineer": ["AWS", "Docker", "Kubernetes", "Linux", "Python"],
    "Full Stack Developer": ["React", "Node.js", "MongoDB", "Git", "AWS"]
}

# All possible skills (master list - for standardization)
all_skills = [
    "Python", "Java", "JavaScript", "HTML", "CSS", "React", "Angular", "Vue",
    "Node.js", "Django", "Flask", "AI/ML", "Statistics", "Pandas", "NumPy",
    "SQL", "PostgreSQL", "MongoDB", "Firebase", "AWS", "Azure", "GCP",
    "Docker", "Kubernetes", "Linux", "Git", "C++", "C#", "PHP"
]

# ==================== JOBS ====================
jobs = [
    {
        "id": 101,
        "title": "Software Developer",
        "company": "Google India",
        "type": "Full-Time",
        "required_skills": ["Python", "React", "Docker"],
        "experience": "Fresher",
        "location": "Bangalore",
        "salary": "12-18 LPA",
        "description": "Build scalable web applications"
    },
    {
        "id": 102,
        "title": "Data Scientist",
        "company": "Google India",
        "type": "Full-Time",
        "required_skills": ["Python", "AI/ML", "Statistics"],
        "experience": "Fresher",
        "location": "Hyderabad",
        "salary": "15-20 LPA",
        "description": "Work on ML models for healthcare"
    },
    {
        "id": 103,
        "title": "Frontend Developer Intern",
        "company": "Microsoft",
        "type": "Internship",
        "required_skills": ["React", "HTML", "CSS", "JavaScript"],
        "experience": "Fresher",
        "location": "Remote",
        "salary": "40,000/month",
        "description": "6-month internship with PPO opportunity"
    },
    {
        "id": 104,
        "title": "Backend Developer",
        "company": "Amazon",
        "type": "Full-Time",
        "required_skills": ["Python", "Django", "AWS", "PostgreSQL"],
        "experience": "0-1 years",
        "location": "Chennai",
        "salary": "14-20 LPA",
        "description": "Build microservices for e-commerce platform"
    },
    {
        "id": 105,
        "title": "Cloud Engineer",
        "company": "TCS",
        "type": "Full-Time",
        "required_skills": ["AWS", "Docker", "Linux"],
        "experience": "Fresher",
        "location": "Pune",
        "salary": "6-9 LPA",
        "description": "Manage cloud infrastructure"
    }
]

# ==================== FACULTY PROGRAMS ====================
faculty_programs = [
    {
        "id": 201,
        "name": "AI for Healthcare",
        "type": "FDP",
        "duration": "3 months",
        "organized_by": "IIT Bombay",
        "mode": "Online",
        "fee": "Free",
        "description": "Learn AI applications in healthcare domain"
    },
    {
        "id": 202,
        "name": "Industry 4.0 Workshop",
        "type": "Workshop",
        "duration": "2 weeks",
        "organized_by": "NASSCOM",
        "mode": "Hybrid",
        "fee": "₹5,000",
        "description": "Hands-on workshop on Industry 4.0 technologies"
    },
    {
        "id": 203,
        "name": "Research Collaboration - Pharma AI",
        "type": "Research",
        "duration": "1 year",
        "organized_by": "Cipla + IIT Delhi",
        "mode": "On-site",
        "fee": "Funded",
        "description": "Joint research on AI in drug discovery"
    },
    {
        "id": 204,
        "name": "Faculty Internship - Data Science",
        "type": "Internship",
        "duration": "6 weeks",
        "organized_by": "Flipkart",
        "mode": "On-site (Bangalore)",
        "fee": "Stipend Provided",
        "description": "Work with Flipkart's data science team"
    },
    {
        "id": 205,
        "name": "Python for Teaching",
        "type": "Certification",
        "duration": "4 weeks",
        "organized_by": "Coursera",
        "mode": "Online",
        "fee": "Free",
        "description": "Certification course for teaching Python"
    }
]

# ==================== CANDIDATES (for company view) ====================
candidates = [
    {
        "id": 1,
        "name": "Rahul Kumar",
        "skills": ["Python", "Java", "HTML", "CSS"],
        "education": "B.Tech CSE, IIT Delhi",
        "cgpa": 8.5,
        "certifications": ["Python for Data Science"],
        "projects": ["E-Commerce Website", "Chat Application"]
    },
    {
        "id": 2,
        "name": "Priya Singh",
        "skills": ["Python", "AI/ML", "Statistics", "Pandas", "SQL"],
        "education": "B.Tech CSE, NIT Trichy",
        "cgpa": 9.1,
        "certifications": ["Machine Learning by Andrew Ng", "Deep Learning Specialization"],
        "projects": ["Image Classification", "Stock Prediction Model"]
    },
    {
        "id": 3,
        "name": "Amit Patel",
        "skills": ["React", "Node.js", "MongoDB", "AWS", "Git"],
        "education": "B.Tech IT, BITS Pilani",
        "cgpa": 8.8,
        "certifications": ["AWS Cloud Practitioner", "Full Stack Development"],
        "projects": ["Social Media App", "Task Manager"]
    },
    {
        "id": 4,
        "name": "Sneha Reddy",
        "skills": ["Python", "Django", "PostgreSQL", "Docker", "AWS"],
        "education": "B.Tech CSE, IIIT Hyderabad",
        "cgpa": 8.9,
        "certifications": ["Docker Certified", "Backend Development"],
        "projects": ["Hospital Management System", "REST API for E-learning"]
    },
    {
        "id": 5,
        "name": "Vikram Joshi",
        "skills": ["AWS", "Docker", "Kubernetes", "Linux", "Python"],
        "education": "B.Tech CSE, VIT Vellore",
        "cgpa": 8.2,
        "certifications": ["AWS Solutions Architect", "Kubernetes Administrator"],
        "projects": ["CI/CD Pipeline", "Cloud Migration Project"]
    }
]

# ==================== ANALYTICS DATA ====================
analytics = {
    "total_students": 1250,
    "total_companies": 85,
    "total_jobs_posted": 320,
    "total_applications": 4500,
    "total_hired": 180,
    "placement_rate": "42%",
    "avg_package": "8.5 LPA",
    "top_skills_demand": [
        {"skill": "Python", "demand": 95},
        {"skill": "React", "demand": 78},
        {"skill": "AI/ML", "demand": 72},
        {"skill": "AWS", "demand": 68},
        {"skill": "Docker", "demand": 55}
    ],
    "placement_trend": [
        {"month": "Jan", "placed": 25},
        {"month": "Feb", "placed": 32},
        {"month": "Mar", "placed": 45},
        {"month": "Apr", "placed": 38},
        {"month": "May", "placed": 28},
        {"month": "Jun", "placed": 12}
    ],
    "skill_gap_summary": {
        "most_missing_skills": ["AI/ML", "Docker", "AWS", "React"],
        "most_available_skills": ["Python", "Java", "HTML", "CSS"]
    }
}

# ==================== SKILL ONTOLOGY (for standardization) ====================
# Maps different names to one standard name
skill_mapping = {
    "python": "Python",
    "py": "Python",
    "python3": "Python",
    "python programming": "Python",
    "js": "JavaScript",
    "javascript": "JavaScript",
    "reactjs": "React",
    "react.js": "React",
    "react js": "React",
    "ml": "AI/ML",
    "machine learning": "AI/ML",
    "artificial intelligence": "AI/ML",
    "ai": "AI/ML",
    "aws": "AWS",
    "amazon web services": "AWS",
    "docker": "Docker",
    "containerization": "Docker"
}

def standardize_skill(skill):
    """Convert any skill name to standard format"""
    skill_lower = skill.lower().strip()
    return skill_mapping.get(skill_lower, skill.strip().title())