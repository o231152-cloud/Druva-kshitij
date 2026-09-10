# app.py - Main Flask Backend for Ayush-Setu
from flask import Flask, request, jsonify
from flask_cors import CORS
import data

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# ==================== HOME ROUTE ====================
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Ayush-Setu API",
        "version": "1.0",
        "status": "running",
        "endpoints": [
            "POST /api/login",
            "POST /api/assessment",
            "GET /api/jobs",
            "POST /api/post-job",
            "GET /api/candidates",
            "GET /api/faculty-programs",
            "GET /api/analytics"
        ]
    })

# ==================== 1. LOGIN API ====================
@app.route('/api/login', methods=['POST'])
def login():
    """Login for any role - student, company, faculty, admin"""
    try:
        req = request.json
        username = req.get('username')
        password = req.get('password')
        
        if username in data.users:
            user = data.users[username]
            if user['password'] == password:
                # Don't send password back
                user_data = {k: v for k, v in user.items() if k != 'password'}
                return jsonify({
                    "success": True,
                    "message": f"Welcome {user['name']}!",
                    "user": user_data
                })
            else:
                return jsonify({"success": False, "message": "Wrong password"}), 401
        else:
            return jsonify({"success": False, "message": "User not found"}), 404
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==================== 2. SKILL ASSESSMENT API ====================
@app.route('/api/assessment', methods=['POST'])
def assessment():
    """
    Takes student skills, compares with industry needs,
    returns skill gap analysis + job recommendations
    """
    try:
        req = request.json
        student_skills = req.get('skills', [])
        career_interest = req.get('career_interest', 'Software Developer')
        
        # Standardize skills (data cleaning)
        student_skills = [data.standardize_skill(s) for s in student_skills]
        
        # Get required skills for the career
        required = data.job_roles.get(career_interest, data.job_roles["Software Developer"])
        
        # Find missing skills
        missing_skills = [s for s in required if s not in student_skills]
        
        # Find matching skills
        matching_skills = [s for s in required if s in student_skills]
        
        # Calculate match score
        if len(required) > 0:
            match_score = round((len(matching_skills) / len(required)) * 100)
        else:
            match_score = 0
        
        # Generate job recommendations
        recommendations = []
        for job in data.jobs:
            job_skills = job['required_skills']
            matched = len(set(student_skills) & set(job_skills))
            if matched > 0:
                job_match = round((matched / len(job_skills)) * 100)
                recommendations.append({
                    "job_id": job['id'],
                    "title": job['title'],
                    "company": job['company'],
                    "type": job['type'],
                    "location": job['location'],
                    "salary": job['salary'],
                    "match_percentage": job_match,
                    "missing_skills": [s for s in job_skills if s not in student_skills]
                })
        
        # Sort by match percentage
        recommendations.sort(key=lambda x: x['match_percentage'], reverse=True)
        
        # Learning recommendations
        learning_path = []
        for skill in missing_skills:
            learning_path.append({
                "skill": skill,
                "course": f"Complete {skill} Bootcamp",
                "duration": "40 hours",
                "provider": "Coursera/Udemy"
            })
        
        return jsonify({
            "success": True,
            "student_skills": student_skills,
            "career_interest": career_interest,
            "required_skills": required,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
            "match_score": match_score,
            "job_recommendations": recommendations,
            "learning_path": learning_path,
            "analysis": {
                "technical_score": match_score,
                "soft_skills_score": 78,
                "overall_readiness": "Needs Improvement" if match_score < 60 else "Good"
            }
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==================== 3. GET ALL JOBS ====================
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """Get all jobs (with optional filter by type)"""
    job_type = request.args.get('type')
    
    if job_type:
        filtered = [j for j in data.jobs if j['type'].lower() == job_type.lower()]
        return jsonify({"success": True, "count": len(filtered), "jobs": filtered})
    
    return jsonify({"success": True, "count": len(data.jobs), "jobs": data.jobs})

# ==================== 4. POST A JOB (Company) ====================
@app.route('/api/post-job', methods=['POST'])
def post_job():
    """Company posts a new job"""
    try:
        req = request.json
        
        new_job = {
            "id": 100 + len(data.jobs) + 1,
            "title": req.get('title'),
            "company": req.get('company', 'Unknown Company'),
            "type": req.get('type', 'Full-Time'),
            "required_skills": req.get('skills', []),
            "experience": req.get('experience', 'Fresher'),
            "location": req.get('location', 'Remote'),
            "salary": req.get('salary', 'Not Disclosed'),
            "description": req.get('description', '')
        }
        
        data.jobs.append(new_job)
        
        return jsonify({
            "success": True,
            "message": f"Job '{new_job['title']}' posted successfully!",
            "job": new_job,
            "total_jobs": len(data.jobs)
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==================== 5. GET MATCHED CANDIDATES (Company) ====================
@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    """
    Company provides required skills, gets matched candidates
    Example: /api/candidates?skills=Python,React
    """
    try:
        skills_param = request.args.get('skills', '')
        required_skills = [s.strip() for s in skills_param.split(',') if s.strip()]
        
        if not required_skills:
            # Return all candidates if no filter
            return jsonify({"success": True, "count": len(data.candidates), "candidates": data.candidates})
        
        # Standardize required skills
        required_skills = [data.standardize_skill(s) for s in required_skills]
        
        # Match candidates
        matched = []
        for candidate in data.candidates:
            candidate_skills = [data.standardize_skill(s) for s in candidate['skills']]
            matching = set(required_skills) & set(candidate_skills)
            
            if matching:
                match_pct = round((len(matching) / len(required_skills)) * 100)
                matched.append({
                    **candidate,
                    "match_percentage": match_pct,
                    "matching_skills": list(matching),
                    "missing_skills": [s for s in required_skills if s not in candidate_skills]
                })
        
        # Sort by match percentage
        matched.sort(key=lambda x: x['match_percentage'], reverse=True)
        
        return jsonify({
            "success": True,
            "required_skills": required_skills,
            "count": len(matched),
            "candidates": matched
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==================== 6. FACULTY PROGRAMS ====================
@app.route('/api/faculty-programs', methods=['GET'])
def get_faculty_programs():
    """Get FDPs, workshops, research opportunities"""
    program_type = request.args.get('type')
    
    if program_type:
        filtered = [p for p in data.faculty_programs if p['type'].lower() == program_type.lower()]
        return jsonify({"success": True, "count": len(filtered), "programs": filtered})
    
    return jsonify({
        "success": True,
        "count": len(data.faculty_programs),
        "programs": data.faculty_programs
    })

# ==================== 7. ANALYTICS (Admin) ====================
@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get analytics for institution dashboard"""
    return jsonify({
        "success": True,
        "analytics": data.analytics
    })

# ==================== 8. SKILL GAP SUMMARY ====================
@app.route('/api/skill-gap', methods=['GET'])
def skill_gap():
    """Get overall skill gap summary for institutions"""
    return jsonify({
        "success": True,
        "most_missing_skills": data.analytics['skill_gap_summary']['most_missing_skills'],
        "most_available_skills": data.analytics['skill_gap_summary']['most_available_skills'],
        "recommendation": "Focus on AI/ML, Docker, and AWS training programs"
    })

# ==================== 9. GET ALL SKILLS (for standardization) ====================
@app.route('/api/skills', methods=['GET'])
def get_skills():
    """Get master list of all skills"""
    return jsonify({
        "success": True,
        "count": len(data.all_skills),
        "skills": data.all_skills
    })

# ==================== RUN SERVER ====================
if __name__ == '__main__':
    print("=" * 60)
    print("🚀 AYUSH-SETU BACKEND SERVER STARTING...")
    print("=" * 60)
    print("📍 Server URL: http://localhost:5000")
    print("📍 API Base:   http://localhost:5000/api")
    print("=" * 60)
    print("\n✅ Available Endpoints:")
    print("   POST /api/login")
    print("   POST /api/assessment")
    print("   GET  /api/jobs")
    print("   POST /api/post-job")
    print("   GET  /api/candidates?skills=Python,React")
    print("   GET  /api/faculty-programs")
    print("   GET  /api/analytics")
    print("   GET  /api/skill-gap")
    print("   GET  /api/skills")
    print("=" * 60)
    print("\n💡 Press CTRL+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)