// ==================== CONFIGURATION ====================
const API_URL = 'https://endurance-snazzy-gown.ngrok-free.dev/api';

// ==================== AUTHENTICATION ====================
function login(username, password, role) {
    fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            localStorage.setItem('user', JSON.stringify(data.user));
            alert(`Welcome ${data.user.name}!`);
            if (role === 'student') window.location.href = 'student.html';
            else if (role === 'company') window.location.href = 'company.html';
            else if (role === 'faculty') window.location.href = 'faculty.html';
            else if (role === 'admin') window.location.href = 'admin.html';
        } else {
            alert('Login failed: ' + data.message);
        }
    })
    .catch(err => alert('Error: ' + err.message));
}

// ==================== STUDENT DASHBOARD ====================
function loadStudentDashboard() {
    fetch(`${API_URL}/jobs`)
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const jobList = document.getElementById('jobList');
            if (jobList) {
                jobList.innerHTML = data.jobs.slice(0, 5).map(job => {
                    const matchScore = Math.floor(Math.random() * 40) + 50;
                    const scoreClass = matchScore > 70 ? '' : (matchScore > 50 ? 'low' : 'very-low');
                    return `
                        <div class="job-item">
                            <div class="job-info">
                                <h4>${job.title}</h4>
                                <p><i class="fas fa-building"></i> ${job.company}</p>
                                <p><i class="fas fa-map-marker-alt"></i> ${job.location} | <i class="fas fa-money-bill"></i> ${job.salary}</p>
                                <div class="skill-tags">
                                    ${job.required_skills.map(s => `<span class="skill-tag need">${s}</span>`).join('')}
                                </div>
                            </div>
                            <div class="job-match">
                                <div class="match-score ${scoreClass}">${matchScore}%</div>
                                <div class="match-label">Match</div>
                                <button class="btn btn-primary btn-small" style="margin-top: 8px;">Apply</button>
                            </div>
                        </div>
                    `;
                }).join('');
            }
        }
    })
    .catch(err => console.log('Error loading jobs:', err));
}

// ==================== SKILL ASSESSMENT ====================
function submitAssessment() {
    const skills = ['Python', 'Java', 'HTML', 'CSS'];
    
    fetch(`${API_URL}/assessment`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            skills: skills,
            career_interest: 'Software Developer'
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            displayAssessmentResults(data);
        }
    })
    .catch(err => console.log('Error:', err));
}

function displayAssessmentResults(data) {
    const resultContent = document.getElementById('resultContent');
    if (!resultContent) return;
    
    resultContent.innerHTML = `
        <div class="result-box">
            <h3>📊 Your Skill Profile</h3>
            
            <div class="analysis-item">
                <h4>Industry Match Score: ${data.match_score}%</h4>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${data.match_score}%;">${data.match_score}%</div>
                </div>
            </div>
            
            <h3>✅ Your Skills</h3>
            <div class="skill-tags">
                ${data.student_skills.map(s => `<span class="skill-tag have">${s}</span>`).join('')}
            </div>
            
            <h3>❌ Missing Skills</h3>
            <div class="skill-tags">
                ${data.missing_skills.map(s => `<span class="skill-tag missing">${s}</span>`).join('')}
            </div>
            
            <h3>💼 Recommended Jobs</h3>
            ${data.job_recommendations.slice(0, 3).map(job => `
                <div class="job-item" style="margin-bottom: 10px;">
                    <div class="job-info">
                        <h4>${job.title}</h4>
                        <p>${job.company} | ${job.location}</p>
                    </div>
                    <div class="job-match">
                        <div class="match-score ${job.match_percentage > 70 ? '' : 'low'}">${job.match_percentage}%</div>
                    </div>
                </div>
            `).join('')}
            
            <h3>📚 Recommended Learning Path</h3>
            <ul style="margin-left: 20px; margin-top: 10px;">
                ${data.learning_path.map(item => 
                    `<li style="margin-bottom: 8px;"><strong>${item.skill}:</strong> ${item.course} (${item.duration})</li>`
                ).join('')}
            </ul>
        </div>
    `;
}

