# VulnX 🛡️

> Website Vulnerability Scanner for Security Awareness & Educational Testing

VulnX is a cybersecurity-focused web application designed to analyze websites for common security misconfigurations and basic vulnerabilities in a safe and educational environment.

The project focuses on vulnerability awareness, security reporting, and defensive security learning through an interactive scanning dashboard and risk visualization system.

---

## ⚠️ Ethical Use Notice

VulnX was developed strictly for educational purposes and authorized security testing.

Users must only scan websites or systems they own or have explicit permission to assess.

Unauthorized scanning or misuse may violate laws or organizational policies.

The authors are not responsible for misuse of this project.

---

## ✨ Features

### 🔍 Security Scanning
- HTTPS configuration analysis
- HTTP security header analysis
- Basic SQL injection pattern detection
- Vulnerability severity classification

---

### 📊 Security Reporting Dashboard
- Dynamic security score calculation
- Risk-level visualization
- Secure / Warning / Critical categorization
- Interactive vulnerability breakdown

---

### 🖥️ Interactive UI
- Live scan progress tracking
- Terminal-style scan logs
- Animated security score ring
- Modal-based vulnerability explanations
- Cybersecurity-inspired responsive interface

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript

### Backend
- Python
- FastAPI

### Additional Technologies
- localStorage
- REST API communication
- Async scanning workflow

---

## 📂 Project Structure

```text
vulnx/
├── index.html
├── scan.html
├── report.html
├── style.css
├── script.js
├── main.py
├── scanner.py
├── headers.py
├── security.py
├── sql.py
├── scoring.py
├── validation.py
└── README.md
```

---

## 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

---

### 2. Install Dependencies

```bash
pip install fastapi uvicorn httpx validators
```

---

### 3. Start the Backend Server

```bash
uvicorn main:app --reload
```

---

### 4. Run the Frontend

Open `index.html` in your browser.

---

## 📚 Key Concepts Learned

- Frontend and backend integration
- REST API communication
- Asynchronous programming
- Vulnerability assessment concepts
- Security header analysis
- UI/UX design for cybersecurity tools
- Dynamic report generation
- Risk scoring systems

---

## 🌱 Future Improvements

Planned future upgrades include:

- Expanded vulnerability checks
- Advanced reporting system
- PDF report export
- Authentication system
- Database integration
- Rate limiting and scan validation
- Deployment support
- Real-time analytics
- Improved scan engine architecture

---

## 💡 Project Goal

VulnX was built to explore how vulnerability assessment tools work while promoting security awareness and responsible cybersecurity practices.

The goal is not offensive exploitation, but understanding common security weaknesses and encouraging safer web configurations.

---

## 👥 Team

This project was developed collaboratively as part of a cybersecurity project initiative.

### Contributions

- **Shraddha Shinde** — Frontend development, UI/UX design, report interface, integration
- **Rau Yelamkar** — Backend development and API handling
- **Shravani Kurade** — Research and documentation
- **Rishi Raj Chaudhary** — Research and project support