// ==================== COMPANY DASHBOARD ====================
function loadCompanyDashboard() {
    fetch(`${API_URL}/candidates`)
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const candidateList = document.getElementById('candidateList');
            if (candidateList) {
                candidateList.innerHTML = data.candidates.map(c => {
                    const matchScore = Math.floor(Math.random() * 30) + 70;
                    return `
                        <div class="candidate-item">
                            <div class="candidate-info">
                                <h4>${c.name}</h4>
                                <p>${c.education} | CGPA: ${c.cgpa}</p>
                                <div class="skill-tags">
                                    ${c.skills.map(s => `<span class="skill-tag have">${s}</span>`).join('')}
                                </div>
                            </div>
                            <div class="job-match">
                                <div class="match-score">${matchScore}%</div>
                                <div class="match-label">Match</div>
                                <button class="btn btn-success btn-small" style="margin-top: 8px;">Shortlist</button>
                            </div>
                        </div>
                    `;
                }).join('');
            }
        }
    })
    .catch(err => console.log('Error:', err));
}

function postJob(event) {
    event.preventDefault();
    const title = document.getElementById('jobTitle').value;
    const skills = document.getElementById('jobSkills').value.split(',').map(s => s.trim());
    const type = document.getElementById('jobType').value;
    
    fetch(`${API_URL}/post-job`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            title: title,
            company: 'Google India',
            skills: skills,
            type: type,
            experience: 'Fresher',
            location: 'Bangalore',
            salary: '12-18 LPA',
            description: 'Great opportunity!'
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            document.getElementById('jobPostResult').innerHTML = `
                <div class="success-message">
                    ✅ Job "${data.job.title}" posted successfully!<br>
                    <strong>AI has started matching candidates...</strong>
                </div>
            `;
            document.getElementById('jobForm').reset();
        }
    })
    .catch(err => alert('Error: ' + err.message));
}

// ==================== FACULTY DASHBOARD ====================
function loadFacultyDashboard() {
    fetch(`${API_URL}/faculty-programs`)
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const programList = document.getElementById('programList');
            if (programList) {
                programList.innerHTML = data.programs.map(p => `
                    <div class="job-item">
                        <div class="job-info">
                            <h4>${p.name}</h4>
                            <p><i class="fas fa-tag"></i> ${p.type} | <i class="fas fa-clock"></i> ${p.duration}</p>
                            <p><i class="fas fa-university"></i> ${p.organized_by} | <i class="fas fa-rupee-sign"></i> ${p.fee}</p>
                        </div>
                        <button class="btn btn-primary btn-small">Apply</button>
                    </div>
                `).join('');
            }
        }
    })
    .catch(err => console.log('Error:', err));
}

// ==================== ADMIN DASHBOARD ====================
function loadAdminDashboard() {
    fetch(`${API_URL}/analytics`)
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const a = data.analytics;
            
            // Update stats
            document.getElementById('totalStudents') && (document.getElementById('totalStudents').textContent = a.total_students);
            document.getElementById('totalCompanies') && (document.getElementById('totalCompanies').textContent = a.total_companies);
            document.getElementById('totalJobs') && (document.getElementById('totalJobs').textContent = a.total_jobs_posted);
            document.getElementById('totalHired') && (document.getElementById('totalHired').textContent = a.total_hired);
            document.getElementById('placementRate') && (document.getElementById('placementRate').textContent = a.placement_rate);
            document.getElementById('avgPackage') && (document.getElementById('avgPackage').textContent = a.avg_package);
            
            // Skill demand
            const skillDemand = document.getElementById('skillDemand');
            if (skillDemand) {
                skillDemand.innerHTML = a.top_skills_demand.map(s => `
                    <div class="demand-bar">
                        <span>${s.skill}</span>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: ${s.demand}%;"></div>
                        </div>
                        <span>${s.demand}%</span>
                    </div>
                `).join('');
            }
        }
    })
    .catch(err => console.log('Error:', err));
}

// ==================== UTILITIES ====================
function logout() {
    localStorage.removeItem('user');
    window.location.href = 'index.html';
}

function getUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
}